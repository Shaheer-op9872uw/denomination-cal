from tkinter import Tk, Label, Button, CENTER
from tkinter import messagebox
from PIL import Image, ImageTk  
root = Tk()
root.title("dem cal")
root.configure(bg='dark blue')
root.geometry("800x600")
upload = Image.open("app_img.jpg")
upload = upload.resize((800, 600))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='dark blue')
label.place(x=180,y=20)
label = Label(root,
        text="Welcome to the calculator app", font=("Arial", 20), bg='dark blue', fg='white')
label.place(relx=0.5, y=340, anchor=CENTER)
def msg():
    MagBox= messagebox.showinfo(
        "Alert","do ya wana cal the dom count")
    if MagBox == "ok":
        topwin()
button1 = Button(root,
                 text="Click to start the calculator",
                 command=msg,
                 bg='brown',
                 fg='white',
                 font=("Arial", 15))
button1.place(x=260, y=360)
def topwin():
    top = Toplevel(root)
    top.title("Calculator")
    top.geometry("400x500")

label = Label(top, text="enter total value",bg='light grey')    
entry = Entry(top)
lbl = Label(top, text="enter no of notes",bg='purple')


l1 = Label(top, text= "2000", bg = 'light grey')
l2 = Label(top, text= "500", bg = 'light grey')
l1 = Label(top, text= "100", bg = 'light grey')

t1 = Entry(top)
t2 = Entry(top) 
t3 = Entry(top)