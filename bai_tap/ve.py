import my_lab as chem

print("--- ⚖️ MÁY TÍNH PHÂN TỬ ---")

# 1. Định nghĩa phân tử (Dưới dạng Dictionary)
# H2SO4 -> H:2, S:1, O:4
axit_sulfuric = {'H': 2, 'S': 1, 'O': 4}

# 2. Gọi hàm tính toán
ket_qua = chem.tinh_M_phan_tu(axit_sulfuric)

print(f"Công thức: H2SO4")
print(f"Cấu tạo: {axit_sulfuric}")
print("-" * 20)
print(f"👉 Phân tử khối (M) là: {ket_qua} g/mol")

# --- CHALLENGE PHỤ ---
# Bro thử tính cho Đường Glucozo (C6H12O6) xem ra bao nhiêu?
# C:6, H:12, O:6
print("\n--- Thử thách: Glucozo (C6H12O6) ---")
glucozo = {'C': 6, 'H': 12, 'O': 6}
print(f"M của Glucozo: {chem.tinh_M_phan_tu(glucozo)}")