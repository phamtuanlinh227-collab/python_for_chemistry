import pandas as pd
import numpy as np

print("🚀 KHỞI ĐỘNG HỆ THỐNG QUÉT ĐIỂM...\n")

# 1. TẠO BẢNG DỮ LIỆU (DataFrame của Pandas)
# Tưởng tượng đây là cái bảng Excel có 5 sinh viên
data = {
    'Ten': ['An', 'Binh', 'Cuong', 'Dung', 'Eo'],
    'Toan': [8.5, 3.5, 9.0, 6.0, 4.0],
    'Ly': [7.0, 4.0, 9.5, 6.5, 5.0],
    'Anh': [9.0, 5.0, 10.0, 7.0, 4.5]
}
df = pd.DataFrame(data)

print("📋 BẢNG ĐIỂM GỐC:")
print(df)
print("-" * 40)

# 2. SỨC MẠNH NUMPY: TÍNH TOÁN ĐỒNG LOẠT (Vectorization)
# Cộng 3 cột lại chia 3, rồi dùng np.round để làm tròn 2 chữ số thập phân
# Chỉ 1 dòng code, nó tính xong cho cả lớp!
df['GPA'] = np.round((df['Toan'] + df['Ly'] + df['Anh']) / 3, 2)

print("🎯 BẢNG ĐIỂM SAU KHI TÍNH GPA:")
print(df)
print("-" * 40)

# 3. SỨC MẠNH PANDAS: THAO TÚNG VÀ LỌC DỮ LIỆU
# Lọc ra những đứa GPA >= 8.0
hao_han = df[ df['GPA'] >= 8.0 ]

# Lọc ra những đứa điểm Toán < 4.0
bao_thu = df[ df['Toan'] < 4.0 ]

print("🏆 DANH SÁCH 'HẢO HÁN' (GPA >= 8.0):")
print(hao_han[['Ten', 'GPA']]) # Chỉ in tên và GPA cho gọn
print("\n💀 DANH SÁCH 'BÁO THỦ' (Tạch Toán):")
print(bao_thu[['Ten', 'Toan']])