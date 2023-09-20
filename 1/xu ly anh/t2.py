import cv2
import numpy as np

# Sử dụng cv2.imread() để đọc hình ảnh
image = cv2.imread('./xu ly anh/data/3.png')

if image is not None:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding or any other preprocessing as needed

    # Apply the Watershed Algorithm
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    sure_fg = cv2.dilate(thresh, None, iterations=3)

    # Find markers for the objects to be segmented
    markers = cv2.connectedComponents(sure_fg)[1]
    markers = markers + 1
    markers[thresh == 255] = 0

    cv2.watershed(image, markers)
    image[markers == -1] = [100, 1, 255]  # Mark segmented objects in red

    cv2.imshow('Segmented Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Unable to load the image.")
