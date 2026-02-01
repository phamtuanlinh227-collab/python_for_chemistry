import streamlit as st
import pandas as pd
import numpy as np
import time

# --- 1. CẤU HÌNH TRANG WEB ---
st.set_page_config(page_title="Nhà Máy Hóa Chất - Center Control", page_icon="🏭", layout="wide")

# --- 2. THANH ĐIỀU KHIỂN BÊN TRÁI (SIDEBAR) ---
st.sidebar.header("⚙️ BẢNG ĐIỀU KHIỂN")
st.sidebar.write("Chỉnh thông số đầu vào tại đây:")

# Kéo thanh trượt để chỉnh Nhiệt độ và Áp suất
temp_setpoint = st.sidebar.slider("Nhiệt độ mong muốn (°C)", min_value=0, max_value=200, value=120)
pressure_setpoint = st.sidebar.slider("Áp suất nồi hơi (Bar)", min_value=1, max_value=50, value=10)
run_simulation = st.sidebar.button("▶️ CHẠY MÔ PHỎNG")

# --- 3. GIAO DIỆN CHÍNH ---
st.title("🏭 DASHBOARD GIÁM SÁT HỆ THỐNG")
st.markdown("---") # Đường kẻ ngang

# Chia giao diện thành 3 cột để hiển thị số liệu (KPI)
col1, col2, col3 = st.columns(3)

# Logic giả lập: Hiệu suất phụ thuộc vào Nhiệt & Áp
hieu_suat = (temp_setpoint * 0.5) + (pressure_setpoint * 2)
if hieu_suat > 100: hieu_suat = 100 # Max là 100%

# Hiển thị số liệu to đẹp (Metric)
with col1:
    st.metric(label="Nhiệt độ Lò", value=f"{temp_setpoint} °C", delta="1.2 °C")
with col2:
    st.metric(label="Áp suất", value=f"{pressure_setpoint} Bar", delta="-0.5 Bar")
with col3:
    # Nếu hiệu suất thấp thì cảnh báo màu đỏ, cao thì màu xanh
    st.metric(label="Hiệu suất Phản ứng", value=f"{hieu_suat:.1f} %", 
              delta=f"{hieu_suat - 50:.1f} % so với TB")

# --- 4. BIỂU ĐỒ TƯƠNG TÁC ---
st.subheader("📈 Dự báo Xu hướng Nhiệt độ")

# Tạo dữ liệu giả: Đường cong đi lên rồi ổn định (giống bài PID nãy)
chart_data = pd.DataFrame({
    'Thời gian (Phút)': range(50),
    'Nhiệt độ Thực tế': [temp_setpoint * (1 - np.exp(-0.1 * i)) + np.random.normal(0, 2) for i in range(50)],
    'Mục tiêu': [temp_setpoint] * 50
})

# Vẽ biểu đồ vùng (Area Chart) cho đẹp
st.area_chart(chart_data.set_index('Thời gian (Phút)'), color=["#00FF00", "#FF0000"])

# --- 5. HIỆU ỨNG LOADING (Cho nó nguy hiểm) ---
if run_simulation:
    with st.spinner('Đang tính toán cân bằng vật chất...'):
        time.sleep(2) # Giả vờ tính trong 2 giây
    st.success("Đã cập nhật thông số thành công! Hệ thống ổn định.")
# --- 6. XUẤT BÁO CÁO (CHERRY ON TOP) ---
st.markdown("---")
st.subheader("📥 Trích xuất Dữ liệu")

# Chuẩn bị dữ liệu để tải
csv = chart_data.to_csv(index=False).encode('utf-8')

st.download_button(
    label="Tải xuống Báo cáo chi tiết (CSV)",
    data=csv,
    file_name='bao_cao_nha_may_vip.csv',
    mime='text/csv',
    help="Bấm vào đây để tải dữ liệu về máy tính"
)