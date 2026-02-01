import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu của thằng C (Vô địch)
t = [0, 10, 20, 30, 40]
data_C = [0, 8, 25, 50, 90]

# --- BÀI TOÁN: TÌM THỜI GIAN KHI NỒNG ĐỘ = 60 ---
muc_tieu = 60

# Hàm np.interp (Interpolate - Nội suy)
# Cú pháp: np.interp(giá_trị_cần_tìm, trục_biết_trước, trục_cần_tìm)
# Ở đây mình biết Nồng độ (data_C), muốn tìm Thời gian (t) -> Nên phải đảo ngược vị trí
thoi_gian_du_bao = np.interp(muc_tieu, data_C, t)

print(f"🔮 TIÊN TRI: Để đạt nồng độ {muc_tieu}, cần chạy lò trong {thoi_gian_du_bao:.2f} phút!")

# --- VẼ HÌNH MINH HỌA CHO SẾP TIN ---
plt.plot(t, data_C, 'b-o', label='Dữ liệu thật')
plt.plot(thoi_gian_du_bao, muc_tieu, 'r*', markersize=15, label='Điểm dự báo')

# Vẽ đường gióng đứt đoạn cho chuyên nghiệp
plt.axvline(x=thoi_gian_du_bao, color='red', linestyle='--') # Đường dọc
plt.axhline(y=muc_tieu, color='red', linestyle='--')         # Đường ngang

plt.title(f"Dự báo: Cần {thoi_gian_du_bao:.2f} phút để đạt {muc_tieu} M")
plt.xlabel("Thời gian (phút)")
plt.ylabel("Nồng độ")
plt.legend()
plt.grid(True)
plt.show()