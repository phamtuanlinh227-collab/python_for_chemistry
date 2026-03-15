import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from rdkit import Chem
from rdkit.Chem import Descriptors, AllChem
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

print(" KHỞI TẠO CHIẾN DỊCH HUẤN LUYỆN AI QUY MÔ LỚN.....\n")

# 1. PHÂN BIỆT THUỐC: 1 LÀ DỄ HẤP THỤ, 0 LÀ KHÓ HẤP THỤ
df = pd.read_csv('kho_bau_1000_thuoc.csv')

nhan_hieu = []
for smiles in df['SMILES']:
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        logp = Descriptors.MolLogP(mol)
        mw = Descriptors.MolWt(mol)
        if logp <= 5 and mw <= 500:
            nhan_hieu.append(1)  # Dễ hấp thụ
        else:
            nhan_hieu.append(0)  # Khó hấp thụ
    else:
        nhan_hieu.append(None)  # Nếu không thể tạo phân tử, gán là khó hấp thụ

df['Nhan_hieu'] = nhan_hieu
df = df.dropna()
# 2. HUẤN LUYỆN MÔ HÌNH AI
print(" ĐANG BĂM NÁT 1000 THUỐC THÀNH CẤU TRÚC MA TRẬN.....\n")

X_ma_tran = []
Y_dap_an = df['Nhan_hieu'].values
for smiles in df['SMILES']:
    mol = Chem.MolFromSmiles(smiles)
    van_tay = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
    arr = np.zeros((0,), dtype=np.int8)
    Chem.DataStructs.ConvertToNumpyArray(van_tay, arr)
    X_ma_tran.append(arr)

X_ma_tran = np.array(X_ma_tran)
# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
x_test, x_train, y_test, y_train = train_test_split(X_ma_tran, Y_dap_an, test_size=0.2, random_state=42)
# Huấn luyện mô hình Random Forest
print("ĐANG HỌC 800 THUỐC....\n")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train,y_train)
print("ĐANG KIỂM TRA 200 THUỐC....\n")

# Đánh giá mô hình trên tập kiểm tra
from sklearn.metrics import confusion_matrix

ma_tran = confusion_matrix(y_test, model.predict(x_test))
sns.heatmap(ma_tran, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Dễ hấp thụ', 'Khó hấp thụ'],
            yticklabels=['Dễ hấp thụ', 'Khó hấp thụ'])
plt.xlabel('Dự đoán')  
plt.ylabel('Thực tế')
plt.title('Ma trận nhầm lẫn')   
plt.show()




    