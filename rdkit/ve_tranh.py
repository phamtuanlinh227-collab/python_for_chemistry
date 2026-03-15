from rdkit import Chem
from rdkit.Chem import Draw

print("🎨 Đang khởi động cỗ máy họa sĩ RDKit...")

# 1. Dán cái chuỗi SMILES tà đạo nhất của bro vào đây (nhớ giữ dấu nháy kép "")
smiles_khung = "CC1(C)[C@H](C(=O)O)N2C(=O)C[C@H]2S1(=O)=O"

# 2. Dịch từ chữ sang Thực thể Hóa học
quai_vat = Chem.MolFromSmiles(smiles_khung)

# 3. Vẽ nó ra thành một bức ảnh 2D cực xịn!
anh_2d = Draw.MolToImage(quai_vat, size=(600, 600))

print("📸 Chụp x-quang xong! Chuẩn bị mở ảnh...")
anh_2d.show() # Lệnh này sẽ bật cái trình xem ảnh mặc định của Windows lên