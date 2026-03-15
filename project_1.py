# 1. Khởi tạo lại từ đầu
git init

# 2. Kết nối lại với cái kho cũ
git remote add origin https://github.com/phamtuanlinh227-collab/python_for_chemistry.git

# 3. Gom đống đồ mới vào
git add .
git commit -m "Reset repository: Only keep weekend projects"

# 4. CHỐT HẠ: Lệnh này sẽ xóa sạch đống cũ trên GitHub và thay bằng đống mới này
git push -u origin master --force