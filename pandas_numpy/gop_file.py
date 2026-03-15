import pandas as pd

print("🚀 KÍCH HOẠT TUYỆT KỸ: GỘP THỂ ĐẠI PHÁP...\n")

# 1. GIẢ LẬP 3 FILE EXCEL GỬI TỪ 3 TỔ (Thực tế bro sẽ dùng pd.read_excel)
to_1 = pd.DataFrame({'Ten': ['An', 'Binh'], 'Diem_Lab': [8.5, 9.0]})
to_2 = pd.DataFrame({'Ten': ['Cuong', 'Dung'], 'Diem_Lab': [7.0, 6.5]})
to_3 = pd.DataFrame({'Ten': ['Eo', 'Phuc'], 'Diem_Lab': [10.0, 8.0]})

print("📁 Dữ liệu Tổ 1:\n", to_1, "\n")
print("📁 Dữ liệu Tổ 2:\n", to_2, "\n")
print("📁 Dữ liệu Tổ 3:\n", to_3, "\n")
print("-" * 40)

# 2. SỨC MẠNH CỦA PANDAS: GỘP TẤT CẢ LÀM MỘT
# Bước A: Gom tất cả các file vào một cái "túi" (Danh sách - List)
danh_sach_file = [to_1, to_2, to_3]

# Bước B: Dùng pd.concat() để úp tụi nó lên nhau
# ignore_index=True nghĩa là: "Ê Pandas, đánh lại số thứ tự từ 0 đến 5 cho đẹp nhé!"
bang_tong = pd.concat(danh_sach_file, ignore_index=True)

print("👑 BẢNG TỔNG KẾT QUYỀN LỰC (Đã gộp xong):")
print(bang_tong)
print("-" * 40)

# Bonus: Đẻ luôn ra 1 file Excel tổng nộp cho thầy!
# bang_tong.to_excel("Bang_Tong_Ket_Lab.xlsx", index=False)
# print("Đã xuất file Excel tổng!")