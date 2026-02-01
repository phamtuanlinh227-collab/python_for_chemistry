import matplotlib.pyplot as plt
# --- THÊM DÒNG NÀY ĐỂ ĐỔI GIAO DIỆN ---
# Các style khác có thể thử: 'ggplot', 'fivethirtyeight', 'bmh'
plt.style.use('seaborn-v0_8-darkgrid')
# -------------------------------------

class LoPhanUng:
    # ... (Code Class y hệt cũ) ...
    def __init__(self, ten, nong_do_dau, he_so_k):
        self.ten = ten
        self.C = nong_do_dau
        self.k = he_so_k
    
    def phan_ung_1_phut(self):
        mat_di = self.C * self.k
        self.C = self.C - mat_di
        return self.C

# ... (Code khởi tạo y hệt cũ) ...
lo_pu = [LoPhanUng("lo_A", 100, 0.1), LoPhanUng("lo_B", 300, 0.2), LoPhanUng("lo_C", 500, 0.3)]
history = {"lo_A": [], "lo_B": [], "lo_C": []}
thoi_gian = []

# ... (Code chạy mô phỏng y hệt cũ) ...
for phut in range(51):
    thoi_gian.append(phut)
    for lo in lo_pu:
        history[lo.ten].append(lo.phan_ung_1_phut())

# --- VẼ VỜI (Có chỉnh sửa tí cho đẹp) ---
plt.figure(figsize=(12, 7)) # Khung to hơn

# Vẽ và tô màu vùng bên dưới (fill_between) nhìn cho nó nguy hiểm
plt.fill_between(thoi_gian, history["lo_C"], color="purple", alpha=0.2)
plt.plot(thoi_gian, history["lo_C"], label="Lò C (C=500, k=0.3) - Nhanh nhất", color="purple", linewidth=3)

plt.fill_between(thoi_gian, history["lo_B"], color="blue", alpha=0.1)
plt.plot(thoi_gian, history["lo_B"], label="Lò B (C=300, k=0.2)", color="blue", linewidth=2)

plt.plot(thoi_gian, history["lo_A"], label="Lò A (C=100, k=0.1) - Chậm nhất", color="green", linewidth=2, linestyle="--")


plt.title("DASHBOARD ĐỘNG HỌC PHẢN ỨNG (STYLED)", fontsize=16, fontweight='bold', color='navy')
plt.xlabel("Thời gian (Phút)", fontsize=12)
plt.ylabel("Nồng độ còn lại (M)", fontsize=12)
plt.legend(fontsize=11) # Hộp chú thích to rõ

plt.show()