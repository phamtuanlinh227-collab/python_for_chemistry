import matplotlib.pyplot as plt

# --- CẤU HÌNH HỆ THỐNG ---
MUC_TIEU = 50.0       # Độ C (Setpoint)
TOC_DO_NGUOI = 0.5    # Độ/phút (Heat Loss - Lỗ thủng của xô nước)

class LoPhanUng:
    def __init__(self, nhiet_do_dau):
        self.T = nhiet_do_dau
        # [NEW] Biến này để nhớ quá khứ (Thành phần I)
        self.tong_sai_so = 0.0 

    def cap_nhat_1_phut(self):
        # 1. Vật lý
        self.T = self.T - TOC_DO_NGUOI
        
        # 2. Sai số
        sai_so = MUC_TIEU - self.T
        
        # --- [FIX] ANTI-WINDUP (CHỐNG BÃO HÒA) ---
        # Chỉ cho phép tích phân hoạt động trong vùng kiểm soát
        # Nếu sai số quá lớn (lò đang quá lạnh), đừng cộng dồn kẻo bị "Ngáo"
        if abs(sai_so) < 5.0:  # Chỉ cộng khi sai số nhỏ hơn 5 độ (sắp đến đích)
            self.tong_sai_so += sai_so 
        else:
            # Nếu đang xa đích quá, reset hoặc giữ nguyên, đừng cộng thêm
            pass 
            
        # 3. Tính toán PI
        Kp = 0.5
        Ki = 0.1
        cong_suat_thuc = (sai_so * Kp) + (self.tong_sai_so * Ki)
        
        # 4. Giới hạn (Saturation)
        if cong_suat_thuc > 5.0: cong_suat_thuc = 5.0
        if cong_suat_thuc < 0.0: cong_suat_thuc = 0.0
        
        self.T = self.T + cong_suat_thuc
        return self.T

# --- MÔ PHỎNG ---
lo = LoPhanUng(nhiet_do_dau=25.0) # Bắt đầu từ 25 độ

time_log = []
temp_log = []

# Chạy thử 80 phút để thấy rõ đoạn sau nó ổn định thế nào
for phut in range(81): 
    T_hien_tai = lo.cap_nhat_1_phut()
    time_log.append(phut)
    temp_log.append(T_hien_tai)

    # In ra vài mốc để check xem nó có lên đúng 50.0 không
    if phut % 20 == 0:
        print(f"Phút {phut}: Nhiệt độ = {T_hien_tai:.2f} độ")

# --- VẼ BIỂU ĐỒ ---
plt.figure(figsize=(10, 6))
plt.plot(time_log, temp_log, label="Nhiệt độ Lò (PI Control)", color="green", linewidth=2)
plt.axhline(y=MUC_TIEU, color="red", linestyle="--", label="Mục tiêu (50°C)")

plt.title("MÔ PHỎNG PI CONTROL (ĐÃ SỬA LỖI SAI SỐ)", fontsize=14, fontweight='bold')
plt.xlabel("Thời gian (Phút)")
plt.ylabel("Nhiệt độ (°C)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Code structure supported by AI, customized by Tuan Linh
# Project: Chemistry Automation