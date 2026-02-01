import pandas as pd
import matplotlib.pyplot as plt

print("⏳ Đang đọc file Excel... Chờ xíu...")

# 1. ĐỌC FILE (Phần quan trọng nhất)
# Biến 'df' là viết tắt của DataFrame (Bảng dữ liệu)
df = pd.read_excel('data_lab.xlsx')

# Kiểm tra xem nó đọc đúng chưa bằng cách in 5 dòng đầu
print("Dữ liệu đã đọc được:")
print(df.head()) 

# 2. VẼ ĐỒ THỊ (Dùng dữ liệu từ df)
# Thay vì gõ list [1, 2...], ta gọi tên cột: df['Tên_Cột']
plt.plot(df['NhietDo'], df['KNO3'], 'o-r', label='KNO3')
plt.plot(df['NhietDo'], df['NaCl'], 's--b', label='NaCl')

# 3. TRANG TRÍ (Y hệt bài trước)
plt.title("Đồ thị độ tan từ dữ liệu Excel")
plt.xlabel("Nhiệt độ (C)")
plt.ylabel("Độ tan (g/100g nước)")
plt.legend()
plt.grid(True)

# 4. SHOW
plt.show()
