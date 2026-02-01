import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-darkgrid")

class VatLieu:
    def __init__(self, ten, nhiet_do, he_so_tan_nhiet):
        self.ten = ten
        self.T = nhiet_do
        self.k = he_so_tan_nhiet
        self.T_ht = 100
        self.T_mt = 25
    
    def lam_nguoi(self):
        T_giam = self.k * ( self.T_ht - self.T_mt)
        self.T_ht = self.T_ht - T_giam
        return self.T_ht
    

vat_lieu = []
vat_lieu.append(VatLieu("wood", 100, 0.05))
vat_lieu.append(VatLieu("Al", 100, 0.1))
vat_lieu.append(VatLieu("Cu", 100, 0.3))

history = {
    "wood": [],
    "Al": [],
    "Cu": []
}
thoi_gian = []
for v in vat_lieu:
    history[v.ten].append(v.T) # Lưu nhiệt độ phút 0 (100 độ)
thoi_gian.append(0)
for phut in range(61):
    thoi_gian.append(phut)
    for giam in vat_lieu:
        T_hien_tai = giam.lam_nguoi()
        history[giam.ten].append(T_hien_tai)

plt.figure(figsize=(10, 8))

plt.axhline(y=25, color="blue", linestyle="--")

plt.fill_between(thoi_gian, history["wood"], color="blue", alpha=0.2)
plt.plot(thoi_gian, history["wood"], color="blue", linewidth=2, label="Gỗ (k=0.05) - Nguội lâu nhất")

plt.fill_between(thoi_gian, history["Al"], color="orange", alpha=0.3)
plt.plot(thoi_gian, history["Al"], color="orange", linewidth=3, label="Nhôm (k=0.1)")

plt.plot(thoi_gian, history["Cu"], color="green", alpha=0.2, linestyle="--", label="Đồng (k=0.3) - Nguội nhanh nhất")

plt.title("ĐỒ THỊ SỰ GIẢM NHIỆT ĐỘ CỦA VẬT LIỆU", fontsize=18, color="navy")
plt.ylabel("Hệ số tản nhiệt")
plt.xlabel("thời gian (phút)")
plt.grid(True)
plt.legend(fontsize=18)
plt.show()
