import my_lab as chem

print("--- ⚖️ MÁY TÍNH PHÂN TỬ ---")

gio_hang = {}
while True:
    nguyen_to = input("Nhập tên nguyên tố bạn muốn tính(nhập ok để kết thúc)").capitalize()
   
    if nguyen_to.lower() == "ok":
        break
    try:
        so_luong = int(input(f"Số lượng của {nguyen_to}"))
        gio_hang[nguyen_to] = so_luong
    except:
        print("Vui lòng nhập số hợp lệ.")

print(f"Phân tử khối của {gio_hang} là: {chem.tinh_M_phan_tu(gio_hang)} g/mol")