import tkinter as tk
from tkinter import messagebox
import cv2
import numpy as np
from scipy import ndimage
# vertical shift
def shift_image(image, vertical_shift):
        translation_matrix = np.float32([[1, 0, 0], [0, 1, vertical_shift]])
        shifted_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
        return shifted_image
# high pass filter
def apply_high_pass_filter(image):
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image

        blurred = cv2.GaussianBlur(gray, (15, 15), 0)
        high_pass = cv2.subtract(gray, blurred)
        return high_pass
# convert to xyz
def convert_to_xyz(image):
        xyz_image = cv2.cvtColor(image, cv2.COLOR_BGR2XYZ)
        return xyz_image
# roberts cross
def roberts_cross(image):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gx = np.array([[1, 0], [0, -1]])
        gy = np.array([[0, 1], [-1, 0]])

        gradient_x = ndimage.convolve(img, gx)
        gradient_y = ndimage.convolve(img, gy)

        magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
        return magnitude

class OpenCVApp:
        def __init__(self, root, image):
            self.root = root
            self.root.title("Image Processor - OpenCV")
            self.root.geometry("600x600")
            self.root.configure(bg="light blue")
            self.image = image
            # Original image display
            '''self.original_image_label = tk.Label(root, text="Original Image", bg="light blue")
            self.original_image_label.pack()

            self.original_image_canvas = tk.Canvas(root, width=image.shape[1]//2, height=image.shape[0]//2, bg="black")
            self.original_image_canvas.pack()

            # self.display_image(self.image, self.original_image_canvas)

            # Processed image display
            self.processed_image_label = tk.Label(root, text="Processed Image", bg="light blue")
            self.processed_image_label.pack()

            self.processed_image_canvas = tk.Canvas(root, width=image.shape[1]//2, height=image.shape[0]//2, bg="black")
            self.processed_image_canvas.pack()'''

            # Data entry field for vertical offset
            self.shift_label = tk.Label(root, text="Enter the offset (in pixels):", bg = "light blue")
            self.shift_label.pack()

            self.shift_entry = tk.Entry(root, width=10)
            self.shift_entry.pack()

            # Buttons
            self.shift_button = tk.Button(root, text="Move Image", bg="pink", command=self.on_shift_button_click)
            self.shift_button.pack()

            self.high_pass_button = tk.Button(root, text="High Pass Filter",  bg="pink", command=self.on_high_pass_button_click)
            self.high_pass_button.pack()

            self.xyz_button = tk.Button(root, text="Convert to XYZ",  bg="pink", command=self.on_xyz_button_click)
            self.xyz_button.pack()

            self.roberts_button = tk.Button(root, text="Roberts Transform",  bg="pink", command=self.on_roberts_button_click)
            self.roberts_button.pack()

        def on_shift_button_click(self):
            try:
                vertical_shift = int(self.shift_entry.get())
            except ValueError:
                messagebox.showerror("Error", "Enter a valid numeric value for the offset")
                return

            shifted_image = shift_image(self.image, vertical_shift)
            cv2.imwrite('shifted.jpg', shifted_image)
            messagebox.showinfo("Success", "The shifted image is saved as 'shifted.jpg'.")

        def on_high_pass_button_click(self):
            filtered_image = apply_high_pass_filter(self.image)
            cv2.imwrite('filtered.jpg', filtered_image)
            messagebox.showinfo("Success", "The filtered image is saved as 'filtered.jpg'.")

        def on_xyz_button_click(self):
            xyz_image = convert_to_xyz(self.image)
            cv2.imwrite('xyz.jpg', xyz_image)
            messagebox.showinfo("Success", "An image in the XYZ color model is saved as 'xyz.jpg'.")

        def on_roberts_button_click(self):
            roberts_image = roberts_cross(self.image)
            cv2.imwrite('roberts.jpg', roberts_image)
            messagebox.showinfo("Success", "The image after Roberts Transform is saved as 'roberts.jpg'.")

if __name__ == "__main__":
        img = cv2.imread('Wall-e.jpg')

        if img is None:
            print("Error: Image not found. Check the file path.")
        else:
            root = tk.Tk()
            app = OpenCVApp(root, img)
            root.mainloop()
