import pandas as pd
import numpy as np

print("🚀 KHỞI ĐỘNG HỆ THỐNG DỌN RÁC...\n")

# 1. GIẢ LẬP FILE EXCEL "BÁO THỦ"
data_rac = {
    'Ma_SV': ['SV01', 'SV02', 'SV03', np.nan, 'SV05'],
    'Diem_Lab': [8.5, np.nan, 9.0, np.nan, 4.0],  # SV02 bị quên nhập điểm
    'Danh_Gia': ['Tot', 'Kha', '   Tot   ', np.nan, 'Kem'] # SV03 gõ dư 1 đống khoảng trắng
}
df = pd.DataFrame(data_rac)

print("🤢 BẢNG DỮ LIỆU GỐC (Rác ngập đầu):")
print(df)
print("-" * 50)

# ==========================================
# 2. BẮT ĐẦU DỌN RÁC BẰNG 3 ĐƯỜNG KIẾM
# ==========================================

# ⚔️ Kiếm 1: Chém bay những dòng trống trơn (how='all' là xóa dòng nếu TẤT CẢ các cột đều trống)
df_sach = df.dropna(how='all') 

# ⚔️ Kiếm 2: Lấp hố bom. 
# Thằng SV02 thiếu điểm? Không thể xóa nó được! Dùng fillna() để nhét điểm trung bình của cả lớp vào chỗ trống đó.
diem_tb = df_sach['Diem_Lab'].mean()
df_sach['Diem_Lab'] = df_sach['Diem_Lab'].fillna(diem_tb)

# ⚔️ Kiếm 3: Cạo râu (xóa khoảng trắng thừa)
# Thằng SV03 gõ chữ "   Tot   " nhìn rất ngứa mắt. Dùng str.strip() để gọt sạch khoảng trắng 2 đầu.
df_sach['Danh_Gia'] = df_sach['Danh_Gia'].str.strip()

print("✨ BẢNG DỮ LIỆU SAU KHI DỌN SẠCH (Đẹp không tì vết):")
print(df_sach)
print("-" * 50)