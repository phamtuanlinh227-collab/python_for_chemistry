import pandas as pd
import matplotlib.pyplot as plt

print("--- 🎨 VẼ ĐỒ THỊ VỚI PANDAS ---")

# 1. Đọc dữ liệu
df = pd.read_csv('thi_nghiem.csv')

# 2. VẼ ĐỒ THỊ (Magic is here!)
# x: Chọn cột làm trục hoành
# y: Chọn những cột làm trục tung (đưa vào một list)
# marker='o': Đánh dấu điểm tròn
df.plot(x='Thoi_gian', y=['Nong_do_A', 'Nong_do_B'], marker='o')

# 3. Trang trí thêm (Vẫn dùng lệnh của matplotlib được)
plt.title("Biến thiên nồng độ các chất")
plt.ylabel("Nồng độ (M)")
plt.grid(True)

# 4. Hiện hình
plt.show()