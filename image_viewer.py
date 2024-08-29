from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os


def show_image():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File",
                                          filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"),
                                                     ("All File", "everybody.txt")))
    if filename:
        img = Image.open(filename).resize((400, 400))
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img)
        lbl.image = img


root = Tk()

f = Frame(root, bg='red')
f.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

button = Button(f, text="Select Image", width=15, bg='orange', bd=10, fg='blue', command=show_image)
button.pack(side=tk.LEFT)

button2 = Button(f, text="Exit", width=15, bg='orange', bd=10, fg='blue', command=lambda: exit())
button2.pack(side=tk.LEFT, padx=15)
root.title("Image Viewer Application")
root.wm_attributes('-transparentcolor', 'red')
root.config(bg='red')
root.geometry("450x450")
root.mainloop()
