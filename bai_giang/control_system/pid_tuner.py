import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- 1. CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="PID Tuner Pro", page_icon="🎛️", layout="wide")

st.title("🎛️ Bàn Tuning PID Giả Lập")
st.markdown("Điều chỉnh thông số Kp, Ki, Kd để tìm ra đường cong hoàn hảo!")

# --- 2. THANH ĐIỀU KHIỂN (SIDEBAR) ---

# Mục tiêu nhiệt độ
setpoint = st.sidebar.slider("Nhiệt độ Mục tiêu (Setpoint)", 0, 100, 70)

# Ba anh em siêu nhân P-I-D
Kp = st.sidebar.slider("Kp (Sức mạnh)", 0.0, 5.0, 1.0, step=0.1)
Ki = st.sidebar.slider("Ki (Cộng dồn)", 0.0, 2.0, 0.1, step=0.01)
Kd = st.sidebar.slider("Kd (Giảm xóc)", 0.0, 5.0, 0.5, step=0.1)

# Các thông số vật lý của lò (giả định)
st.sidebar.markdown("---")
st.sidebar.header("🔥 Đặc tính Lò")
toc_do_nguoi = st.sidebar.slider("Tốc độ mất nhiệt môi trường", 0.0, 2.0, 0.5)

# --- 3. BỘ NÃO PID (Class cũ của bro) ---
class PID_Controller:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

    def update(self, current_value, target):
        error = target - current_value
        
        # P term
        P = self.Kp * error
        
        # I term (Anti-windup nhẹ: chỉ tích lũy khi sai số nhỏ)
        if abs(error) < 20: 
            self.integral += error
        I = self.Ki * self.integral

        # D term
        D = self.Kd * (error - self.prev_error)
        self.prev_error = error

        output = P + I + D
        
        # Giới hạn công suất lò (0 - 100%)
        return max(0, min(100, output))

# --- 4. CHẠY MÔ PHỎNG (SIMULATION LOOP) ---
# Tạo dữ liệu giả lập trong 100 phút
time_steps = 100
temps = []
targets = []
power_log = []

# Khởi tạo lò
current_temp = 25.0 # Nhiệt độ phòng
pid = PID_Controller(Kp, Ki, Kd)

for t in range(time_steps):
    # 1. Tính toán công suất cần thiết
    power = pid.update(current_temp, setpoint)
    
    # 2. Tác động vật lý vào lò
    # Nhiệt tăng do lò sưởi (Power * 0.5 là hệ số gia nhiệt)
    # Nhiệt giảm do môi trường (toc_do_nguoi)
    current_temp += (power * 0.5) - toc_do_nguoi
    
    # Lưu lại để vẽ
    temps.append(current_temp)
    targets.append(setpoint)
    power_log.append(power)

# --- 5. VẼ BIỂU ĐỒ (VISUALIZATION) ---
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("📈 Phản hồi Nhiệt độ (Response)")
    fig, ax1 = plt.subplots(figsize=(10, 5))
    
    # Trục Y1: Nhiệt độ
    ax1.plot(temps, label="Nhiệt độ Thực (PV)", color="green", linewidth=2)
    ax1.plot(targets, label="Mục tiêu (SP)", color="red", linestyle="--")
    ax1.set_ylabel("Nhiệt độ (°C)", color="green")
    ax1.set_ylim(0, 120)
    ax1.legend(loc="upper left")
    ax1.grid(True, alpha=0.3)

    # Trục Y2: Công suất lò (để xem lò hoạt động vất vả ko)
    ax2 = ax1.twinx()
    ax2.fill_between(range(time_steps), power_log, color="orange", alpha=0.1, label="Công suất Lò (%)")
    ax2.set_ylabel("Công suất Lò (%)", color="orange")
    ax2.set_ylim(0, 110)
    
    st.pyplot(fig)

with col2:
    st.subheader("📊 Chỉ số KPI")
    # Tính độ vọt lố (Overshoot)
    max_temp = max(temps)
    overshoot = max_temp - setpoint if max_temp > setpoint else 0
    
    st.metric("Nhiệt độ Cuối", f"{temps[-1]:.1f} °C", delta=f"{temps[-1]-setpoint:.1f}")
    st.metric("Độ vọt lố (Overshoot)", f"{overshoot:.1f} °C", 
              delta_color="inverse" if overshoot > 5 else "normal") # Đỏ nếu vọt quá 5 độ
    
    if overshoot > 10:
        st.error("⚠️ CẢNH BÁO: Vọt lố quá cao! Tăng Kd hoặc giảm Ki.")
    elif abs(temps[-1] - setpoint) < 1.0:
        st.success("✅ QUÁ ĐỈNH: Hệ thống ổn định!")


# Code structure supported by AI, customized by Tuan Linh
# Project: Chemistry Automation