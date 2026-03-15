import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors

print("Khởi động màng lọc thuốc")
danh_sach = {
    'Ten_Chat': ['Nước', 'Paracetamol', 'Aspirin', 'Benzen', 'Vitamin C'],
    'SMILES': ['O', 'CC(=O)Nc1ccc(O)cc1', 'CC(=O)Oc1ccccc1C(=O)O', 'c1ccccc1', 'C1(C(C(O1)(CO)O)O)=O']
}
df = pd.DataFrame(danh_sach)

khoi_luong_list = []
logp_list = []
phan_quyet_list = []

for smiles in df['SMILES']:
    mol = Chem.MolFromSmiles(smiles)
    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)

    khoi_luong_list.append(mw)
    logp_list.append(logp)
    if mw < 500 and logp < 5:
        phan_quyet_list.append('Đạt')
    else:
        phan_quyet_list.append('Không đạt')
    
df['Khoi_Luong'] = khoi_luong_list
df['LogP'] = logp_list
df['Phan_Quyet'] = phan_quyet_list
print(df)
df.to_excel('bao_cao_loc_thuoc.xlsx', index=False)