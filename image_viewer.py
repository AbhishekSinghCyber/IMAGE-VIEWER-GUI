from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
import tkinter.messagebox as tmsg


root = Tk()
root.title("Image Viewer Application")
root.wm_attributes('-transparentcolor', 'red')
root.config(bg='red')
root.geometry("450x450")

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

def appli():
    tmsg.showinfo("About GUI", "This GUI Is Made In Python With The Help Of Tkinter And Pillow Library")

def developer():
    tmsg.showinfo("About Developer","Hello User,   I'm Abhishek Singh  the developer of this Image Viewer Application")

# MainMenu And Dropdown Menu
mainmenu = Menu(root)
mainmenu.add_command(label="About GUI", command=appli)
mainmenu.add_command(label="Developer", command=developer)
mainmenu.add_command(label="Exit", command=quit)

# Packing of menu
root.config(menu=mainmenu)


# Frame
f = Frame(root, bg='red')
f.pack(side=BOTTOM, padx=15, pady=8)


lbl = Label(root, text="Your Image Will Be Shown Here", width=35, bg="black", bd=180, fg="white", font=("lucida", 15))
lbl.pack()

button = Button(f, text="Select Image", width=15, bg='orange', bd=10, fg='blue', command=show_image)
button.pack(side=tk.LEFT)

button2 = Button(f, text="Exit", width=15, bg='orange', bd=10, fg='blue', command=lambda: exit())
button2.pack(side=tk.LEFT, padx=15)
root.mainloop()
