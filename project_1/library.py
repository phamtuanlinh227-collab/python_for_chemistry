# library.py
from rdkit import Chem
from rdkit.Chem import Descriptors

# 1. TỪ ĐIỂN THUỐC (Bro có thể thêm 100 chất vào đây cũng được)
duoc_dien = {
    "Aspirin": {
        "smiles": "CC(=O)Oc1ccccc1C(=O)O",
        "temp_opt": 70.0,  # Nhiệt độ nấu lý tưởng
    },
    "Paracetamol": {
        "smiles": "CC(=O)Nc1ccc(O)cc1",
        "temp_opt": 80.0,
    },
    "Vitamin C": { 
        "smiles": "OCC(O)C1OC(=O)C(O)=C1O",
        "temp_opt": 40.0, 
    }
}

# 2. HÀM KIỂM TRA CHẤT LƯỢNG (Lipinski Rule)
def check_quality(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return None, 0, 0, "❌ Lỗi: Công thức SMILES không hợp lệ"
    
    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    
    # Kiểm tra luật Lipinski (Khối lượng < 500, LogP < 5)
    if mw <= 500 and logp <= 5:
        status = "✅ Đạt chuẩn Drug-like (Dễ hấp thu)"
    else:
        status = "⚠️ Cảnh báo: Vi phạm Lipinski (Khó hấp thu)"
        
    return mol, mw, logp, status