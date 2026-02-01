import matplotlib.pyplot as plt

# --- CẤU HÌNH HỆ THỐNG ---
MUC_TIEU = 50.0       # Độ C (Setpoint)
SUC_MANH_LO_SUOI = 2.0 # Độ/phút (Heater Gain)
TOC_DO_NGUOI = 0.5    # Độ/phút (Heat Loss)

class LoPhanUng:
    def __init__(self, nhiet_do_dau):
        self.T = nhiet_do_dau  # Nhiệt độ hiện tại
    
    def cap_nhat_1_phut(self):
        # 1. Vật lý: Vẫn bị nguội đi
        self.T = self.T - TOC_DO_NGUOI
        
        # 2. Bộ điều khiển PRO (P-Control)
        sai_so = MUC_TIEU - self.T  # Còn thiếu bao nhiêu độ nữa?
        
        if sai_so > 0:
            # Còn thiếu nhiệt -> Bơm nhiệt
            # CÔNG THỨC P: Thiếu nhiều bơm nhiều, thiếu ít bơm ít
            # Kp = 0.5 là "Hệ số nhạy" (Gain). 
            # Ví dụ: Thiếu 10 độ -> Bơm 10 * 0.5 = 5 (Max công suất)
            #        Thiếu 2 độ  -> Bơm 2 * 0.5 = 1 (Nhẹ nhàng)
            cong_suat_thuc = sai_so * 0.5 
            
            # Giới hạn công suất (Máy sưởi không thể mạnh vô cực được)
            if cong_suat_thuc > 5.0: cong_suat_thuc = 5.0 
            
            self.T = self.T + cong_suat_thuc
        else:
            # Nóng quá rồi -> Tắt hẳn (Hoặc có thể làm mát)
            pass 
            
        return self.T, "Variable"


# --- MÔ PHỎNG ---
lo = LoPhanUng(nhiet_do_dau=25.0)

time_log = []
temp_log = []

for phut in range(60): # Chạy trong 60 phút
    T_hien_tai, trang_thai = lo.cap_nhat_1_phut()
    
    time_log.append(phut)
    temp_log.append(T_hien_tai)

# --- VẼ BIỂU ĐỒ ---
plt.figure(figsize=(10, 6))
plt.plot(time_log, temp_log, label="Nhiệt độ Lò", color="#1f77b4", linewidth=2)
plt.axhline(y=MUC_TIEU, color="red", linestyle="--", label=f"Mục tiêu ({MUC_TIEU}°C)")

plt.title("MÔ PHỎNG ĐIỀU KHIỂN ON/OFF (RĂNG CƯA)", fontsize=14, fontweight='bold')
plt.xlabel("Thời gian (Phút)")
plt.ylabel("Nhiệt độ (°C)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

# Code structure supported by AI, customized by Tuan Linh
# Project: Chemistry Automation