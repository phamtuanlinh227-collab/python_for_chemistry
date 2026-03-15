import sys
import subprocess

print(f"🕵️ Đang tìm vị trí thật của Python... Thấy rồi: {sys.executable}")
print("🚀 Đang ép máy tính tải scikit-learn. Chờ khoảng 15-30 giây nhé...")

# Dòng lệnh này dùng chính cái Python đang chạy để gọi pip
# Dòng lệnh này dùng chính cái Python đang chạy để gọi pip
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'seaborn'])

print("\n🎉 BÙM! CÀI ĐẶT HOÀN TẤT! QUAY LẠI FILE TIÊN TRI ĐỂ CHẠY THÔI SẾP!")