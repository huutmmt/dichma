import cv2
import dlib
import numpy as np

# Khởi tạo webcam hoặc thiết bị ghi hình video (thay đổi index nếu cần)
cap = cv2.VideoCapture(0)

crown_image = cv2.imread('image/pngegg.png', -1)

# Kiểm tra xem webcam có hoạt động hay không
if not cap.isOpened():
    print("Không thể mở webcam hoặc thiết bị ghi hình video.")
    exit()

# Thiết lập kích thước khung hình
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Tạo VideoWriter để lưu video đầu ra
out = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (frame_width, frame_height))

# Khởi tạo bộ phát hiện khuôn mặt
face_detector = dlib.get_frontal_face_detector()

# Khởi tạo dlib facial landmarks predictor
landmarks_predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Chuyển đổi video sang đen trắng để tăng tốc độ xử lý
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Phát hiện khuôn mặt trong khung hình
    faces = face_detector(gray)

    for face in faces:
        # Xác định vị trí của khuôn mặt
        x, y, w, h = face.left(), face.top(), face.width(), face.height()

        # Tính toán vị trí cho vương miện (ví dụ: giữa đầu)
        crown_x = x + w // 2 - crown_image.shape[1] // 2
        crown_y = y - crown_image.shape[0]

        # Đảm bảo vương miện không vượt ra khỏi video
        if crown_x < 0:
            crown_x = 0
        if crown_y < 0:
            crown_y = 0

        # Cắt ảnh vương miện nếu nó ra ngoài video
        if crown_x + crown_image.shape[1] > frame.shape[1]:
            crown_image = crown_image[:, :frame.shape[1] - crown_x]
        if crown_y + crown_image.shape[0] > frame.shape[0]:
            crown_image = crown_image[:frame.shape[0] - crown_y, :]

        # Thêm vương miện vào khung hình
        for c in range(0, 3):
            frame[crown_y:crown_y + crown_image.shape[0], crown_x:crown_x + crown_image.shape[1], c] = \
                frame[crown_y:crown_y + crown_image.shape[0], crown_x:crown_x + crown_image.shape[1], c] * \
                (1 - crown_image[:, :, 3] / 255.0) + \
                crown_image[:, :, c] * (crown_image[:, :, 3] / 255.0)

    # Ghi khung hình đã xử lý vào video đầu ra
    out.write(frame)

    # Hiển thị video trực tiếp
    cv2.imshow('AR Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng các tài nguyên
cap.release()
# out.release()
cv2.destroyAllWindows()
