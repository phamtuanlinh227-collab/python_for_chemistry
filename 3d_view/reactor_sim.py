import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- 1. CẤU HÌNH ---
st.set_page_config(page_title="Chemical Reactor Sim", page_icon="⚗️", layout="wide")
st.title("⚗️ Mô phỏng Lò Phản Ứng Batch")
st.markdown("**Nhiệm vụ:** Điều khiển PID để tối đa hóa sản lượng thuốc, tránh làm cháy thuốc!")

# --- 2. THANH ĐIỀU KHIỂN ---
col1, col2 = st.columns([1, 3])

with col1:
    st.header("🎛️ Control Panel")
    # Mục tiêu cố định là 80 độ cho bài toán này
    setpoint = 80.0 
    st.info(f"Nhiệt độ Yêu cầu: {setpoint} °C")
    
    # Tuner PID
    Kp = st.slider("Kp (Sức mạnh)", 0.0, 5.0, 1.5)
    Ki = st.slider("Ki (Cộng dồn)", 0.0, 1.0, 0.05)
    Kd = st.slider("Kd (Giảm xóc)", 0.0, 5.0, 1.0)
    
    st.markdown("---")
    noise_level = st.slider("Độ nhiễu môi trường", 0.0, 2.0, 0.5)

# --- 3. LOGIC HÓA HỌC & PID ---

class PID_Controller:
    def __init__(self, Kp, Ki, Kd):
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.prev_error = 0
        self.integral = 0
        
    def update(self, current_value, target):
        error = target - current_value
        self.integral += error
        D = self.Kd * (error - self.prev_error)
        self.prev_error = error
        output = (self.Kp * error) + (self.Ki * self.integral) + D
        return max(0, min(100, output))

# --- 4. CHẠY MÔ PHỎNG (ENGINE) ---
time_steps = 150
temps = []      # Lưu nhiệt độ
san_pham = []   # Lưu lượng thuốc tạo ra (Product)
tap_chat = []   # Lưu lượng chất hỏng (Impurity)

# Khởi tạo
current_temp = 25.0
amount_product = 0.0
amount_impurity = 0.0
pid = PID_Controller(Kp, Ki, Kd)

for t in range(time_steps):
    # --- A. VẬT LÝ (LÒ NHIỆT) ---
    sensor_val = current_temp + np.random.normal(0, noise_level)
    power = pid.update(sensor_val, setpoint)
    current_temp += (power * 0.4) - 0.5 # Gia nhiệt & Mất nhiệt
    
    # --- B. HÓA HỌC (PHẢN ỨNG) ---
    # 1. Tốc độ tạo thuốc (Chỉ xảy ra tốt quanh 80 độ)
    # Dùng hàm Gaussian: Đỉnh cao nhất ở 80, lệch ra xa là giảm
    rate_reaction = 0
    if current_temp > 70:
        # Công thức mô phỏng hiệu suất (càng gần 80 càng nhanh)
        rate_reaction = np.exp(-0.1 * (current_temp - 80)**2) 
    
    # 2. Tốc độ phân hủy (Xảy ra nếu quá nhiệt > 85)
    rate_degradation = 0
    if current_temp > 85:
        # Quá nhiệt càng cao hỏng càng nhanh
        rate_degradation = (current_temp - 85) * 0.2 
    
    # Cập nhật kho
    amount_product += rate_reaction - rate_degradation # Tạo ra trừ đi bị hỏng
    amount_impurity += rate_degradation
    
    # Không để âm
    amount_product = max(0, amount_product)
    
    # Lưu data
    temps.append(current_temp)
    san_pham.append(amount_product)
    tap_chat.append(amount_impurity)

# --- 5. HIỂN THỊ KẾT QUẢ (DASHBOARD) ---
with col2:
    # Biểu đồ 1: Nhiệt độ (Quá trình)
    st.subheader("1. Quá trình Gia nhiệt")
    fig1, ax1 = plt.subplots(figsize=(10, 3))
    ax1.plot(temps, label="Nhiệt độ Lò", color="blue")
    ax1.axhline(y=80, color="green", linestyle="--", label="Target (80°C)")
    ax1.axhline(y=85, color="red", linestyle=":", label="Ngưỡng Nguy hiểm (85°C)")
    ax1.fill_between(range(time_steps), 85, 120, color="red", alpha=0.1) # Vùng chết
    ax1.legend()
    st.pyplot(fig1)
    
    # Biểu đồ 2: Kết quả Hóa học (Thành phẩm)
    st.subheader("2. Sản lượng Hóa chất")
    fig2, ax2 = plt.subplots(figsize=(10, 3))
    ax2.plot(san_pham, label="Thuốc Tốt (Paracetamol)", color="green", linewidth=2)
    ax2.plot(tap_chat, label="Tạp chất (Do quá nhiệt)", color="red", linewidth=2)
    ax2.set_ylabel("Khối lượng (kg)")
    ax2.legend()
    st.pyplot(fig2)

    # --- KPI CUỐI CÙNG ---
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Tổng Thuốc Tốt", f"{san_pham[-1]:.1f} kg")
    kpi2.metric("Tổng Tạp Chất", f"{tap_chat[-1]:.1f} kg", delta_color="inverse")
    
    hieu_suat = (san_pham[-1] / (san_pham[-1] + tap_chat[-1] + 0.1)) * 100
    kpi3.metric("Độ Tinh Khiết", f"{hieu_suat:.1f}%")
    
    if hieu_suat > 90 and san_pham[-1] > 20:
        st.success("🏆 MẺ THUỐC ĐẠT CHUẨN GMP! XUẤT XƯỞNG!")
    elif tap_chat[-1] > 5:
        st.error("☠️ CẢNH BÁO: Thuốc nhiễm độc do quá nhiệt!")
    else:
        st.warning("⚠️ Hiệu suất thấp. Cần tối ưu PID!")