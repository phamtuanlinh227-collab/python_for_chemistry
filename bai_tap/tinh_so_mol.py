import pandas as pd

df = pd.read_csv('pha_che.csv')

df['So_mol'] = df['The_tich_mL'] / 1000 * df['Nong_do_M']

print("Dữ liệu sau khi tính số mol:")
print(df)

df.to_csv('ket_qua_so_mol.csv', index = False)
print("\n✅ Đã lưu file 'ket_qua_so_mol.csv'. Bro mở lên xem thử đi!")

a = df['So_mol']
b = df[df['So_mol'] > 0.1]
print("\n --- Cột số mol lớn hơn 0.1 ---")
print(b)
    
    
