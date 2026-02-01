import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Thoi_gian': [0, 50, 100, 150, 200, 250, 300],
    'Nong_do_NO2': [0.0100, 0.0079, 0.0065, 0.0055, 0.0048, 0.0041, 0.0038]
}
df = pd.DataFrame(data)

x = df['Thoi_gian']
y_thuc_te = 1 / df['Nong_do_NO2']

he_so = np.polyfit(x, y_thuc_te, 1)
k = he_so[0]
b = he_so[1]

r_squared = np.corrcoef(x, y_thuc_te)[0, 1] ** 2
y_ly_thuyet = k * x + b

plt.figure(figsize=(10, 6))

plt.plot(x, y_thuc_te, 'ks', label='Dữ liệu thực nghiệm', markersize=8)
plt.plot(x, y_ly_thuyet, 'r-', label='Dữ liệu lý thuyết', linewidth=2)
plt.title('Đồ thị Động học Phân tử bậc 2', fontsize=16, color='darkblue')
plt.xlabel('Thời gian (giây)', fontsize=14)
plt.ylabel('Nghịch đảo nồng độ $1/NO2$ ($M^-1$)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12, loc='best')
# Cách sửa "nhà khoa học": Dùng tọa độ tương đối (0.0 đến 1.0)
# transform=plt.gca().transAxes nghĩa là dùng hệ trục của khung hình
# (0.6, 0.2) nghĩa là: Cách lề trái 60%, Cách lề dưới 20% -> Góc dưới phải
plt.text(0.6, 0.2, f'$R^2$ = {r_squared:.4f}', 
         fontsize=12, 
         bbox=dict(facecolor='yellow', alpha=0.3),
         transform=plt.gca().transAxes)
plt.show()
