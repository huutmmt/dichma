import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Định nghĩa các hàm chỉnh sửa ảnh
def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def blur_image(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

def edge_detection(image):
    return cv2.Canny(image, 100, 200)

def resize_image(image, width, height):
    return cv2.resize(image, (width, height))

# Tạo danh sách chức năng chỉnh sửa ảnh
image_editing_functions = {
    "Grayscale": convert_to_grayscale,
    "Blur": blur_image,
    "Edge Detection": edge_detection,
    "Resize": resize_image
}

# Hàm để chuyển đổi mảng numpy thành đối tượng hình ảnh Tkinter
def convert_numpy_to_photoimage(numpy_array):
    pil_image = Image.fromarray(numpy_array)
    return ImageTk.PhotoImage(pil_image)

# Hàm để cập nhật canvas với ảnh mới
def update_canvas_with_image(image_array, canvas):
    photo_image = convert_numpy_to_photoimage(image_array)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo_image)
    canvas.photo = photo_image

# Hàm để chọn chức năng chỉnh sửa ảnh dựa trên lựa chọn của người dùng
def apply_selected_function():
    selected_function = editing_function_var.get()
    if selected_function and selected_function in image_editing_functions:
        image = image_editing_functions[selected_function](original_image.copy())
        update_canvas_with_image(image, edited_image_canvas)

# Hàm để mở ảnh từ tệp
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if file_path:
        global original_image
        original_image = cv2.imread(file_path)
        update_canvas_with_image(original_image.copy(), original_image_canvas)
        update_canvas_with_image(original_image.copy(), edited_image_canvas)

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Image Editor")

# Tạo thanh menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_image)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Tạo hai canvas để hiển thị ảnh gốc và ảnh đã chỉnh sửa
original_image_canvas = tk.Canvas(root, width=400, height=600)
original_image_canvas.pack(side=tk.LEFT)

edited_image_canvas = tk.Canvas(root, width=400, height=600)
edited_image_canvas.pack(side=tk.RIGHT)

# Tạo phần tử hộp chọn để chọn chức năng chỉnh sửa ảnh
editing_function_var = tk.StringVar()
editing_function_var.set("Grayscale")  # Mặc định chọn Grayscale
editing_function_optionmenu = tk.OptionMenu(root, editing_function_var, *image_editing_functions.keys())
editing_function_optionmenu.pack()

# Tạo nút để áp dụng chức năng chỉnh sửa ảnh
apply_button = tk.Button(root, text="Apply", command=apply_selected_function)
apply_button.pack()

# Khởi tạo biến lưu ảnh gốc
original_image = None

# Chạy ứng dụng
root.mainloop()
