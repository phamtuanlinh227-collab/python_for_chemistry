import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from sklearn.ensemble import RandomForestClassifier
import time

print("🔮 KHỞI ĐỘNG CỖ MÁY TIÊN TRI AI...\n")

# ==========================================
# BƯỚC 1: DỮ LIỆU HUẤN LUYỆN (Dạy AI phân biệt Thiện - Ác)
# 1 = Thuốc an toàn, 0 = Chất độc
# ==========================================
data = {
    'Ten_Chat': ['Paracetamol', 'Aspirin', 'Vitamin C', 'Benzen', 'Cyanide', 'Phenol'],
    'SMILES': ['CC(=O)Nc1ccc(O)cc1', 'CC(=O)Oc1ccccc1C(=O)O', 'C1(C(C(O1)(CO)O)O)=O', 'c1ccccc1', 'C#N', 'Oc1ccccc1'],
    'Nhan_Hieu': [1, 1, 1, 0, 0, 0] # AI sẽ nhìn vào cột này để tự rút ra bài học!
}
df = pd.DataFrame(data)

# ==========================================
# BƯỚC 2: RDKIT + NUMPY (Băm thuốc thành Ma trận 0 và 1)
# ==========================================
print("⚙️ Đang băm nát cấu trúc để đút cho AI ăn...")
danh_sach_ma_tran = []

for smiles in df['SMILES']:
    phan_tu = Chem.MolFromSmiles(smiles)
    # Tạo Vân tay phân tử (Bán kính 2, dài 1024 bit)
    van_tay = AllChem.GetMorganFingerprintAsBitVect(phan_tu, 2, nBits=1024)
    
    # Ép kiểu sang Numpy Array (Cái Casio siêu cấp)
    ma_tran = np.zeros((0,), dtype=np.int8)
    Chem.DataStructs.ConvertToNumpyArray(van_tay, ma_tran)
    danh_sach_ma_tran.append(ma_tran)

X_train = np.array(danh_sach_ma_tran) # Trục X: Đề bài (Cấu trúc Hóa học)
y_train = df['Nhan_Hieu'].values      # Trục Y: Đáp án (1 hoặc 0)

# ==========================================
# BƯỚC 3: DẠY AI (Thuật toán Trồng Rừng - Random Forest)
# ==========================================
print("🧠 AI đang động não tìm quy luật ẩn...")
mo_hinh_ai = RandomForestClassifier(n_estimators=100, random_state=42)
mo_hinh_ai.fit(X_train, y_train) # CÂU THẦN CHÚ THIÊNG LIÊNG NHẤT NGÀNH AI!
print("✅ AI BẢO: 'TÔI ĐÃ HỌC XONG!'\n")

# ==========================================
# BƯỚC 4: BÀI TEST THỰC CHIẾN TẬP 2
# ==========================================
print("🧪 ĐEM THUỐC GIẢM ĐAU (Ibuprofen) VÀO THỬ NGHIỆM:")
chat_la = "CC(C)Cc1ccc(cc1)C(C)C(=O)O" # Chuỗi SMILES của Ibuprofen

# Băm thuốc y như cũ
pt_la = Chem.MolFromSmiles(chat_la)
vt_la = AllChem.GetMorganFingerprintAsBitVect(pt_la, 2, nBits=1024)
mt_la = np.zeros((0,), dtype=np.int8)
Chem.DataStructs.ConvertToNumpyArray(vt_la, mt_la)

# Hỏi cỗ máy tiên tri
du_doan = mo_hinh_ai.predict([mt_la])

if du_doan[0] == 1:
    print("👉 PHÁN QUYẾT TỪ AI: 🟢 CHẤT NÀY AN TOÀN! (Có thể làm thuốc)")
else:
    print("👉 PHÁN QUYẾT TỪ AI: 🔴 ĐỘC HẠI! (Cảnh báo, tránh xa!!!)")



# ==========================================
# BƯỚC 3: DẠY AI 
# ==========================================
mo_hinh_ai = RandomForestClassifier(n_estimators=100, random_state=42)

print("🧠 AI đang động não...")
bat_dau = time.time() # ⏱️ BẤM ĐỒNG HỒ!

mo_hinh_ai.fit(X_train, y_train)

ket_thuc = time.time() # ⏱️ DỪNG ĐỒNG HỒ!

thoi_gian_hoc = ket_thuc - bat_dau
print(f"✅ AI BẢO: 'TÔI ĐÃ HỌC XONG TRONG VÒNG {thoi_gian_hoc:.4f} GIÂY!'\n")