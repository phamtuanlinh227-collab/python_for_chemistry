import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv('dataset_phase4.csv')

mw_list = []
logp_list = []
tspa_list = []
bbb_permeability = []    # Index: 1 for permeability, 0 for non-permeability
for smiles in df['SMILES']:
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        mw = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        tspa = Descriptors.TPSA(mol)

        mw_list.append(mw)
        logp_list.append(logp) 
        tspa_list.append(tspa)
    if mw <= 400 and logp <= 5 and tspa <= 90:
        bbb_permeability.append(1)
    else:
        bbb_permeability.append(0)

# Add the calculated properties and permeability to the DataFrame
df['Molecular_Weight'] = mw_list
df['LogP'] = logp_list
df['TPSA'] = tspa_list
df['BBB_Permeability'] = bbb_permeability
# Check
df = df.dropna()

BBB_counts = df['BBB_Permeability'].value_counts() # Count the number of compounds with BBB permeability and non-permeability
# Visualize the distribution of properties for BBB permeability and non-permeability of conpounds
plt.figure(figsize=(8, 6))
plt.pie(BBB_counts, labels=['BBB Permeability', 'Non Permeability'], autopct='%1.1f%%', colors=['#66b3ff', '#ff9999'], shadow=True)
plt.title('Distribution of BBB Permeability')
plt.show()

print(f"Successfully analyzed {len(df)} compounds.")