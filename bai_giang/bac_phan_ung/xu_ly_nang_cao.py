import pandas as pd
import numpy as np  # Gọi thằng đệ chuyên toán học về

print("--- 🧪 XỬ LÝ SỐ LIỆU HÓA LÝ ---")

# 1. Đọc dữ liệu
df = pd.read_csv('thi_nghiem.csv')


df['Ln_A'] = np.log(df['Nong_do_A'])

# Tính 1/A cho cả cột
df['Nghich_dao_A'] = 1 / df['Nong_do_A']

print("Dữ liệu sau khi xử lý:")
print(df)

df.to_csv('ket_qua_da_xu_ly.csv', index=False)

print("\n✅ Đã lưu file 'ket_qua_da_xu_ly.csv'. Bro mở lên xem thử đi!")

df.plot(x='Thoi_gian', y='Ln_A', marker='s', color='green', title="Đồ thị Bậc 1 (Ln A)")
import matplotlib.pyplot as plt
plt.grid(True)
plt.ylabel("ln[A]")
plt.show()