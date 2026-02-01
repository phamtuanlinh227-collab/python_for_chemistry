# File: my_lab.py
# Đây là nơi chứa công cụ, không phải nơi chạy code

def doi_ra_kelvin(do_c):
    return do_c + 273.15

def tinh_CM(n, V):
    if V <= 0 or n <=0:
        return "giá trị không hợp lệ"
    return n / V

def tinh_khoi_luong(n, M):
    if n <= 0 or M <= 0:
        return "giá trị không hợp lệ"
    return n * M

# --- PHẦN DỮ LIỆU (DATABASE) ---
# Đây là bộ nhớ của thư viện
bang_tuan_hoan = {
    'H': 1,
    'He': 4,
    'C': 12,
    'N': 14,
    'O': 16,
    'Na': 23,
    'Mg': 24,
    'Al': 27,
    'S': 32,
    'Cl': 35.5,
    'K': 39,
    'Ca': 40,
    'Fe': 56,
    'Cu': 64,
    'Zn': 65,
    'Ag': 108,
    'Ba': 137,
    'Au': 197,
    'Ag':108
}

# --- PHẦN HÀM MỚI ---
def lay_M(nguyen_to):
    # Hàm .get() sẽ tìm xem nguyên tố có trong kho không
    # Nếu có thì trả về số M, nếu không thì trả về None
    return bang_tuan_hoan.get(nguyen_to)

# --- HÀM ---
def tinh_so_mol(m, M):
    if m<=0 or M<=0:
        return "giá trị không hợp lệ"
    return m / M

# Hàm tính tổng M của một phân tử phức tạp
# Input 'phan_tu' sẽ là một dict, ví dụ: {'H': 2, 'S': 1, 'O': 4}
def tinh_M_phan_tu(phan_tu):
    tong_M = 0  # Ban đầu chưa có gì
    
    # Cú pháp thần thánh: Lặp qua từng chất trong giỏ hàng
    # .items() giúp lấy cả Tên (key) và Số lượng (value) cùng lúc
    for ten_nguyen_to, so_luong in phan_tu.items():
        
        # 1. Tra bảng giá (Lấy M từ kho)
        M = lay_M(ten_nguyen_to)
        
        # 2. Check lỗi: Nếu lỡ gặp chất lạ (VD: 'Uranium')
        if M is None:
            return f"Lỗi: Không tìm thấy chất {ten_nguyen_to}"
            
        # 3. Cộng dồn vào tổng (Giá x Số lượng)
        tong_M += M * so_luong
        
    return tong_M