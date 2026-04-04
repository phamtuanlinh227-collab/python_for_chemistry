from rdkit import Chem
from rdkit.Chem import BRICS, Descriptors

smiles = 'CC(=O)OC1=CC=CC=C1C(=O)O' # Aspirin
mol = Chem.MolFromSmiles(smiles)

fragments = BRICS.BRICSDecompose(mol) # BRICSDecompose return a set of unique fragments
print(f"Total fragments: {len(fragments)}")

for idx, smi in enumerate(fragments):
    print(f"Fragment {idx + 1}: {smi}")

fragment_mols = [Chem.MolFromSmiles(smi) for smi in fragments]

def validate_lipinski(mol):  # Quality check Lipinski's Rule of Three
    if mol is not None:
        mw = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        hbd = Descriptors.NumHDonors(mol)
        hba = Descriptors.NumHAcceptors(mol)
        if mw <= 300 and logp <= 3 and hbd <= 3 and hba <= 3:
            return True
        return False
     
valid_fragments = []   
for idx, mol in enumerate(fragment_mols):  
    if validate_lipinski(mol):
        valid_fragments.append(mol)
        print(f"Fragments_ID: {idx + 1} is valid according to Lipinski's Rule of Three.")
    else:
        print(f"Fragments_ID: {idx + 1} is NOT valid according to Lipinski's Rule of Three")

