import matplotlib.pyplot as plt

MUC_TIEU = 50.0 # Mục tiêu nhiệt độ lò lên 50 độ C
TOC_DO_NGUOI = 2.0 # Tốc độ nhiệt thất thoát ra ngoài môi trường

class LoPhanUng:
    def __init__ (self, nhiet_do_dau):
        self.T = nhiet_do_dau
        self.tong_sai_so = 0.0
        self.sai_so_cu = 0.0
    def update_1_minutes(self):
        self.T = self.T - TOC_DO_NGUOI
        sai_so = MUC_TIEU - self.T # Sai số của phép đo
        if abs(sai_so) < 5.0:
            self.tong_sai_so += sai_so
        else:
            pass

        # [NEW] TÍNH ĐẠO HÀM (D)
        # Tốc độ thay đổi lỗi = Lỗi nay - Lỗi xưa
        toc_do_loi = sai_so - self.sai_so_cu
        
        # [NEW] Cập nhật bộ nhớ cho vòng sau (Cực quan trọng, quên dòng này là D vô dụng)
        self.sai_so_cu = sai_so
        Kp = 1.1  # Bro vừa chọn
        Ki = 0.5  # Bro vừa chọn
        Kd = 0.1  # [NEW] Thử số này xem
        
        # Công thức PID: P + I + D
        true_p = (sai_so * Kp) + (self.tong_sai_so * Ki) + (toc_do_loi * Kd)
        
        # ... (đoạn Saturation và cập nhật nhiệt độ giữ nguyên) ...
        if true_p > 20.0: true_p = 20.0 
        if true_p < 0: true_p = 0
        self.T = true_p + self.T
        return self.T
  
lo = LoPhanUng(nhiet_do_dau = 10)

time_log = []
temp_log = []

for phut in range(81):
    T1 = lo.update_1_minutes()
    if phut == 40:
        lo.T = lo.T - 15
        T1 = lo.T

    time_log.append(phut)
    temp_log.append(T1)

    if phut % 20 == 0:
        print(f"Tại thời gian {phut} nhiệt độ lò là: {T1:.2f} độ")

plt.figure(figsize=(10, 6))
plt.plot(time_log, temp_log, label="Nhiệt độ Lò (PI Control)", color="green", linewidth=2)
plt.axhline(y=MUC_TIEU, color="red", linestyle="--", label="Mục tiêu (50°C)")

plt.title("MÔ PHỎNG PI CONTROL (ĐÃ SỬA LỖI SAI SỐ)", fontsize=14, fontweight='bold')
plt.xlabel("Thời gian (Phút)")
plt.ylabel("Nhiệt độ (°C)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()




