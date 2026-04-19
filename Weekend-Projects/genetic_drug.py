import pandas as pd
import numpy as np
import random
from rdkit import Chem
from rdkit.Chem import BRICS, AllChem, Descriptors, Draw
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from rdkit import RDLogger
RDLogger.DisableLog('rdApp.*')

df_test = pd.read_csv('dataset_chembl.csv').dropna()
df = df_test.sample(random_state=42, n=1000)

def smiles_to_features(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
        mw = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        hbd = Descriptors.NumHDonors(mol)
        tpsa = Descriptors.TPSA(mol)
        return pd.Series([fp, mw, logp, hbd, tpsa])
    
df[['fingerprint', 'molecular_weight', 'logp', 'hbd', 'tpsa']] = df['SMILES'].apply(smiles_to_features)
df['BBB_Permeability'] = np.where(
    (df['molecular_weight'] < 500) & 
    (df['logp'] < 5) & 
    (df['hbd'] < 5) & 
    (df['tpsa'] < 90), 1, 0 
) # 1 for bbb+, 0 for bbb-
# df.to_csv('processed_dataset.csv', index=False)
# Seed list : Extract only the elite candidates ( BBB == 1 ) for the initial gene pool
f0_seed_list = df[df['BBB_Permeability'] == 1]['SMILES'].tolist()
# AI SCORING 
X = np.array(list(df['fingerprint']))
y = np.array(df['BBB_Permeability'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# BRICS fragmentation
# Extract only the fragment unique to set
def brics_fragments(smiles): 
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        fragments = BRICS.BRICSDecompose(mol)
        return fragments
    return set()
fragments_pool = df['SMILES'].apply(brics_fragments).explode().unique()

def RO3(smiles):
    '''
    Rule of Three (RO3) filter:
    Ensures fragments are small and soluble to prevent molecular obesity upon recombination
    '''
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        mw = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        hbd = Descriptors.NumHDonors(mol)
        tpsa = Descriptors.TPSA(mol)
        if mw < 300 and logp < 3 and hbd < 3 and tpsa < 60:
            return True
        return False
valid_fragments_pool = [] # list valid fragments for replace in mutation function
for idx,fragments_pool in enumerate(fragments_pool):
    if RO3(fragments_pool):
       valid_fragments_pool.append(fragments_pool)

# GENETICS ALGORITHM
# STEP 1: CROSSOVER 

def crossover(male, female):
    parent1 = Chem.MolFromSmiles(male)
    parent2 = Chem.MolFromSmiles(female)
    if parent1 is None or parent2 is None:
        return None
    frag1 = BRICS.BRICSDecompose(parent1)
    frag2 = BRICS.BRICSDecompose(parent2)
    # Create a pool for crossover 
    pool = list(set(frag1)) + list(set(frag2))
    pool_frag = [Chem.MolFromSmiles(f) for f in pool if f]
    # Crossover
    builder = BRICS.BRICSBuild(pool_frag)
    try:
        child = next(builder) # Get the child from the builder
        child.UpdatePropertyCache(strict=False)
        return Chem.MolToSmiles(child) # Return the smiles of the child
    except StopIteration:
        return None
# Yeah 'combie' two valid fragments after BRICS smiles object in f0_seed_list
# STEP 2: MUTATION
def mutation(smiles, pool, mutation_rate=0.4):
    if random.random() > mutation_rate:
        return smiles
    random_frag = random.choice(pool) # pool is valid_fragments_pool
    new_smiles = crossover(smiles, random_frag)
    return new_smiles if new_smiles else smiles
# 40% Probability: Randomly integrates an external fragment from the pool to introduce genetic diversity.
# STEP BY STEP: FITNESS
def fitness(smiles, ai): # dựa vào model đã trên ai sẽ tính tỉ lệ bbb+ của 1 phân tử 
    mol = Chem.MolFromSmiles(smiles)
    if mol is None: return 0.0

    fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
    pred_proba = ai.predict_proba([list(fp)])
    return float(pred_proba[0][1]) # Use probability conver binary system for calculation selection function
'''
Dựa vào model AI tính tỉ lệ của thỏa mãn của chất mới, thay vì dùng hệ nhị phân chúng ta dùng tỉ lệ cho chính xác
tỉ lệ thì có thể ví dụ như: 100 cây dự đoán, có 75 cái cây chọn 0, 25 cây chọn số 1. Thì tỉ lệ sẽ là 0.25
tỉ lệ là 'tỉ lệ' số cây số quyết định [1] 
'''
# STEP 3: SELECTION
def selection(population, ai, topk=10):
    scored_population = []
    for smiles in population:
        score = fitness(smiles, ai)
        scored_population.append((smiles, score))

    scored_population.sort(key=lambda x: x[1], reverse=True)
    return [item[0] for item in scored_population[:topk]]
# Nah slection top 10 score 'child'
# STEP 4: GENETIC ALGORITHM
def genetic_algorithm(pool, ai, seed_list, generations=3, pop_size=150):
    print("Starting Genetic Algorithm...")

    # Initalize F0 population
    population = random.sample(seed_list, min(pop_size, len(seed_list)))

    for gen in range(generations):
        print(f"Generation: {gen + 1} / {generations}")

        # 1. Selection phase
        selected_individuals = selection(population, ai, topk=10)
        if len(selected_individuals) < 2:
            print("Extinction")
            break

        new_pop = selected_individuals.copy() # Retain dominant traits

        # 2. Reproduction Phase to repopulate
        while len(new_pop) < pop_size:
            p1,p2 = random.sample(selected_individuals, 2)
            child = crossover(p1,p2)
            if child is not None:
                final_child = mutation(child, pool)

                new_pop.append(final_child)
        # Loop population for new generations
        population = new_pop
    return population

# Ignite the System Pipeline!
final_pop = genetic_algorithm(pool=valid_fragments_pool, ai=model, seed_list=f0_seed_list)
print(len(final_pop))



