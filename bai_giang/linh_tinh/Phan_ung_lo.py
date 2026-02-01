class LoPhanUng:
    def __init__(self, ten_lo, nhiet_do_max, ap_suat_max):
        self.ten = ten_lo
        self.t_max = nhiet_do_max
        self.p_max = ap_suat_max # Thêm giới hạn áp suất
        
        self.nhiet_do = 0
        self.ap_suat = 1 # Atm (Mặc định là 1)

    # Hàm nạp nhiệt (Mô phỏng: Nhiệt tăng thì Áp cũng tăng)
    def gia_nhiet(self, do_tang):
        self.nhiet_do += do_tang
        # Giả sử cứ tăng 10 độ thì áp suất tăng 0.5 atm (Quy luật giả định)
        self.ap_suat += (do_tang / 10) * 0.5 
        
        print(f"🔥 {self.ten} | T: {self.nhiet_do}°C | P: {self.ap_suat} atm")
        self.kiem_tra_an_toan()

    # Hàm xả áp (Logic bro vừa hỏi)
    def xa_ap(self):
        print(f"💨 Đang xả van lò {self.ten}...")
        
        # 1. Giảm áp suất về mức an toàn (ví dụ về 1 atm)
        self.ap_suat = 1 
        
        # 2. HỆ QUẢ: Nhiệt độ cũng bị giảm theo (ví dụ giảm 20 độ do mất nhiệt)
        self.nhiet_do -= 20 
        
        print(f"✅ Đã xả áp xong. Nhiệt độ giảm còn: {self.nhiet_do}°C")

    def xa_ap(self):
        print(f"   💨 Đang xả van khẩn cấp...")
        self.ap_suat = 1       # Áp suất về mức khí quyển
        self.nhiet_do -= 20    # Giả sử mỗi lần xả giảm được 20 độ
        print(f"   -> Đã xả. T: {self.nhiet_do}°C | P: {self.ap_suat} atm")

    def kiem_tra_an_toan(self):
        # Dùng WHILE: Chừng nào còn nguy hiểm thì còn xử lý
        while self.nhiet_do > self.t_max or self.ap_suat > self.p_max:
            print(f"🚨 CẢNH BÁO: Vẫn chưa an toàn! (T: {self.nhiet_do}/{self.t_max})")
            self.xa_ap() # Gọi hàm xả áp
            
            # (Quan trọng) Nếu xả mãi không được thì sao?
            if self.nhiet_do < 0: # Tránh lỗi logic nhiệt độ âm vô cực
                print("⚠️ Lò đã đóng băng, dừng xả!")
                break
        
        print("✅ Lò đã trở về trạng thái an toàn.")
    # Hàm này giúp Object tự giới thiệu bản thân
    def __str__(self):
        trang_thai = "🟢 ỔN ĐỊNH"
        if self.nhiet_do > self.t_max or self.ap_suat > self.p_max:
            trang_thai = "🔴 NGUY HIỂM"
        
        return f"[{self.ten}] {trang_thai} | T: {self.nhiet_do}°C | P: {self.ap_suat} atm"

# --- CHẠY THỬ ---
lo_A = LoPhanUng("Reactor-A", 200, 10) # Max 200 độ, Max 10 atm

print("\n--- Lần 1: Tăng nhẹ ---")
lo_A.gia_nhiet(100) 

print("\n--- Lần 2: Tăng mạnh (Gây quá áp/quá nhiệt) ---")
lo_A.gia_nhiet(150) # Tổng sẽ là 250 độ -> Bùm -> Tự xả