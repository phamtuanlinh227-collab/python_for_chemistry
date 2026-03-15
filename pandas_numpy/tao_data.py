import os
import pandas as pd
import numpy as np

print("🚀 ĐANG TẠO 100 FILE EXCEL VÀO THƯ MỤC 'Du_Lieu_Lab'...")

# 1. Tạo một cái Folder (nếu chưa có)
thu_muc = "Du_Lieu_Lab"
os.makedirs(thu_muc, exist_ok=True)

# 2. Vòng lặp đẻ ra 100 file
for i in range(1, 101):
    # Dùng Numpy tạo ngẫu nhiên 5 mức điểm Toán, Lý, Hóa từ 4.0 đến 10.0
    data = {
        'Ma_SV': [f"SV_To{i}_01", f"SV_To{i}_02", f"SV_To{i}_03", f"SV_To{i}_04", f"SV_To{i}_05"],
        'Toan': np.round(np.random.uniform(4.0, 10.0, 5), 1),
        'Ly': np.round(np.random.uniform(4.0, 10.0, 5), 1),
        'Hoa': np.round(np.random.uniform(4.0, 10.0, 5), 1)
    }
    df = pd.DataFrame(data)
    
    # Đặt tên file: bang_diem_to_1.xlsx, bang_diem_to_2.xlsx...
    duong_dan = os.path.join(thu_muc, f"bang_diem_to_{i}.xlsx")
    df.to_excel(duong_dan, index=False)

print("✅ BÙM! Mở cột bên trái VS Code ra xem, 100 file Excel đã ra đời!")