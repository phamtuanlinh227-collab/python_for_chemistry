from rdkit import Chem
from rdkit.Chem import Descriptors
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
#---- CẤU HÌNH ----
st.set_page_config(page_title = "Smart Pharma Reactor", page_icon = "💊", layout = "wide")

st.title("Smart Pharma Reactor v1.0")
st.markdown("Điều chình hệ thống Kp,Ki,Kd để tìm ra đường cong hoàn hảo")
# --- TỦ THUỐC ---
duoc_dien = {
    "Aspirin": {
        "smiles": "CC(=O)Oc1ccccc1C(=O)O",
        "temp_opt": 70.0,
        "temp_max": 80.0
    },
    "Ibuprofen": {
        "smiles": "CC(C)Cc1ccc(cc1)C(C)C(=O)O",
        "temp_opt": 76.0,
        "temp_max": 78.0
    },
    "Cafein (Test)": {
        "smiles": "CN1C=NC2=C1C(=O)N(C(=O)N2C)C",
        "temp_opt": 80.0,
        "temp_max": 100.0
    }
}
#---- GIAO DIỆN ----
st.markdown("---")
st.sidebar.header("Đặc tính lò")
noise = st.sidebar.slider("Độ nhiễu của phản ứng", 0, 2.0, 0.5)
soc_nhiet = st.checkbox("Sự cố:Mất điện làm mát (phút 60)")
def quality_check(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if not mol: return None, "Lỗi công thức"
    # Tính toán hóa chất 
    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)

    status = "Đạt chuẩn Drug_Like"
    if mw > 500 or logp > 5:
        status = " Cảnh Báo: Khó hấp thụ"
    return mol, logp, mw, status

class PIDauto:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0  # sai số trước đó
        self.integral = 0    # tích phân
    def updates(self, current_value, target):
        error = target - current_value
        P = self.Kp * error

        if abs(error) < 10:
            self.integral += error
        I = self.Ki * self.integral

        D = self.Kd * (error - self.prev_error)
        self.prev_error = error

        output = P + I + D
        return max(0, min(100, output))
# Khu vục điều khiển
with st.sidebar:
    st.header("1. Cấu hình Nguyên Liệu")
    selected_drug = st.selectbox("Chọn loại thuốc bạn cầu nấu:".lower, list(duoc_dien.keys()))
    smiles = duoc_dien[selected_drug]
    mol, mw, logp, status = quality_check(smiles)
    # hiện thị thông tin của thuốc 
    st.info(f"**{selected_drug}**\n\nMW: {mw:.1f} | LogP: {logp:.1f}\n\n{status}")
    st.markdown("---")
    st.header("2.Cấu hình lò phản ứng")
    target_temp = st.slider("Nhiệt độ phản ứng", 50, 120,80)

    Kp = st.sidebar.slider("Kp (sức mạnh)", 0, 5.0, 1.0, step = 0.1)
    Ki = st.sidebar.slider("Ki (cộng dồn)", 0, 2.0, 0.5, step = 0.05)
    Kd = st.sidebar.slider("Kd (giảm xóc)", 0, 5.0, 1.0, step = 0.1)
# --- MÔ PHỎNG QUÁ TRÌNH ---
if st.button("KÍCH HOẠT QUÁ SẢN XUẤT"):

    time_steps = 120
    temps = []
    setpoints = []
    powers = []
    reaction_progress = [] # % phản ứng hoàn thành

    current_temp = 25
    current_progress = 0
    pid = PIDauto(Kp, Ki, Kd, target_temp)

    progress_bar = st.progress(0)

    for t in range(time_steps):
        sensor_val = current_temp + np.random.normal(0, noise) # tạo nhiễu cảm biến
        power = pid.compute(sensor_val)
        cooling_factor = 0.5
        if soc_nhiet and t > 60 or t < 80:
            cooling_factor = -1.0

        current_temp += (power * 0.3) - cooling_factor
        rate = 0
    
        if abs(current_temp - target_temp) < 5:
            rate = 1.0 # Tốc độ chuẩn
        elif abs(current_temp - target_temp) < 10:
            rate = 0.2 # Quá lạnh hoặc quá nóng thì phản ứng chậm
        else:
            ate = 0 # Không phản ứng
            
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
        ig, ax1 = plt.subplots(figsize=(10, 6))
        
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



    

    
