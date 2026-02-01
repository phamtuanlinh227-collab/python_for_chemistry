try:
    with open('phan_ung_k.txt', 'r', encoding='utf-8') as f:
        noi_dung= f.readlines()
    print("Máy phân tích hóa học K 3000")
    print("-" * 30)

    time = []
    nong_do = []
    for dong in noi_dung[1:]:
        cac_phan = dong.strip().split(',')

        t = float(cac_phan[0])
        C = float(cac_phan[1])

        time.append(t)
        nong_do.append(C)
    print(f"Đã xử lí xong mẫu số liệu")
    print("Đang vẽ đồ thị")
    import matplotlib.pyplot as plt
    plt.plot(time, nong_do, 'o-b', label='Nồng độ chất phản ứng K')
    plt.title("Đồ thị nồng độ phản ứng chất K theo thời gian")
    plt.xlabel("Thời gian (giây)")
    plt.ylabel("Nồng độ chất K (mol/L)")
    plt.grid(True)
    plt.legend()
    print("Đang xuất báo cáo....")
    C_dau = nong_do[0]
    C_cuoi = nong_do[-1]
    sum_time = time[-1]
    
    with open('ket_qua_phan_tich.txt', 'w', encoding='utf-8') as f_ot:
        f_ot.write("BÁO CÁO PHÂN TÍCH PHẢN ỨNG CHẤT K\n")
        f_ot.write(f"Nồng độ ban đầu: {C_dau} mol/L\n")
        f_ot.write(f"Nồng độ cuối cùng: {C_cuoi} mol/L\n")
        f_ot.write(f"Thời gian phản ứng: {sum_time} giây\n")
    print("Đã phân tích xong vào kiểm tra file đi nào!")
    plt.show()
    
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file phản ứng K?")
except ValueError:
    print("Lỗi: Dữ liệu trong file bị sai định dạng hoặc không tồn tại!")


