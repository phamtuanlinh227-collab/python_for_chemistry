import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs

df = pd.read_csv('dataset_phase4.csv')
df = df.dropna(subset=['SMILES'])

target_name = 'ASPIRIN'
target_smile = "CC(=O)Oc1ccccc1C(=O)O"

target_mol = Chem.MolFromSmiles(target_smile)

target_fp = AllChem.GetMorganFingerprintAsBitVect(target_mol, 2, nBits=1024)

results = []
for index, row in df.iterrows():
    smiles = row['SMILES']
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
        similarity = DataStructs.TanimotoSimilarity(target_fp, fp)
        results.append({
            'SMILES': smiles,
            'Similarity': round(similarity * 100, 2)
        })

results_df = pd.DataFrame(results)
top_5 = results_df.sort_values(by='Similarity', ascending=False).head(5)

print(top_5.to_string(index=False))
"""
um, this code read a dataset of chemical compounds, calculates the Taimoto similarity of each compound
to the target compound (ASPIRIN),
and prints 5 coumpounds with 'highest similarity' percentage"""