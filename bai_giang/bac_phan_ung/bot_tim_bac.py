import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. DỮ LIỆU ĐẦU VÀO (Giả sử số liệu thực nghiệm)
# Đây là dữ liệu của phản ứng Bậc 1 (mình biết trước để test)
t = np.array([0, 10, 20, 30, 40, 50, 60])
C = np.array([1.00, 0.60, 0.37, 0.22, 0.14, 0.08, 0.05])

# 2. CHUẨN BỊ KHUNG TRANH (1 hàng, 3 cột - giống ảnh Facebook)
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

# Tạo danh sách để lưu kết quả thi đấu của 3 bậc
ket_qua = [] 

# 3. VÒNG LẶP FOR (Cỗ máy xử lý)
# Chạy lần lượt qua 3 trường hợp: 0, 1, 2
# zip([0, 1, 2], axes) nghĩa là:
# - Lần 1: order=0, vẽ vào cái khung thứ nhất (ax)
# - Lần 2: order=1, vẽ vào cái khung thứ hai
# - Lần 3: order=2, vẽ vào cái khung thứ ba
for order, ax in zip([0, 1, 2], axes):
    
    # --- A. BIẾN ĐỔI DỮ LIỆU (TRANSFORM) ---
    if order == 0:
        y = C             # Bậc 0: Giữ nguyên [A]
        ylabel = '[A] (M)'
    elif order == 1:
        y = np.log(C)     # Bậc 1: Lấy ln[A]
        ylabel = 'ln[A]'
    else:
        y = 1 / C         # Bậc 2: Lấy 1/[A]
        ylabel = '1/[A] ($M^{-1}$)'

    # --- B. HỒI QUY TUYẾN TÍNH (FITTING) ---
    he_so = np.polyfit(t, y, 1) # Luôn tìm đường thẳng y = ax + b
    k_slope = he_so[0]
    r_squared = np.corrcoef(t, y)[0, 1] ** 2
    
    # Lưu kết quả lại để tí so sánh
    ket_qua.append( (order, r_squared) )

    # --- C. VẼ HÌNH (VISUALIZATION) ---
    y_ly_thuyet = he_so[0] * t + he_so[1]
    
    ax.scatter(t, y, color='black', label='Thực nghiệm') # Chấm điểm
    ax.plot(t, y_ly_thuyet, 'r--', label='Hồi quy')      # Đường thẳng
    
    # Trang trí
    ax.set_title(f'Giả định Bậc {order}\n$R^2 = {r_squared:.4f}$', 
                 fontsize=12, color='darkblue')
    ax.set_xlabel('Thời gian (s)')
    ax.set_ylabel(ylabel)
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.6)

# 4. MÁY TÍNH TỰ PHÁN QUYẾT (BOT DECISION)
# Tìm xem R^2 nào lớn nhất (gần 1 nhất)
best_order = max(ket_qua, key=lambda item: item[1]) 

print("-" * 30)
print(f"🤖 BOT BÁO CÁO: Phản ứng này là BẬC {best_order[0]}!")
print(f"Độ chính xác (R^2) = {best_order[1]:.4f}")
print("-" * 30)

plt.tight_layout()
plt.show()