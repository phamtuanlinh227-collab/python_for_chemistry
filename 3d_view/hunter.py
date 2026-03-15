import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

# 1. ĐỌC FILE TỪ SẾP
df = pd.read_csv("thuoc_nhap_kho.csv", encoding="utf-8")

# 2. BÊ NGUYÊN HÀM KIỂM TRA LIPINSKI VÀO
def check_lipinski(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return 0, 0, "❌ Lỗi"
    
    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    
    if mw <= 500 and logp <= 5:
        return round(mw, 1), round(logp, 1), "✅ Đạt"
    else:
        return round(mw, 1), round(logp, 1), "⚠️ Loại"

# 3. CHẠY BĂNG CHUYỀN RDKIT (Quét diện rộng)
print("⏳ Đang thả RDKit vào quét kho dữ liệu...\n")

# Tạo 3 cái rổ trống để hứng kết quả
list_mw = []
list_logp = []
list_status = []

# Duyệt qua từng công thức SMILES trong cột "SMILES" của file Excel
for cong_thuc in df["SMILES"]:
    # Ném vào máy quét
    mw, logp, status = check_lipinski(cong_thuc)
    
    # Bỏ kết quả vào rổ
    list_mw.append(mw)
    list_logp.append(logp)
    list_status.append(status)

# 4. GẮN KẾT QUẢ VÀO BẢNG EXCEL GỐC
df["Khối Lượng"] = list_mw
df["LogP"] = list_logp
df["Đánh Giá"] = list_status

# 5. IN THÀNH QUẢ RA MÀN HÌNH
print("🚀 BẢNG BÁO CÁO SAU KHI SÀNG LỌC:")
print(df.to_string())

# --- VIẾT TIẾP VÀO CUỐI FILE ---

# 6. LỌC LẤY CHẤT XỊN (Tuyệt chiêu Filter của Pandas)
# Lệnh này nghĩa là: "Chỉ giữ lại những hàng mà cột Đánh Giá có chữ ✅ Đạt"
df_xin = df[df["Đánh Giá"] == "✅ Đạt"]

print("\n💎 DANH SÁCH CHẤT XỊN ĐÃ ĐƯỢC LỌC RA:")
print(df_xin.to_string())

# 7. XUẤT RA FILE MỚI ĐỂ GỬI SẾP
# Tham số index=False để nó không in cái cột số thứ tự 0, 1, 2... thừa thãi ra
df_xin.to_csv("thuoc_xin_gui_sep.csv", index=False, encoding="utf-8")

print("\n📁 Đã xuất file 'thuoc_xin_gui_sep.csv' thành công! Tắt máy đi nhậu thôi bro!")