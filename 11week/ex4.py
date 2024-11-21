import qrcode 

이름 = input("이름을 입력하시오:")
학번 = input("학번을 입력하시오:")
전공 = input("전공을 입력하시오:")
qr_data = f"{이름}, {학번}, {전공}"
qr_img = qrcode.make(qr_data)

save_path = 'my_info_data.png'
qr_img.save(save_path)