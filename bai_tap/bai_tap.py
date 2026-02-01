class BonChuaHoaChat:
    def __init__(self, ten_lo, the_tich_max):
        self.ten = ten_lo
        self.v_max = the_tich_max
        self.v = 0
    def nap_be(self, do_tang):
        du_kien = self.v + do_tang
        if du_kien > self.v_max:
            luong_tran = du_kien - self.v_max
            self.v = self.v_max
            print(f" 🚨 CẢNH BÁO: Lượng hóa chất vượt quá giới hạn! Bể bị tràn {luong_tran} lít")
        else:
            self.v = du_kien
            print(f"Đã nạp thành công {du_kien} lít")
    
    def xa_be(self, do_giam):
        if do_giam > self.v:
            print(f" ⚠️ CẢNH BÁO: Đã rút {do_giam} lít, bể đã cạn đáy!!!")
            self.v = 0
        else:
            self.v -= do_giam
            print(f" ✅ Đã rút {do_giam} l, hiện còn {self.v} l trong bể.") 
    def __str__(self):
        # Sửa lại công thức toán: Tỷ lệ 0.0 -> 1.0 thôi
        if self.v_max == 0: ty_le = 0
        else: ty_le = self.v / self.v_max
        
        do_dai_bar = 20 
        so_dau_bang = int(ty_le * do_dai_bar)
        so_khoang_trang = do_dai_bar - so_dau_bang
        
        thanh_bar = "=" * so_dau_bang + " " * so_khoang_trang
        
        # Sửa lại tên biến self.v và self.v_max
        return f"[{self.ten}] |{thanh_bar}| {self.v}/{self.v_max} ({int(ty_le*100)}%)"
be_A = BonChuaHoaChat("Bon-A", 1000) # Bể chứa max 1000 lít
print("\n--- HỆ THỐNG QUẢN LÝ BỒN CHỨA  ---")
print("Các lệnh: 'nạp', 'rút', nhấn 'enter' để thoát")
print(be_A)
while True:
    lenh = input("Nhập lệnh (nạp/rút) hoặc nhấn enter để dừng: ").lower()
    if lenh == "nạp":
        so_lit = int(input("Nhập số lít bạn muốn nạp: "))
        be_A.nap_be(so_lit)
        print(be_A)
    elif lenh == "rút":
        so_lit = int(input("Nhập số lít bạn muốn rút: "))
        be_A.xa_be(so_lit)
        print(be_A)
    elif lenh == "":
        break
    else:
        print("Lệnh không hợp lệ. Vui lòng chọn 'nạp', 'rút' hoặc nhấn enter để dừng.")