from rdkit import Chem
from rdkit.Chem import Draw

# 1. Định nghĩa phân tử bằng mã SMILES
# Đây là Cafein (Thứ bro miễn nhiễm ấy :v)
cafein_smiles = "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"

# 2. Dịch từ Text sang Đối tượng Phân tử (Object)
mol = Chem.MolFromSmiles(cafein_smiles)

# 3. Vẽ nó ra!
print("Đang vẽ Cafein...")
img = Draw.MolToImage(mol)

# 4. Hiển thị lên màn hình
img.show() 

# Nếu muốn lưu lại thành file ảnh thì dùng dòng dưới:
# img.save("cafein.png")

# Code structure supported by AI, customized by Tuan Linh
# Project: Chemistry Automation