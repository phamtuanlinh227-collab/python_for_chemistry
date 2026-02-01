import pandas as pd

df = pd.read_csv('hoa_chat.csv')

df['Tong_tien'] = df['Khoi_luong_ton(g)'] * df['Don_gia_1g(k_VND)']
print("Dữ liệu sau khi tính tổng tiền:")
print(df)

df.to_csv('can_nhap_hang.csv', index=False)
print("\n Đã lưu file vào'can_nhap_hang.csv' rồi nhé bro!")

a = df[df['Khoi_luong_ton(g)'] < 100]
print("\n --- Hóa chất có khối lượng tồn dưới 100g ---")
print(a)

b = a.sort_values(by='Tong_tien', ascending=False)
print("\n --- Dữ liệu sắp xếp theo tổng tiền giảm dần ---")
print(b)