import pandas as pd
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import Descriptors
import time

thoi_gian_load = time.time()
df = pd.read_csv('kho_bau_1000_thuoc.csv')
print(f"Đã lôi {len(df)} chất từ kho báu trong khoảng thời gian: {time.time() - thoi_gian_load:.4f} giây")

khoi_luong_list = []
logp_list = []
for smiles in df['SMILES']:
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        khoi_luong_list.append(Descriptors.MolWt(mol))
        logp_list.append(Descriptors.MolLogP(mol))
    else:
        khoi_luong_list.append(None)
        logp_list.append(None)
df = df.dropna()  
df['Khối lượng phân tử'] = khoi_luong_list
df['LogP'] = logp_list

plt.figure(figsize=(10, 6))
plt.scatter(df['Khối lượng phân tử'], df['LogP'], alpha=0.5, edgecolors='skyblue')
plt.axvline(x=500, color='red', linestyle='--', label='Khối lượng phân tử = 500')
plt.axhline(y=5, color='green', linestyle='--', label='LogP = 5')

plt.title('Phân bố Khối lượng phân tử và LogP của 1000 chất')
plt.xlabel('Khối lượng phân tử')
plt.ylabel('LogP')
plt.legend()
plt.grid()
plt.show()
