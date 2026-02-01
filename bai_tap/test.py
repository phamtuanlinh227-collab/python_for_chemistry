import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-darkgrid")

class VatLieu:
    def __init__(self, ten, nhiet_do, he_so_tan_nhiet):
        self.ten = ten
        self.T = nhiet_do    # Nhiệt độ hiện tại (Dùng biến này xuyên suốt)
        self.k = he_so_tan_nhiet
        self.T_mt = 25       # Nhiệt độ môi trường
    
    def lam_nguoi(self):
        # 1. Tính lượng nhiệt mất đi dựa trên chênh lệch hiện tại
        # Công thức: k * (T_vật - T_môi_trường)
        T_giam = self.k * (self.T - self.T_mt) 
        
        # 2. CẬP NHẬT NHIỆT ĐỘ MỚI (Trừ đi phần đã mất)
        self.T = self.T - T_giam  # <--- QUAN TRỌNG NHẤT: Phải lưu lại vào self.T
        
        # 3. Trả về nhiệt độ hiện tại (chứ không phải lượng giảm)
        return self.T 

# --- KHỞI TẠO ---
vat_lieu = []
vat_lieu.append(VatLieu("Wood", 100, 0.05)) # Gỗ
vat_lieu.append(VatLieu("Al", 100, 0.1))    # Nhôm
vat_lieu.append(VatLieu("Cu", 100, 0.3))    # Đồng

history = {
    "Wood": [],
    "Al": [],
    "Cu": []
}
thoi_gian = []

# --- MÔ PHỎNG ---
# Lưu ý: Nên lưu trạng thái ban đầu (phút 0) trước khi chạy vòng lặp
for v in vat_lieu:
    history[v.ten].append(v.T) # Lưu nhiệt độ phút 0 (100 độ)
thoi_gian.append(0)

# Chạy từ phút 1 đến 60
for phut in range(1, 61):
    thoi_gian.append(phut)
    for v in vat_lieu:
        T_moi = v.lam_nguoi() # Gọi hàm làm nguội
        history[v.ten].append(T_moi)

# --- VẼ ĐỒ THỊ ---
plt.figure(figsize=(10, 8))

# Đường tham chiếu nhiệt độ phòng
plt.axhline(y=25, color="red", linestyle="--", label="Nhiệt độ phòng (25°C)")

# Vẽ các đường
plt.plot(thoi_gian, history["Wood"], color="brown", linewidth=2, label="Gỗ (k=0.05) - Giữ nhiệt tốt")
plt.fill_between(thoi_gian, history["Wood"], 25, color="brown", alpha=0.1) # Tô màu đệm xuống mốc 25

plt.plot(thoi_gian, history["Al"], color="orange", linewidth=2, label="Nhôm (k=0.1)")

plt.plot(thoi_gian, history["Cu"], color="green", linewidth=2, linestyle="-.", label="Đồng (k=0.3) - Tản nhiệt nhanh")

# Sửa lại nhãn trục cho đúng logic
plt.title("MÔ PHỎNG QUÁ TRÌNH LÀM NGUỘI (Newton's Law of Cooling)", fontsize=16, color="navy")
plt.xlabel("Thời gian (Phút)", fontsize=12) # <--- SỬA LẠI
plt.ylabel("Nhiệt độ (°C)", fontsize=12)    # <--- SỬA LẠI

plt.grid(True)
plt.legend(fontsize=12)
plt.show()