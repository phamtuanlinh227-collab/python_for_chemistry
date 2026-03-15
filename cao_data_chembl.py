import pandas as pd
from chembl_webresource_client.new_client import new_client

print("🌍 Đang kết nối với Trụ sở dữ liệu Y Tế Châu Âu (ChEMBL)...")

# 1. Gọi ông bồi bàn phụ trách mảng Phân tử (Molecule)
phan_tu_api = new_client.molecule

# 2. Ghi Order: "Lấy cho tao 10 chất đã làm thuốc thật (max_phase=4)"
print("🏃 Bồi bàn đang chạy đi lấy Data. Chờ xíu nhé...")
ket_qua = phan_tu_api.filter(max_phase=4)[0:10] # [0:10] là chỉ lấy 10 thằng đầu tiên cho lẹ

# 3. Chuyển đống Data lộn xộn bồi bàn mang về thành Bảng Pandas cho đẹp
danh_sach_thuoc = []

for chat in ket_qua:
    # Lấy Tên thuốc (nếu có)
    ten = chat.get('pref_name', 'Không có tên')
    
    # Moi cái mã SMILES từ trong cấu trúc (nếu có)
    smiles = None
    if chat.get('molecule_structures'):
        smiles = chat['molecule_structures'].get('canonical_smiles')
        
    # Cho vào rổ
    danh_sach_thuoc.append({
        'ID_ChEMBL': chat['molecule_chembl_id'],
        'Ten_Thuoc': ten,
        'SMILES': smiles
    })

# 4. Ép vào khuôn Pandas và khoe thành quả
df = pd.DataFrame(danh_sach_thuoc)

print("\n🎉 BÙM! HÀNG ĐÃ VỀ TỪ CHÂU ÂU:")
print(df)

# (Tùy chọn) Xuất luôn ra Excel để xem cho sướng
# df.to_excel('data_tu_chau_au.xlsx', index=False)