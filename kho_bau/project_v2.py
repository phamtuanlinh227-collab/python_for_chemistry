import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from rdkit import Chem
from rdkit.Chem import Descriptors


st.set_page_config(page_title = "HỆ THỐNG ĐIỀU CHẾ THUỐC", page_icon ="💊", layout = "wide")
st.title("SMART PHARMA REACT")
st.markdown("Hệ thống tích hợp: Hóa Tin + PID")

# --- DATA THUỐC ---
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
# Kiểm tra chất lượng thuốc theo Lipinski Rule
def check_quality(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return None, 0, 0, "Lỗi: Công thức SMILES không hợp lệ"
    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    if mw <= 500 and logp <= 5:
        status = "✅ Đạt chuẩn Drug-like (Dễ hấp thụ)"
    else:        status = "⚠️ Vi phạm Lipinski (Khó hấp thụ)"
    return mol, mw, logp, status
# --- GIAO DIỆN --- 
class PharmaApp: 
    def __init__(self, Kp, Ki, Kd, setpoint):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.setpoint = setpoint
        self.prev_error = 0
        self.integral = 0
    def computer(self, current_temp):
        error = self.setpoint - current_temp
        if abs(error) < 10:
            self.integral += error
        P = self.Kp * error
        I = self.Ki * self.integral
        D = self.Kd * (error - self.prev_error)
        self.prev_error = error
        output = P + I + D
        return max(0 , min(100, output))
    def run_simulation(pid_params, target_temp, steps=100):
        Kp, Ki, Kd = pid_params
        pid = PharmaApp(Kp, Ki, Kd, target_temp)
        current_temp = 25.0
        progress = 0.0
        history = {"time": [], "temp": [], "power": [], "progress": []}
        for t in range(steps):
            sensor_temp = current_temp + np.random.normal(0, 0.5)
            power = pid.computer(sensor_temp)
            current_temp += (power * 0.2) - 0.8  # Simulate heating effect
            if abs(current_temp - target_temp) <= 5:
                progress += 1.5  # reaction progress increases when near target temp
                progress = min(100, progress + 1.5)
            history["time"].append(t)
            history["temp"].append(sensor_temp)
            history["power"].append(power)
            history["progress"].append(progress)
        return history

# --- CHẠY APP ---
# giao diện bên trái
with st.sidebar:
    st.header("1.Cấu hình Hóa Học 🧪")
    ten_thuoc = st.selectbox("Chọn thuốc muốn nấu:", list(duoc_dien.keys()))
    thuoc_info = duoc_dien[ten_thuoc]
    mol, mw, logp, status = check_quality(thuoc_info["smiles"])
    st.info(f"Khối lượng: {mw:.1f}\n\nĐộ ưa béo (LogP): {logp:.1f}\n\n{status}")
    st.markdown("---")
    st.header("2.Cấu hình hóa lí")

    target_t= st.slider("Nhiệt độ mục tiêu (°C)", 20, 120, int(thuoc_info["temp_opt"]))

    kp = st.number_input("Tỷ lệ Kp", 0.0, 10.0, 2.5)
    ki = st.number_input("Tỷ lệ Ki", 0.0, 5.0, 0.2)
    kd = st.number_input("Tỷ lệ Kd", 0.0, 10.0, 1.5)

# --- KHU VỰC HIỂN THỊ CHÍNH ---
if st.button("KHỞI ĐỘNG LÒ", use_container_width=True):
    data = PharmaApp.run_simulation((kp, ki, kd), target_t)
    col1, col2 = st.columns([3,1])
    with col1:
        st.subheader("Biểu đồ nhiệt độ theo thời gian")
        fig, ax = plt.subplots(figsize=(10,4))
        ax.plot(data["time"], data["temp"], label="Nhiệt độ thực tế", color="blue", linewidth=2)
        ax.axhline(target_t, color='red', linestyle='--', label="Mục tiêu (Setpoint)")
        ax.set_xlabel("Thời gian (giây)")
        ax.set_ylabel("Nhiệt độ (°C)")
        ax.legend()
        st.pyplot(fig)
    with col2:
        st.subheader("Kết quả mẻ nấu")
        final_progress = data['progress'][-1]
        st.metric(label="Tiến độ phản ứng", value=f"{final_progress:.1f}%")
        if final_progress >= 95:
            st.success("Mẻ thuốc thành công")
            st.balloons()
        elif final_progress >= 50:
            st.warning("Lò chưa đủ ấm, phản ứng chưa xong. Hãy tăng Kp hoặc giảm nhiễu.")
        else:
            st.error("Lò quá lạnh, phản ứng gần như không xảy ra. Hãy tăng Kp hoặc giảm nhiễu.")
        
