import streamlit as st
import py3Dmol
from stmol import showmol

st.set_page_config(page_title="Bảo tàng 3D Pro Max", page_icon="🧬", layout="wide")
st.title("Phòng Thí Nghiệm 3D 🧬")

# 1. TẠO MENU CHỌN THUỐC ĐỂ NGHỊCH
thuoc_dict = {
    "Cafein (Tỉnh táo)": "2519",
    "Aspirin (Giảm đau)": "2244",
    "Penicillin (Kháng sinh)": "5904"
}
ten_thuoc = st.selectbox("Bro muốn xem cấu trúc chất nào?", list(thuoc_dict.keys()))
cid_code = thuoc_dict[ten_thuoc]

# 2. KHỞI TẠO MÔ HÌNH
view = py3Dmol.view(query=f'cid:{cid_code}') 

# 3. NGHỊCH STYLE (ĐỘ KIỂNG CHO PHÂN TỬ)
# Kiểu greenCarbon: Bôi màu Carbon thành xanh lá cho dễ nhìn, Oxy đỏ, Nito xanh dương
view.setStyle({'stick': {'colorscheme': 'greenCarbon', 'radius': 0.2}})

# Thêm "Lớp da" (Bề mặt Van der Waals) mờ mờ ảo ảo bao quanh
view.addSurface(py3Dmol.VDW, {'opacity': 0.5, 'color': 'white'})

# Bật chế độ tự quay
view.setBackgroundColor('#0E1117')
view.spin(True)

# 4. HIỂN THỊ LÊN STREAMLIT
showmol(view, height=500, width=800)
st.success("Dùng chuột lật, xoay, và cuộn để zoom nhé bro!")