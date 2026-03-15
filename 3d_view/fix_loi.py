import sys
import subprocess

print("Đang vá lỗi đồ cổ...")

# Ép nó cài thằng ipython_genutils bị thiếu
subprocess.check_call([sys.executable, "-m", "pip", "install", "ipython_genutils"])

print("✅ Đã vá xong! Chạy lại Streamlit thôi!")