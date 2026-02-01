print("--- 📥 MÁY ĐỌC DỮ LIỆU ---")

# Mở file để ĐỌC (mode 'r')
try:
    with open('data_nhiet_do.txt', 'r', encoding='utf-8') as f:
        # Lệnh f.readlines() -> Đọc toàn bộ các dòng và nhét vào 1 cái List
        # Mỗi dòng là 1 phần tử trong list
        noi_dung_tho = f.readlines()

    print(f"Dữ liệu thô vừa đọc: {noi_dung_tho}")
    print("-" * 30)

    # --- XỬ LÝ SỐ LIỆU (DATA CLEANING) ---
    # Lúc này dữ liệu vẫn là Chữ (String) và dính cái đuôi '\n'
    # VD: ['25.5\n', '26.1\n'...] -> Phải làm sạch!

    danh_sach_so = []

    for dong in noi_dung_tho:
        # 1. .strip() -> Cắt bỏ khoảng trắng và cái đuôi '\n' thừa thãi
        so_sach = dong.strip()
        
        # 2. float() -> Biến chữ thành số thực để tính toán
        gia_tri = float(so_sach)
        
        # 3. Ném vào list sạch
        danh_sach_so.append(gia_tri)
        print(f"Đã lấy được số: {gia_tri}")

    # --- TÍNH TOÁN ---
    print("-" * 30)
    print(f"List chuẩn: {danh_sach_so}")
    print(f"🌡️ Nhiệt độ trung bình: {sum(danh_sach_so)/len(danh_sach_so):.2f} độ C")

except FileNotFoundError:
    print("❌ Lỗi: Không tìm thấy file 'data_nhiet_do.txt' đâu cả!")

# Code structure supported by AI, customized by Tuan Linh
# Project: Chemistry Automation