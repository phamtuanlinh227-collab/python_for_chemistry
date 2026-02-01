import matplotlib.pyplot as plt # Gọi thợ vẽ
import random # Gọi thêm ông thần ngẫu nhiên để mô phỏng cho thật

# --- PHẦN 1: CÁI KHUÔN (CLASS) ---
class BonChua:
    def __init__(self, ten, v_max):
        self.ten = ten
        self.v_max = v_max
        self.v = 0 # Ban đầu rỗng

    def nap_ngau_nhien(self):
        # Mô phỏng: Mỗi phút nạp ngẫu nhiên từ 10 đến 50 lít
        luong_nap = random.randint(10, 50)
        
        # Logic cộng dồn (Không cần if/else rườm rà cho demo này)
        if self.v + luong_nap > self.v_max:
            self.v = self.v_max # Tràn thì chỉ đầy max thôi
        else:
            self.v += luong_nap
        
        return self.v # Trả về mức hiện tại để ghi vào sổ

# --- PHẦN 2: KHỞI TẠO TRẠI BỒN (LIST OF OBJECTS) ---
# Tạo danh sách chứa 3 cái bồn
trai_bon = []
trai_bon.append(BonChua("Tank A", 1000)) # Bồn to
trai_bon.append(BonChua("Tank B", 500))  # Bồn nhỏ
trai_bon.append(BonChua("Tank C", 800))  # Bồn vừa

# Tạo sổ nhật ký dữ liệu cho từng bồn (List rỗng để hứng số liệu)
# data_bon_A = [], data_bon_B = [] ... (Làm thế này hơi thủ công, nhưng dễ hiểu trước đã)
history = {
    "Tank A": [],
    "Tank B": [],
    "Tank C": []
}
thoi_gian = [] # Trục hoành

# --- PHẦN 3: CHẠY MÔ PHỎNG (DATA LOGGING) ---
print("⏳ Đang chạy mô phỏng nạp liệu trong 20 phút...")

for phut in range(21): # Chạy từ phút 0 đến phút 20
    thoi_gian.append(phut) # Ghi giờ
    
    # Duyệt qua từng bồn trong trại để nạp và ghi số liệu
    for bon in trai_bon:
        muc_nuoc_hien_tai = bon.nap_ngau_nhien()
        
        # Ghi vào sổ nhật ký tương ứng với tên bồn
        history[bon.ten].append(muc_nuoc_hien_tai)

# --- PHẦN 4: VẼ ĐỒ THỊ (VISUALIZATION) ---
plt.figure(figsize=(10, 6)) # Tạo khung tranh to đẹp

# Vẽ đường cho Tank A
plt.plot(thoi_gian, history["Tank A"], label="Tank A (1000L)", color="blue", marker="o")
# Vẽ đường cho Tank B
plt.plot(thoi_gian, history["Tank B"], label="Tank B (500L)", color="green", marker="s")
# Vẽ đường cho Tank C
plt.plot(thoi_gian, history["Tank C"], label="Tank C (800L)", color="red", marker="^")

# Kẻ vạch giới hạn Max của từng bồn (để xem khi nào tràn)
plt.axhline(y=1000, color='blue', linestyle='--', alpha=0.3)
plt.axhline(y=500, color='green', linestyle='--', alpha=0.3)

# Trang trí
plt.title("THEO DÕI QUÁ TRÌNH NẠP ĐẦY TANK FARM")
plt.xlabel("Thời gian (Phút)")
plt.ylabel("Thể tích (Lít)")
plt.grid(True)
plt.legend() 

plt.show() 
