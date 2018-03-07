from Tkinter import *
from tkFileDialog import *
import ttk
import Tkinter as tk
#import py2exe
from eppy import modeleditor
from eppy.modeleditor import IDF
from PIL import Image, ImageTk
from openpyxl import *
try:
    # python 2
    from tkFont import Font
except ImportError:
    # python 3
    from tkinter.font import Font

import Tkinter
import tkMessageBox


root = tk.Tk()
def make_button():
    b = tk.Button(root)
    imagebt = ImageTk.PhotoImage(file="info.png")
    b.config(image=image,background='white')
    b.image = image
    b.pack()
make_button()
root.mainloop()