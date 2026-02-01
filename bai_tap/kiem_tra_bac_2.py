import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data_bac_2.csv')

df['Y_nghich_dao'] = 1 / df['Nong_do_NO2']

ket_qua =  np.polyfit(df['Thoi_gian'], df['Y_nghich_dao'], 1)

k = ket_qua[0]
b = ket_qua[1]

r_squared = np.corrcoef(df['Thoi_gian'], df['Y_nghich_dao'])[0, 1] ** 2
print("--- KẾT QUẢ PHÂN TÍCH ---")

print(f"Hằng số tốc độ k = {k:.5f} (L/mol.s)")
print(f"Độ tin cậy R^2 = {r_squared:.4f}")

if r_squared > 0.99:
    print("=> Đây chính là phương trình bậc 2")
else:
    print("=> Kiểm tra lại phương trình đi nhé")

y_ly_thuyet = k * df['Thoi_gian'] + b
plt.plot(df['Thoi_gian'], df['Y_nghich_dao'], 'o', label='Dữ liệu thật')
plt.plot(df['Thoi_gian'], y_ly_thuyet, '-', label='Đường hồi quy')
plt.title("Đồ thị bậc 2")
plt.xlabel("Thời gian (s)")
plt.ylabel("1/[NO2]")
plt.grid(True)
plt.legend()
plt.show()