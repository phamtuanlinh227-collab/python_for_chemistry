import pandas as pd
import numpy as np

# 1. Đọc dữ liệu
df = pd.read_csv('bi_an.csv') # Thử thay bằng file khác xem sao
t = df['Thoi_gian']
A = df['Nong_do_X']

# 2. Chuẩn bị 3 chìa khóa (3 loại trục Y)
# Bậc 0: Y = A
# Bậc 1: Y = ln(A)
# Bậc 2: Y = 1/A
cac_truong_hop = {
    "Bậc 0": A,
    "Bậc 1": np.log(A),
    "Bậc 2": 1 / A
}

best_r2 = -1      # Điểm kỷ lục hiện tại
best_bac = ""     # Tên của bậc tốt nhất

print(f"{'BẬC':<10} | {'R-SQUARED':<10} | {'KẾT LUẬN'}")
print("-" * 40)

# 3. Vòng lặp kiểm tra từng chìa khóa
for ten_bac, y_data in cac_truong_hop.items():
    # Tính R^2 cho trường hợp này
    r_squared = np.corrcoef(t, y_data)[0, 1] ** 2
    
    print(f"{ten_bac:<10} | {r_squared:.5f}    | ", end="")
    
    if r_squared > 0.98:
        print("✅ Có thể đúng")
    else:
        print("❌ Sai rồi")

    # Tìm ra thằng nào cao điểm nhất để trao cúp
    if r_squared > best_r2:
        best_r2 = r_squared
        best_bac = ten_bac

print("-" * 40)
print(f"🏆 CHỐT ĐƠN: Phản ứng này là {best_bac} (R^2 = {best_r2:.5f})")