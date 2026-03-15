import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors
import matplotlib.pyplot as plt

print("COMPARING DRUGS TO LIPINSKI'S RULE: PHASE 1 vs PHASE 4")
# Load the datasets
phase1_df = pd.read_csv('dataset_phase1.csv')
phase4_df = pd.read_csv('dataset_phase4.csv')
# Function to calculate Lipinski's rule paramates ( hàm tính tham số theo quy tắc của lipinski )
def calculate_lipinski (smiles_list):
    lipinski_results = 0
    for smiles in smiles_list:
        mol = Chem.MolFromSmiles(smiles)
        if mol is not None:
            mw = Descriptors.MolWt(mol) # molecular weight
            logp = Descriptors.MolLogP(mol) # logp
            if mw <= 500 and logp <= 5:
                lipinski_results += 1
    return lipinski_results
# Calculate Lipinski's rule parmates for both datasets
phase1_lipinski = calculate_lipinski(phase1_df['SMILES'])
phase4_lipinski = calculate_lipinski(phase4_df['SMILES'])
# Calculate percentages
phase1_percentages = (phase1_lipinski / len(phase1_df)) * 100
phase4_percentages = (phase4_lipinski / len(phase4_df)) * 100
# Draw a bar chart to compare the results
labels = ['Phase 1', 'Phase 4']
percentages = [phase1_percentages, phase4_percentages]
colors = ['red', 'green']

plt.figure(figsize=(8,6))
plt.bar(labels, percentages, color=colors)
plt.title('Comparison of Drugs Meeting Lipinski\'s Rule')
plt.ylabel('Percentages of Drugs Meeting Lipinski\'s Rule (%)')
plt.ylim(0, 100)
plt.show()
