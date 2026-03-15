import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import Descriptors

print("Khởi động trạm cân phân tử")

danh_sach = {
    'Ten_Chat': ['Nước', 'Paracetamol', 'Aspirin', 'Benzen', 'Vitamin C'],
    'SMILES': ['O', 'CC(=O)Nc1ccc(O)cc1', 'CC(=O)Oc1ccccc1C(=O)O', 'c1ccccc1', 'C1(C(C(O1)(CO)O)O)=O']
}
df = pd.DataFrame(danh_sach)

khoi_luong_list = []
logp_list = []

for smiles in df['SMILES']:
    mol = Chem.MolFromSmiles(smiles)

    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)

    khoi_luong_list.append(mw)
    logp_list.append(logp)

df['Khoi_Luong'] = khoi_luong_list
df['LogP'] = logp_list

print(df)

plt.figure(figsize = (10, 5))
plt.bar(df['Ten_Chat'], df['Khoi_Luong'], color='skyblue', edgecolor='black')
plt.title('Khối lượng phân tử của các chất')
plt.xlabel('Tên chất')
plt.ylabel('Khối lượng phân tử (g/mol)')
plt.show()

df.to_excel('bao_cao_khoi_luong.xlsx', index=False)
