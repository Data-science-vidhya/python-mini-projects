import pyqrcode
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image,ImageTk

win = Tk()
win.title("QR Code Generator")
win.config(background='#fed304')

text=ttk.Label(win,text= "Enter text or link")
text.grid(row=0,column=0,padx=3,pady=3)

data = ttk.Entry(win,width=40)
data.grid(row=0, column=1, padx=3,pady=3)

button = ttk.Button(win,text="Generate", command=generate())
button.grid(row=0,column=2,padx=3, pady=3)

show_qr = ttk.Label(win, text= "QR Code :")
show_qr.grid(row=1, column=0,padx=3,pady=3)

win.imagelabel = ttk.Label(win,background= '#fed304')
win.imagelabel.grid(row=2,column=0,padx=3, pady=3, columnspan=3)

win.mainloop()

def generate():
    text = data.get()
    qr = pyqrcode.create(text)
    file_name = "QR code"
    save_path = "D:\AI\Image processing and cnn stuff\prectice of open cv\4\ "
    name = save_path+file_name+ '.png'
    qr.png(name,scale=10)
    image = Image.open(name)
    image = image.resize((400,400), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    win.imagelabel.config(image=image)
    win.imagelabel.photo = image