# app.py
import streamlit as st
import matplotlib.pyplot as plt

# Triệu hồi "đệ tử" từ 2 file kia
from library import duoc_dien, check_quality
from brain import run_simulation

# Cài đặt trang
st.set_page_config(page_title="Smart Reactor", layout="wide")
st.title("🏭 Hệ Thống Lò Phản Ứng Số v2.0")

# --- BẢNG ĐIỀU KHIỂN BÊN TRÁI ---
with st.sidebar:
    st.header("1. Cấu hình Hóa Học 🧪")
    ten_thuoc = st.selectbox("Chọn mẻ thuốc muốn nấu:", list(duoc_dien.keys()))
    thuoc_info = duoc_dien[ten_thuoc]
    
    # RDKit phân tích
    mol, mw, logp, status = check_quality(thuoc_info["smiles"])
    st.info(f"Khối lượng: {mw:.1f}\n\nĐộ ưa béo (LogP): {logp:.1f}\n\n{status}")
    
    st.markdown("---")
    st.header("2. Cấu hình Hóa Lý ⚙️")
    # Tự động gợi ý nhiệt độ theo thuốc
    target_t = st.slider("Nhiệt độ mục tiêu (°C)", 20, 120, int(thuoc_info["temp_opt"]))
    
    # Thông số PID
    kp = st.number_input("Tỷ lệ (Kp) - Chân ga", 0.0, 10.0, 2.5)
    ki = st.number_input("Tích phân (Ki) - Bộ nhớ", 0.0, 5.0, 0.2)
    kd = st.number_input("Đạo hàm (Kd) - Chân phanh", 0.0, 10.0, 1.5)

# --- KHU VỰC HIỂN THỊ CHÍNH ---
if st.button("🚀 KHỞI ĐỘNG LÒ", use_container_width=True):
    # Gọi não bộ tính toán
    data = run_simulation(target_t, (kp, ki, kd))
    
    # Vẽ biểu đồ
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader("📈 Biểu đồ Nhiệt độ")
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(data["time"], data["temp"], label="Nhiệt độ thực tế", color="blue", linewidth=2)
        ax.axhline(target_t, color='red', linestyle='--', label="Mục tiêu (Setpoint)")
        ax.set_xlabel("Thời gian (phút)")
        ax.set_ylabel("Nhiệt độ (°C)")
        ax.legend()
        ax.grid(True, linestyle=":", alpha=0.7)
        st.pyplot(fig)
        
    with col2:
        st.subheader("📊 Kết Quả Mẻ Nấu")
        final_progress = data['progress'][-1]
        st.metric(label="Tiến độ phản ứng", value=f"{final_progress:.1f}%")
        
        if final_progress >= 95:
            st.success("🎉 Mẻ thuốc thành công mỹ mãn!")
            st.balloons()
        elif final_progress >= 50:
            st.warning("⚠️ Lò chưa đủ ấm, phản ứng chưa xong. Hãy tăng Kp hoặc giảm nhiễu.")
        else:
            st.error("❌ Phản ứng thất bại. Thuốc hỏng bét!")