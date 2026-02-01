import pandas as pd
import numpy as np  # Gọi thằng đệ chuyên toán học về

print("--- 🧪 XỬ LÝ SỐ LIỆU HÓA LÝ ---")

# 1. Đọc dữ liệu
df = pd.read_csv('thi_nghiem.csv')

# 2. TÍNH TOÁN CỘT MỚI (Dùng NumPy)
# np.log() là Logarit tự nhiên (ln)
# np.log10() là Logarit cơ số 10

# Tính ln(A) cho cả cột trong 1 nốt nhạc
df['Ln_A'] = np.log(df['Nong_do_A'])

# Tính 1/A cho cả cột
df['Nghich_dao_A'] = 1 / df['Nong_do_A']

print("Dữ liệu sau khi xử lý:")
print(df)

# 3. LƯU KẾT QUẢ RA FILE MỚI (Save)
# Bro không muốn tính xong rồi mất đúng không?
# index=False nghĩa là không lưu cái cột số thứ tự 0,1,2,3... thừa thãi
df.to_csv('ket_qua_da_xu_ly.csv', index=False)

print("\n✅ Đã lưu file 'ket_qua_da_xu_ly.csv'. Bro mở lên xem thử đi!")

# 4. TIỆN TAY VẼ LUÔN ĐỂ CHECK BẬC PHẢN ỨNG
# Vẽ Ln(A) theo Thời gian
df.plot(x='Thoi_gian', y='Ln_A', marker='s', color='green', title="Đồ thị Bậc 1 (Ln A)")
import matplotlib.pyplot as plt
plt.grid(True)
plt.ylabel("ln[A]")
plt.show()