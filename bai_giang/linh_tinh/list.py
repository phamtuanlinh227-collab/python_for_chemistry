print("---- MÁY TÍNH HIỆU SUẤT TỰ ĐỘNG-----")
m_ly_thuyet = 10.0
m_thuc_te = [8.5, 9.2, 7.8, 9.5, 8.9, 1.0]

ds_hieu_suat = []

for m in m_thuc_te:
    if m < 5.0:
        print(f"Mẫu {m}g bị lỗi, bỏ qua.")
        continue
    hieu_suat = (m/m_ly_thuyet) * 100
    ds_hieu_suat.append(hieu_suat)

    print(f"Mẫu {m}g -> Hiệu suất: {hieu_suat:.2f}%")
print(f"Danh sách hiệu suất cuối cùng là: {ds_hieu_suat}")
 
# --- PHẦN BÁO CÁO ---
# sum(): Tính tổng
# len(): Đếm số lượng phần tử (Length)
# max(): Tìm số lớn nhất
# min(): Tìm số nhỏ nhất

h_trung_binh = sum(ds_hieu_suat) / len(ds_hieu_suat)
h_cao_nhat = max(ds_hieu_suat)
h_thap_nhat = min(ds_hieu_suat)

print("\n--- 📈 TỔNG KẾT ---")
print(f"Trung bình cộng: {h_trung_binh:.2f}%")
print(f"Cao nhất: {h_cao_nhat}%")
print(f"Thấp nhất: {h_thap_nhat}%")