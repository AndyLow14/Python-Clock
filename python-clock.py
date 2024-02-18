# import required modules
from configparser import ConfigParser
from datetime import datetime
import tkinter as tk

from time import strftime

PRISM_UW = 3500

# Tkinter Window
window = tk.Tk()
window.geometry('740x250+'+ str(PRISM_UW) +'+400')
window.title("PyClock")
window.configure(background='black', pady=15)
window.overrideredirect(True)

def time():
    string = strftime('%I | %M | %S %p')
    time_label.config(text=string)
    time_label.after(1000, time)

def date():
    string = strftime('%a, %d %b %Y       W%W  D%j')
    date_label.config(text=string)
    date_label.after(1000, time)

# UI
time_label = tk.Label(window, font=('Minecraftia', 60), background='black', foreground='white')
date_label = tk.Label(window, font=('Minecraftia', 26), background='black', foreground='white')
 
time_label.pack()
date_label.pack()

time() 
date()

tk.mainloop()