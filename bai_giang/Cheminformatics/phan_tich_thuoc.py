from rdkit import Chem
from rdkit.Chem import Descriptors

# 1. Danh sách thuốc cần soi (Tên: SMILES)
tu_thuoc = {
    "Cafein": "CN1C=NC2=C1C(=O)N(C(=O)N2C)C",
    "Paracetamol": "CC(=O)Nc1ccc(O)cc1",
    "Aspirin": "CC(=O)Oc1ccccc1C(=O)O",
    "Vitamin C": "OCC(O)C1OC(=O)C(O)=C1O" # Cấu trúc phức tạp hơn
}

print(f"{'TÊN THUỐC':<15} | {'KL PHÂN TỬ (g/mol)':<20} | {'ĐỘ TAN (LogP)':<15}")
print("-" * 60)

for ten, smiles in tu_thuoc.items():
    # Biến text thành Object
    mol = Chem.MolFromSmiles(smiles)
    
    if mol: # Nếu công thức đúng
        # --- TÍNH TOÁN Ở ĐÂY ---
        khoi_luong = Descriptors.MolWt(mol)
        do_tan = Descriptors.MolLogP(mol)
        
        # In ra bảng đẹp
        print(f"{ten:<15} | {khoi_luong:<20.2f} | {do_tan:<15.2f}")

from rdkit import Chem
from rdkit.Chem import Descriptors

# Hàm kiểm tra chuẩn Lipinski (Bộ lọc)
def check_lipinski(mol):
    # 1. Tính toán 4 chỉ số cốt tử
    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    h_donors = Descriptors.NumHDonors(mol)
    h_acceptors = Descriptors.NumHAcceptors(mol)
    
    # 2. Kiểm tra điều kiện (Logic IF-ELSE thần thánh)
    vi_pham = 0
    if mw > 500: vi_pham += 1
    if logp > 5: vi_pham += 1
    if h_donors > 5: vi_pham += 1
    if h_acceptors > 10: vi_pham += 1
    
    # 3. Kết luận
    if vi_pham <= 1:
        return "✅ ĐẠT CHUẨN (Drug-like)"
    else:
        return f"❌ LOẠI (Vi phạm {vi_pham} quy tắc)"

# --- MAIN ---
tu_thuoc_moi = {
    "Aspirin": "CC(=O)Oc1ccccc1C(=O)O",
    "Paclitaxel (K Ung thư)": "CC1=C2C(C(=O)C3(C(CC4C(C3C(C(C2(C)C)(CC1OC(=O)C(C(C5=CC=CC=C5)NC(=O)C6=CC=CC=C6)O)O)OC(=O)C7=CC=CC=C7)(CO4)OC(=O)C)O)C)OC(=O)C", 
    # Paclitaxel là thuốc trị ung thư cực mạnh nhưng cấu trúc siêu to khổng lồ
}

print(f"{'TÊN THUỐC':<25} | {'KẾT QUẢ SÀNG LỌC'}")
print("-" * 50)

for ten, smiles in tu_thuoc_moi.items():
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        ket_luan = check_lipinski(mol)
        print(f"{ten:<25} | {ket_luan}")

# Code structure supported by AI, customized by Tuan Linh
# Project: Chemistry Automation