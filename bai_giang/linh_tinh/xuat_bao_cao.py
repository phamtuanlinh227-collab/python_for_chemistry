# Dữ liệu cũ
m_ly_thuyet = 10.0
m_thuc_te = [8.5, 9.2, 1.0, 9.5, 8.9]

# Mở file để chuẩn bị ghi (Mode 'w' - Write)
print("⏳ Đang tạo báo cáo...")

with open('baocao_thi_nghiem.txt', 'w', encoding='utf-8') as f:
    # 1. Ghi tiêu đề
    f.write("=== BÁO CÁO KẾT QUẢ THÍ NGHIỆM ===\n")
    f.write(f"Khối lượng lý thuyết: {m_ly_thuyet} g\n")
    f.write("-" * 30 + "\n") # Kẻ đường gạch ngang trong file

    # 2. Vòng lặp tính toán & Ghi file
    ds_hieu_suat = []
    
    for m in m_thuc_te:
        if m < 5.0:
            # Ghi lỗi vào file luôn
            f.write(f"⚠️ Mẫu {m}g: BỊ LỖI (Bỏ qua)\n")
            continue
            
        h = (m / m_ly_thuyet) * 100
        ds_hieu_suat.append(h)
        
        # Ghi kết quả từng dòng
        f.write(f"✅ Mẫu {m}g -> Hiệu suất: {h:.2f}%\n")

    # 3. Ghi tổng kết
    f.write("-" * 30 + "\n")
    if len(ds_hieu_suat) > 0:
        h_tb = sum(ds_hieu_suat) / len(ds_hieu_suat)
        f.write(f"📈 Hiệu suất trung bình: {h_tb:.2f}%\n")
        f.write(f"🏆 Cao nhất: {max(ds_hieu_suat):.2f}%\n")
    
print("✅ Xong! Bro mở file 'baocao_thi_nghiem.txt' lên mà xem!")