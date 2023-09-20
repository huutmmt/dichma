import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageSmoothingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Smoothing App")

        self.canvas = tk.Canvas(root, width=640, height=480)
        self.canvas.pack()

        self.load_button = tk.Button(root, text="Chọn ảnh", command=self.load_image)
        self.load_button.pack()

        self.smooth_button = tk.Button(root, text="Làm mịn ảnh", command=self.smooth_image, state=tk.DISABLED)
        self.smooth_button.pack()

        self.save_button = tk.Button(root, text="Lưu ảnh", command=self.save_image, state=tk.DISABLED)
        self.save_button.pack()

        self.image = None
        self.photo = None

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()
            self.smooth_button.config(state=tk.NORMAL)

    def smooth_image(self):
        if self.image:
            try:
                # Chuyển ảnh thành numpy array
                image_array = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)

                # Áp dụng bộ lọc Gaussian Blur để làm mịn ảnh
                smoothed_image_array = cv2.GaussianBlur(image_array, (5, 5), 0)

                # Chuyển lại thành định dạng PIL Image
                smoothed_image = Image.fromarray(cv2.cvtColor(smoothed_image_array, cv2.COLOR_BGR2RGB))

                self.image = smoothed_image
                self.display_image()
                self.save_button.config(state=tk.NORMAL)
            except Exception as e:
                messagebox.showerror("Lỗi", "Có lỗi xảy ra khi làm mịn ảnh: " + str(e))

    def save_image(self):
        if self.image:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
            if file_path:
                try:
                    self.image.save(file_path)
                    messagebox.showinfo("Thành công", "Lưu ảnh thành công!")
                except Exception as e:
                    messagebox.showerror("Lỗi", "Có lỗi xảy ra khi lưu ảnh: " + str(e))

    def display_image(self):
        if self.image:
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSmoothingApp(root)
    root.mainloop()
