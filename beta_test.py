import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

t = np.array([0, 1, 2, 3, 4, 5])
C = np.array([0, 0.5, 0.8, 0.9, 0.95, 0.98])

he_so = np.polyfit(t, C, 1)
a = he_so[0]
b = he_so[1]    

y_ly_thuyet = a * t + b

plt.plot(t, C, 'o', label='Dữ liệu thật')
plt.plot(t, y_ly_thuyet, '-r', label=f'Hồi quy (a={a:.4f})')
plt.title("Đồ thị xác định bậc phản ứng")
plt.xlabel("Thời gian (s)")
plt.ylabel("C")
plt.legend()
plt.grid(True)
plt.show()

ma_tran_tuong_quan = np.corrcoef(t, C)
r = ma_tran_tuong_quan[0, 1]
r_squared = r**2
print(f"R^2: {r_squared:.4f}")


