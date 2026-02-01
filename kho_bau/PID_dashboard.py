# --- MẪU CODE PID CHUẨN ---
# Dùng cho: Lò nhiệt, Bồn nước, Pha hóa chất...
# Cách dùng: 
# 1. Chỉnh MUC_TIEU ở dòng 5
# 2. Chỉnh Kp, Ki, Kd ở hàm update()
# 3. Kp to thì nhanh, Ki to thì hết sai số, Kd to thì giảm rung lắc.
import matplotlib.pyplot as plt

# --- 1. SETUP HỆ THỐNG ---
TOC_DO_NGUOI = 1.0  # Lò này mất nhiệt vừa phải
# Lưu ý: MUC_TIEU không còn là hằng số cố định nữa!

class LoPhanUng:
    def __init__ (self, nhiet_do_dau):
        self.T = nhiet_do_dau
        self.tong_sai_so = 0.0 
        self.sai_so_cu = 0.0 # Dùng cho D

    def update(self, muc_tieu_hien_tai):
        # 1. Mất nhiệt
        self.T = self.T - TOC_DO_NGUOI
        
        # 2. Tính toán PID
        sai_so = muc_tieu_hien_tai - self.T
        
        # Anti-windup
        if abs(sai_so) < 10.0: # Mở rộng vùng hoạt động cho I chút
            self.tong_sai_so += sai_so
            
        toc_do_loi = sai_so - self.sai_so_cu
        self.sai_so_cu = sai_so

        # Thông số Tuning (Cân bằng)
        Kp = 0.8
        Ki = 0.1
        Kd = 0.5
        
        cong_suat = (sai_so * Kp) + (self.tong_sai_so * Ki) + (toc_do_loi * Kd)
        
        # Giới hạn công suất (Lò mạnh Max 20)
        if cong_suat > 20.0: cong_suat = 20.0 
        if cong_suat < 0.0: cong_suat = 0.0
        
        self.T = self.T + cong_suat
        return self.T

# --- 2. MÔ PHỎNG QUY TRÌNH (BATCH) ---
lo = LoPhanUng(nhiet_do_dau=25.0)

time_log = []
temp_log = []
target_log = [] # Lưu lại mục tiêu để vẽ đường đỏ gãy khúc

for phut in range(120): # Chạy 2 tiếng (120 phút)
    
    # === [BRAIN] BỘ NÃO ĐIỀU KHIỂN QUY TRÌNH ===
    if phut < 30:
        # Giai đoạn 1: Ủ ấm (0 - 30 phút)
        target = 40.0
    elif phut < 70:
        # Giai đoạn 2: Nấu chín (30 - 70 phút)
        target = 70.0
    elif phut < 90:
        # Giai đoạn 3: Giữ nhiệt nhẹ (70 - 90 phút)
        target = 50.0
    else:
        # Giai đoạn 4: Tắt lò/Làm nguội (90 - 120 phút)
        target = 30.0
    # ===========================================

    # Truyền target động vào lò
    T_hien_tai = lo.update(target)
    
    time_log.append(phut)
    temp_log.append(T_hien_tai)
    target_log.append(target)

# --- 3. VẼ ---
plt.figure(figsize=(12, 6))
plt.plot(time_log, temp_log, label="Nhiệt độ Lò (Thực tế)", color="green", linewidth=2)
# Vẽ đường mục tiêu màu đỏ (nó sẽ là bậc thang)
plt.plot(time_log, target_log, label="Quy trình cài đặt (Target)", color="red", linestyle="--")

plt.title("MÔ PHỎNG QUY TRÌNH NHIỆT (PROFILE CONTROL)", fontsize=14, fontweight='bold')
plt.xlabel("Thời gian (Phút)")
plt.ylabel("Nhiệt độ (°C)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()