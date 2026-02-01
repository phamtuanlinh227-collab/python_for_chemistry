from mendeleev import element

print("--- ⚛️ TỪ ĐIỂN HÓA HỌC GEN Z ⚛️ ---")
print("(Gõ 'exit' hoặc 'thoat' để tắt máy nhé bro!)")

while True:
    # 1. Nhập liệu
    # .strip() để xóa khoảng trắng thừa nếu lỡ tay ấn space
    raw_input = input("\n>> Nhập ký hiệu nguyên tố (ví dụ Fe, Au): ").strip()
    
    # 2. Kiểm tra điều kiện THOÁT (Phanh khẩn cấp)
    # Chuyển về chữ thường (.lower) để gõ 'EXIT' hay 'exit' đều nhận
    if raw_input.lower() in ['exit', 'thoat', 'quit']:
        print("Bye bye bro! Hẹn gặp lại 👋")
        break # <--- Lệnh này phá vỡ vòng lặp, kết thúc chương trình

    # 3. Xử lý logic (Nằm trong try-except để bắt lỗi)
    try:
        # Chuẩn hóa đầu vào (ví dụ 'fe' -> 'Fe')
        symbol = raw_input.capitalize()
        
        # Lấy dữ liệu
        chat = element(symbol)
        
        # In kết quả (Đã sửa lỗi chính tả automic -> atomic)
        print(f"✅ Tên: {chat.name}")
        print(f"🔢 Số hiệu Z: {chat.atomic_number}")
        print(f"⚖️  Khối lượng M: {chat.atomic_weight:.2f} g/mol")
        print(f"⚡ Cấu hình e: {chat.ec}")
        
    except Exception as e:
        # Nếu nhập sai (ví dụ 'Vibranium')
        print(f"❌ Lỗi rồi: Không tìm thấy chất '{raw_input}' trong bảng tuần hoàn!")
        # Mẹo: Không in lỗi 'e' dài dòng nữa cho người dùng đỡ sợ, chỉ báo sai thôi.

print("--- Chương trình đã tắt ---")


# Code structure supported by AI, customized by Tuan Linh
# Project: Chemistry Automation