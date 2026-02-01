import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("--- 🕵️ TÌM HẰNG SỐ TỐC ĐỘ PHẢN ỨNG ---")

# 1. Đọc dữ liệu & Xử lý (Bài cũ)
df = pd.read_csv('thi_nghiem.csv')
df['Ln_A'] = np.log(df['Nong_do_A'])  # Tính trục y

# 2. HỒI QUY TUYẾN TÍNH (Magic is here ⭐)
# Cú pháp: np.polyfit(Trục_X, Trục_Y, Bậc_của_phương_trình)
# Bậc 1 nghĩa là đường thẳng y = ax + b
he_so = np.polyfit(df['Thoi_gian'], df['Ln_A'], 1)

# Kết quả trả về là một list gồm 2 số: [Hệ_số_góc_a, Hệ_số_tự_do_b]
a = he_so[0]
b = he_so[1]

k = -a  # Vì a = -k nên k = -a

print(f"✅ Phương trình tìm được: y = {a:.4f}x + {b:.4f}")
print(f"🚀 Hằng số tốc độ k = {k:.5f} (1/s)")

# 3. VẼ ĐỂ KIỂM CHỨNG (Dữ liệu thật vs Đường hồi quy)
# Tạo đường thẳng lý thuyết từ a và b vừa tìm được
y_ly_thuyet = a * df['Thoi_gian'] + b

plt.plot(df['Thoi_gian'], df['Ln_A'], 'o', label='Dữ liệu thật')
plt.plot(df['Thoi_gian'], y_ly_thuyet, '-r', label=f'Hồi quy (k={k:.4f})')

plt.title("Đồ thị xác định bậc phản ứng")
plt.xlabel("Thời gian (s)")
plt.ylabel("ln[A]")
plt.legend()
plt.grid(True)
plt.show()

# TÍNH ĐỘ CHÍNH XÁC R-SQUARED (R^2)
# np.corrcoef trả về ma trận tương quan giữa 2 cột
matran_tuong_quan = np.corrcoef(df['Thoi_gian'], df['Ln_A'])

# Lấy giá trị tương quan (r)
r = matran_tuong_quan[0, 1]

# Bình phương lên thành R^2
r_squared = r**2

print("-" * 30)
print(f"🎯 Độ tin cậy (R^2): {r_squared:.4f}")

if r_squared > 0.99:
    print("=> Số liệu quá đẹp! Xuất sắc! 🌟")
elif r_squared > 0.95:
    print("=> Số liệu ổn, chấp nhận được. ✅")
else:
    print("=> Số liệu hơi xấu, coi chừng bị bắt làm lại thí nghiệm! ⚠️")