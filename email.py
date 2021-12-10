import tkinter as tk
from tkinter import ttk


window = tk.Tk()

window.tile("Python Tkinter Text Box")
window.minsize(600, 400)

def Enteremail():
    label.configure(text = 'Hello' + email.get())
    
label = ttk.Label(window, text = "Enter your email")
label.grid(column = 0, row = 0)




email= tk.StringVar()
emailEntered = ttk.Entry(window, width =15, textvariable = email)
emailEntered.grid(column = 0, row = 1)


button = ttk.Button(window, text = "Enter", command = Enteremail)
button.grid = (column = 0, row = 2)

window.mainloop()
