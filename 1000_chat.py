import pandas as pd
from chembl_webresource_client.new_client import new_client
import time

print("🌍 Đang hack vào Trụ sở dữ liệu Y Tế Châu Âu (ChEMBL)...")
phan_tu_api = new_client.molecule

print("🏃 Bồi bàn đang chạy đi bốc 1.000 hồ sơ thuốc Phase 4... (Đi pha ly cafe đi sếp, khâu này hơi lâu!)")
bat_dau = time.time()

# 1. BỐC 1000 CHẤT (Tăng giới hạn lên [0:1000])
ket_qua = phan_tu_api.filter(max_phase=4)[0:1000] 

danh_sach_thuoc = []
for chat in ket_qua:
    ten = chat.get('pref_name', 'Không_tên')
    smiles = None
    if chat.get('molecule_structures'):
        smiles = chat['molecule_structures'].get('canonical_smiles')
        
    danh_sach_thuoc.append({
        'ID_ChEMBL': chat['molecule_chembl_id'],
        'Ten_Thuoc': ten,
        'SMILES': smiles
    })

# 2. ĐÚC VÀO KHUÔN PANDAS
df = pd.DataFrame(danh_sach_thuoc)
so_luong_ban_dau = len(df)
print(f"\n📦 Bồi bàn đã về! Mang theo {so_luong_ban_dau} chất. Thời gian: {time.time() - bat_dau:.1f} giây.")

# ==========================================
# 3. BƯỚC SỐNG CÒN: DỌN RÁC BẰNG PANDAS
# ==========================================
print("🧹 Đang gọi lao công Pandas ra soi rác (tìm những chất bị khuyết mã SMILES)...")

# Phép thuật dọn rác: Xóa sạch những dòng mà cột 'SMILES' bị trống (NaN)
df_sach = df.dropna(subset=['SMILES'])
so_luong_sau_don = len(df_sach)

print(f"✅ Dọn xong! Đã vứt thẳng tay {so_luong_ban_dau - so_luong_sau_don} hồ sơ rác xuống biển.")
print(f"💎 Kho báu còn lại: {so_luong_sau_don} chất chuẩn chỉnh 100% để luyện AI!")

# In 5 dòng đầu ra ngắm thử (dùng lệnh .head() cho đỡ lag màn hình)
print("\n👉 Trích xuất 5 dòng đầu tiên của Data Sạch:")
print(df_sach.head())

# (Tùy chọn) Lưu kho báu này lại để mai mốt xài, khỏi mắc công cào lại
df_sach.to_csv('kho_bau_1000_thuoc.csv', index=False)