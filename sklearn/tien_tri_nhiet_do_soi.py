import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

print("🤖 ĐANG KHỞI ĐỘNG TRÍ TUỆ NHÂN TẠO...\n")

# 1. BƯỚC CHUẨN BỊ DỮ LIỆU (Kinh nghiệm quá khứ)
# Dạy cho AI biết nhiệt độ sôi của 6 chất Ankan đầu tiên (Từ Metan C1 đến Hexan C6)
data = {
    'Ten_Chat': ['Metan', 'Etan', 'Propan', 'Butan', 'Pentan', 'Hexan'],
    'So_Carbon': [1, 2, 3, 4, 5, 6],
    'Nhiet_Do_Soi': [-161.5, -88.6, -42.1, -0.5, 36.1, 68.7] # Độ C
}
df = pd.DataFrame(data)

print("📚 SÁCH GIÁO KHOA CHO AI HỌC:")
print(df[['Ten_Chat', 'So_Carbon', 'Nhiet_Do_Soi']])
print("-" * 50)

# Scikit-learn yêu cầu dữ liệu đầu vào (X) phải là ma trận 2 chiều (DataFrame)
X_train = df[['So_Carbon']] 
y_train = df['Nhiet_Do_Soi']

# 2. BƯỚC HỌC MÁY (Dạy AI tìm quy luật)
# Gọi thuật toán Hồi quy tuyến tính (Kẻ một đường thẳng đi qua các điểm dữ liệu)
mo_hinh_ai = LinearRegression()

print("🧠 AI ĐANG VẮT ÓC TÌM QUY LUẬT...")
mo_hinh_ai.fit(X_train, y_train) # Phép màu nằm đúng ở chữ "fit" này!
print("✅ AI ĐÃ HỌC XONG!\n")

# 3. BƯỚC TIÊN TRI (Dự đoán tương lai)
# Hỏi AI: "Ê, tao có một chất có 15 nguyên tử Carbon (Pentadecan), mày đoán xem nó sôi ở bao nhiêu độ?"
# Số 15 chưa từng xuất hiện trong sách giáo khoa lúc nãy!
chat_moi = pd.DataFrame({'So_Carbon': [15]})
nhiet_do_du_doan = mo_hinh_ai.predict(chat_moi)

print("🔮 LỜI TIÊN TRI TỪ AI:")
print(f"👉 Chất có 15 nguyên tử Carbon sẽ sôi ở khoảng: {np.round(nhiet_do_du_doan[0], 2)} độ C")