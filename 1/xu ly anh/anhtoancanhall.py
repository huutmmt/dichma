import cv2
import numpy as np
import os
#Đọc ảnh
#Để thực hiện nối nhiều ảnh thành 1 ảnh toàn cảnh
# Các ảnh cần nối được đặt trong 1 thư mục
duongdan='xu ly anh/data/'
#Kiểm tra thư mục có tồn tại không, nếu có lấy tất cả các file
if os.path.exists(duongdan):
    danhsachfile=os.listdir(duongdan)
    dsanh=[]
    #Lặp qua ds file và đọc các file ảnh
    for tenfile in danhsachfile:
        if tenfile.lower().endswith(('.jpg','.png','.jpeg','.bmp','.gif')):
            #đường dẫn đầy đủ đến file
            duongdanfile=os.path.join(duongdan,tenfile)
            #Đọc ảnh
            image=cv2.imread(duongdanfile)
            if image is not None:
                dsanh.append(image)
    stitcher=cv2.Stitcher.create()
    status,panoimage=stitcher.stitch(dsanh)

    if status!=cv2.Stitcher_OK:
        print('Khong the noi anh, loi: %d'%status)
    else:
        cv2.imwrite('data/panorama_kq.jpg',panoimage)
        print('Noi anh thanh cong')
        cv2.imshow('Anh toan canh',panoimage)
        cv2.waitKey()
        cv2.destroyAllWindows()
