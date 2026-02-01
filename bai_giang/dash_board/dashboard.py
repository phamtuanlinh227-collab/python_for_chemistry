import matplotlib.pyplot as plt
import numpy as np

# 1. TẠO DỮ LIỆU GIẢ LẬP
t = np.linspace(0, 100, 50)       # Thời gian từ 0 đến 100 phút
C = 2.0 * np.exp(-0.05 * t)       # Nồng độ giảm theo hàm mũ (Phản ứng bậc 1)
T = 30 + 50 * (1 - np.exp(-0.05 * t)) # Nhiệt độ tăng dần từ 30 lên 80 độ

# 2. KHỞI TẠO KHUNG TRANH (DASHBOARD)
# nrows=2, ncols=1: Chia làm 2 dòng, 1 cột (Hình trên, hình dưới)
# figsize=(8, 8): Kích thước tổng thể
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8, 8))

# --- VẼ HÌNH TRÊN (AX1 - Nồng độ) ---
ax1.plot(t, C, 'b-o', label='Nồng độ [A]') # b-o: Xanh dương, nét liền, chấm tròn
ax1.set_title('Theo dõi Nồng độ theo thời gian', fontsize=14, color='blue')
ax1.set_ylabel('Nồng độ (M)', fontsize=12)
ax1.grid(True) # Bật lưới
ax1.legend()   # Hiện chú thích

# --- VẼ HÌNH DƯỚI (AX2 - Nhiệt độ) ---
ax2.plot(t, T, 'r--^', label='Nhiệt độ lò') # r--^: Đỏ, nét đứt, tam giác
ax2.set_title('Theo dõi Nhiệt độ phản ứng', fontsize=14, color='red')
ax2.set_xlabel('Thời gian (phút)', fontsize=12)
ax2.set_ylabel('Nhiệt độ (°C)', fontsize=12)
ax2.grid(True)
ax2.legend()

# 3. TINH CHỈNH CUỐI CÙNG
plt.tight_layout() # Lệnh này cực hay: Tự động chỉnh khoảng cách để chữ không bị đè lên nhau
plt.show()