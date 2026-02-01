import pandas as pd

# 1. Đọc dữ liệu
df = pd.read_csv('thi_nghiem.csv')

print("--- 📊 DỮ LIỆU GỐC ---")
print(df)

# --- PHÉP MÀU BẮT ĐẦU TẠI ĐÂY ---

# 2. Lấy riêng 1 cột ra xem
# Cú pháp: df['Tên_Cột']  (Giống hệt Dictionary bro đã học)
cot_nong_do = df['Nong_do_A']
print("\n--- Chỉ xem cột Nồng độ A ---")
print(cot_nong_do)

# 3. Tính toán cả cột KHÔNG CẦN FOR
# Nhiệm vụ: Chuyển đổi nồng độ A sang đơn vị mới (x1000)
# Trong Excel bro phải kéo công thức từ trên xuống dưới.
# Ở đây bro chỉ cần viết đúng 1 phép tính:
df['Nong_do_A_mM'] = df['Nong_do_A'] * 1000 

print("\n--- Đã thêm cột đơn vị mM (milliMolar) ---")
print(df)

# 4. Lọc dữ liệu (Filtering) - Cái này cực phê!
# Nhiệm vụ: Tìm những thời điểm mà Nhiệt độ > 27 độ
# Cách cũ: if nhiet_do > 27: append... (Dài dòng)
# Cách Pandas:
ngay_nong = df[df['Nhiet_do'] > 27]

print("\n--- ☀️ Những ngày nhiệt độ trên 27 độ ---")
print(ngay_nong)

# 5. Thống kê nhanh
print("\n--- 📈 Báo cáo nhanh ---")
print("Nhiệt độ trung bình:", df['Nhiet_do'].mean())
print("Nồng độ A cao nhất:", df['Nong_do_A'].max())