import pandas as pd
import glob
import numpy as np

print("📡 BẬT RADAR QUÉT THƯ MỤC 'Du_Lieu_Lab'...\n")

# 1. Quét tìm MỌI file .xlsx nằm TRONG thư mục Du_Lieu_Lab
danh_sach_file = glob.glob("Du_Lieu_Lab/*.xlsx")

# Chuẩn bị cái thùng
thung_chua = []

# Đọc lần lượt 100 file nhét vào thùng
for file in danh_sach_file:
    df_tam = pd.read_excel(file)
    thung_chua.append(df_tam)

# 2. GỘP CẢ 100 FILE THÀNH 1 BẢNG (Chứa 500 sinh viên)
bang_tong = pd.concat(thung_chua, ignore_index=True)

# 3. TÍNH GPA CHO 500 ĐỨA BẰNG 1 DÒNG CODE NUMPY
bang_tong['GPA'] = np.round((bang_tong['Toan'] + bang_tong['Ly'] + bang_tong['Hoa']) / 3, 2)

print(f"👑 ĐÃ GỘP THÀNH CÔNG {len(bang_tong)} SINH VIÊN!")
print(bang_tong.head(10)) # In 10 đứa đầu tiên cho gọn
print("-" * 50)

# 4. TRUY TÌM BÁO THỦ (Toán < 5.0)
bao_thu = bang_tong[bang_tong['Toan'] < 5.0]

print(f"💀 PHÁT HIỆN {len(bao_thu)} BÁO THỦ TẠCH TOÁN! Danh sách 5 đứa đầu:")
print(bao_thu[['Ma_SV', 'Toan', 'GPA']].head(5))

# Xuất ra 1 file Excel tổng kết cuối cùng nộp hiệu trưởng
bang_tong.to_excel("Bao_Cao_Tong_500_SV.xlsx", index=False)
