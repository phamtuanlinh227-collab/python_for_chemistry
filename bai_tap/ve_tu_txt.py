import matplotlib.pyplot as plt

print("--- 📈 VẼ BIỂU ĐỒ TỪ FILE TXT ---")

# BƯỚC 1: Đọc dữ liệu từ file (Kỹ năng cũ)
ds_nhiet_do = []

try:
    with open('data_nhiet_do.txt', 'r', encoding='utf-8') as f:
        noi_dung = f.readlines()
        
    # Vòng lặp làm sạch dữ liệu
    for dong in noi_dung:
        # Cắt dòng, ép kiểu sang float, nhét vào list
        gia_tri = float(dong.strip())
        ds_nhiet_do.append(gia_tri)
        
    print(f"✅ Đã đọc được {len(ds_nhiet_do)} mẫu dữ liệu.")

    # BƯỚC 2: Tạo trục thời gian (Trục X)
    # Vì file chỉ có nhiệt độ, mình giả sử cứ 1 dòng là 1 phút
    # range(5) -> tạo ra [0, 1, 2, 3, 4]
    ds_thoi_gian = range(len(ds_nhiet_do))

    # BƯỚC 3: Vẽ đồ thị (Kỹ năng cũ)
    plt.plot(ds_thoi_gian, ds_nhiet_do, 'o-r', label='Nhiệt độ lò nung')
    
    # Trang trí
    plt.title("Biến thiên nhiệt độ theo thời gian")
    plt.xlabel("Thời gian (phút)")
    plt.ylabel("Nhiệt độ (°C)")
    plt.grid(True)
    plt.legend()
    
    # Bùm!
    plt.show()

except FileNotFoundError:
    print("❌ Lỗi: Không tìm thấy file dữ liệu đâu cả!")
except ValueError:
    print("❌ Lỗi: Trong file có dòng nào đó không phải là số!")