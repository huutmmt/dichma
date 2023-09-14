import cv2

# Đọc ảnh
image1 = cv2.imread('./xu ly anh/data/3.png')
image2 = cv2.imread('./xu ly anh/data/4.png')

# Tạo đối tượng Stitcher (nối ảnh)
stitcher = cv2.Stitcher.create()

# Nối hai ảnh
status, anhketqua = stitcher.stitch((image1, image2))

# Kiểm tra việc nối thành công hay không
if status == cv2.Stitcher_OK:
    panorama = anhketqua
    cv2.imwrite('anhtoancanh.jpg', panorama)
    cv2.imshow('Ảnh toàn cảnh', panorama)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('Không thể nối ảnh')
