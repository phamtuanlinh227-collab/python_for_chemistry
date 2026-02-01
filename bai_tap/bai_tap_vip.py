import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Tạo dữ liệu giả lập
temp = [100, 110, 120, 130, 140, 150]
hieu_suat = [30, 45, 60, 85, 90, 88]

plt.plot(temp, hieu_suat, 'r-s', label='Hiệu suất theo nhiệt độ')

plt.xlabel('Nhiệt độ (°C)')
plt.ylabel('Hiệu suất (%)')
plt.title('Tối ưu hóa phản ứng')
plt.grid(True)
plt.legend()
plt.show()


# BÀI TẬP 2

time = np.arange(0, 10, 1)
pH = [7, 7.1, 6.8, 7.2, 6.9, 7.0, 7.1, 6.8, 6.5, 6.0]
pressure = [1, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8]
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8, 8))

ax1.plot(time, pH, 'g-o', label='pH theo thời gian')
ax1.set_title('Theo dõi nồng độ theo thời gian', fontsize=14, color='green')
ax1.set_xlabel('Thời gian (phút)', fontsize=12)
ax1.set_ylabel('pH', fontsize=12)
ax1.grid(True)
ax1.legend()

ax2.plot(time, pressure, color='purple', linestyle='-', marker='^', label='Áp suất theo thời gian')
ax2.set_title('Theo dõi áp suất theo thời gian', fontsize=14, color='purple')
ax2.set_xlabel('Thời gian (phút)', fontsize=12)
ax2.set_ylabel('Áp suất (atm)', fontsize=12)
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()

# BÀI TẬP 3
t_data = [0, 20, 40]   # Thời gian
T_data = [100, 60, 30] # Nhiệt độ giảm dần
target = 50            # Cần tìm lúc 50 độ C
a = np.flip(T_data)
b = np.flip(t_data)
time_can_tim = np.interp(target, a, b)
print(f" Dự Báo: Để đạt được nhiệt độ {target} độ C, cần thời gian {time_can_tim:.2f} phút.")

plt.plot(time_can_tim, target,'r^', label='Điểm dự báo')
plt.plot(b, a, 'b-o', label='Dữ liệu thật')
plt.axvline(x=time_can_tim, color='red', linestyle='--')
plt.axhline(y=target, color='red', linestyle='--')
plt.title(f'Cần {time_can_tim:.2f} phút để đạt được {target} độ C')
plt.xlabel('Thời gian (phút)')
plt.ylabel('Nhiệt độ (°C)')
plt.grid(True)
plt.legend()
plt.show()