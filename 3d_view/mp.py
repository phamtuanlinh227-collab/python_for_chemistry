import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors

# --- 1. SETUP HỆ THỐNG & GIAO DIỆN ---
st.set_page_config(page_title="Smart Pharma Reactor", page_icon="💊", layout="wide")

st.title("🏭 SMART PHARMA REACTOR v1.0")
st.markdown("""
**Hệ thống tích hợp:** Hóa Tin (RDKit) + Điều khiển Tự động (PID) + Mô phỏng Vật lý.
*Nhiệm vụ: Chọn thuốc -> Kiểm tra tiêu chuẩn -> Nấu mẻ thuốc hoàn hảo.*
""")

# --- 2. DATABASE THUỐC (RDKit Module) ---
# Từ điển chứa công thức SMILES
duoc_dien = {
    "Paracetamol": "CC(=O)Nc1ccc(O)cc1",
    "Aspirin": "CC(=O)Oc1ccccc1C(=O)O",
    "Ibuprofen": "CC(C)Cc1ccc(cc1)C(C)C(=O)O",
    "Cafein (Test)": "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"
}

# Hàm kiểm tra chất lượng thuốc (Lipinski Rule)
def check_quality(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if not mol: return None, "Lỗi công thức"
    
    # Tính toán tính chất
    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    
    # Luật Lipinski (MW < 500, LogP < 5)
    status = "✅ Đạt chuẩn Drug-like"
    if mw > 500 or logp > 5:
        status = "⚠️ Cảnh báo: Khó hấp thu"
        
    return mol, mw, logp, status

# --- 3. BỘ NÃO ĐIỀU KHIỂN (PID Module) ---
class SmartPID:
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.prev_error = 0
        self.integral = 0
    
    def compute(self, current_val):
        error = self.setpoint - current_val
        
        # P-term
        P = self.Kp * error
        
        # I-term (Có Anti-windup: Chỉ cộng khi sai số < 10 độ)
        if abs(error) < 10:
            self.integral += error
        I = self.Ki * self.integral
        
        # D-term
        D = self.Kd * (error - self.prev_error)
        self.prev_error = error
        
        # Tổng hợp
        output = P + I + D
        
        # Giới hạn công suất lò (0% - 100%)
        return max(0, min(100, output))

# --- 4. KHU VỰC ĐIỀU KHIỂN (SIDEBAR) ---
with st.sidebar:
    st.header("1. Cấu hình Nguyên Liệu 🧪")
    selected_drug = st.selectbox("Chọn loại thuốc cần nấu:", list(duoc_dien.keys()))
    
    # Xử lý RDKit ngay khi chọn thuốc
    smiles = duoc_dien[selected_drug]
    mol, mw, logp, status = check_quality(smiles)
    
    # Hiển thị thông tin Hóa học ngay sidebar
    st.info(f"**{selected_drug}**\n\nMW: {mw:.1f} | LogP: {logp:.1f}\n\n{status}")
    
    st.markdown("---")
    st.header("2. Cấu hình Lò Phản Ứng 🔥")
    target_temp = st.slider("Nhiệt độ Phản ứng (°C)", 50, 150, 80)
    
    # PID Tuning
    st.caption("Thông số PID")
    Kp = st.number_input("Kp", 0.0, 10.0, 2.0, step=0.1)
    Ki = st.number_input("Ki", 0.0, 5.0, 0.1, step=0.01)
    Kd = st.number_input("Kd", 0.0, 10.0, 1.0, step=0.1)
    
    st.markdown("---")
    st.header("3. Thử thách Hệ thống 🌪️")
    noise = st.slider("Độ nhiễu Cảm biến", 0.0, 5.0, 0.5)
    soc_nhiet = st.checkbox("Sự cố: Mất điện làm mát (Phút 60)")

# --- 5. MÔ PHỎNG QUÁ TRÌNH (SIMULATION ENGINE) ---
# Nút bấm để bắt đầu chạy mô phỏng
if st.button("🚀 KÍCH HOẠT QUY TRÌNH SẢN XUẤT"):
    
    # Khởi tạo dữ liệu
    time_steps = 120 # 120 phút
    temps = []
    setpoints = []
    powers = []
    reaction_progress = [] # % Phản ứng hoàn thành
    
    # Trạng thái ban đầu
    current_temp = 25.0 # Nhiệt độ phòng
    current_progress = 0.0
    pid = SmartPID(Kp, Ki, Kd, target_temp)
    
    # VÒNG LẶP MÔ PHỎNG (THE CORE LOOP)
    progress_bar = st.progress(0)
    
    for t in range(time_steps):
        # 1. Tạo nhiễu cảm biến
        sensor_val = current_temp + np.random.normal(0, noise)
        
        # 2. Tính toán PID
        power = pid.compute(sensor_val)
        
        # 3. Sự cố vật lý (Disturbance)
        cooling_factor = 0.5 # Tốc độ nguội tự nhiên
        if soc_nhiet and t > 60 and t < 80:
             cooling_factor = -1.0 # Lò tự nóng lên do phản ứng tỏa nhiệt mất kiểm soát!
        
        # 4. Cập nhật nhiệt độ lò (Vật lý)
        # Temp mới = Temp cũ + (Nhiệt từ lò sưởi - Nhiệt mất đi)
        current_temp += (power * 0.3) - cooling_factor
        
        # 5. Cập nhật Hóa học (Reaction Kinetics)
        # Phản ứng chỉ xảy ra tốt nếu Temp nằm trong vùng Target +/- 5 độ
        rate = 0
        if abs(current_temp - target_temp) < 5:
            rate = 1.0 # Tốc độ chuẩn
        elif abs(current_temp - target_temp) < 10:
            rate = 0.2 # Quá lạnh hoặc quá nóng thì phản ứng chậm
        else:
            rate = 0 # Không phản ứng
            
        current_progress += rate
        if current_progress > 100: current_progress = 100
        
        # Lưu dữ liệu
        temps.append(current_temp)
        setpoints.append(target_temp)
        powers.append(power)
        reaction_progress.append(current_progress)
        
        # Update thanh tiến trình (cho cảm giác real-time)
        if t % 10 == 0:
            progress_bar.progress(int(t/time_steps * 100))

    progress_bar.progress(100)

    # --- 6. HIỂN THỊ KẾT QUẢ (VISUALIZATION) ---
    
    # Chia bố cục 2 cột: Biểu đồ & Kết luận
    c1, c2 = st.columns([3, 1])
    
    with c1:
        st.subheader("📈 Biểu đồ Vận hành")
        fig, ax1 = plt.subplots(figsize=(10, 6))
        
        # Trục 1: Nhiệt độ
        ax1.plot(temps, 'g-', label="Nhiệt độ Lò (PV)", linewidth=2)
        ax1.plot(setpoints, 'r--', label="Mục tiêu (SP)")
        ax1.set_ylabel("Nhiệt độ (°C)", color='green')
        ax1.set_ylim(0, 160)
        ax1.legend(loc='upper left')
        ax1.grid(True, alpha=0.3)
        
        # Trục 2: Công suất (Twin Axis - Kỹ thuật nâng cao)
        ax2 = ax1.twinx()
        ax2.fill_between(range(time_steps), powers, color='orange', alpha=0.2, label="Công suất Lò (%)")
        ax2.set_ylabel("Công suất Heater (%)", color='orange')
        ax2.set_ylim(0, 110)
        
        st.pyplot(fig)
        
    with c2:
        st.subheader("📋 Báo cáo Mẻ")
        
        # Vẽ hình phân tử thuốc dùng RDKit
        if mol:
            img = Chem.Draw.MolToImage(mol)
            st.image(img, caption=f"Cấu trúc {selected_drug}")
            
        # KPI
        final_yield = reaction_progress[-1]
        st.metric("Hiệu suất Phản ứng", f"{final_yield:.1f}%")
        
        # Logic đánh giá cuối cùng
        overshoot = max(temps) - target_temp
        if overshoot > 15:
            st.error("❌ Mẻ hỏng! Quá nhiệt nghiêm trọng.")
        elif final_yield < 80:
            st.warning("⚠️ Hiệu suất thấp. Cần chỉnh lại PID.")
        else:
            st.success("🏆 TUYỆT VỜI! Mẻ thuốc hoàn hảo.")
            st.balloons() # Phần thưởng visual