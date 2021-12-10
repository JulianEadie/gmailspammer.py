import tkinter as tk
from tkinter import tkk


window = tk.Tk()

window.tile("Python Tkinter Text Box")
window.minsize(600, 400)

def password():
    label.configure(text = 'Hello' + password.get())
    
label = ttk.Label(window, text = "Enter your email password")
label.grid(column = 0, row = 0)




password = tk.StringVar()
passwordEntered = ttk.Entry(window, width = 15, textvariable = password)
passwordEntered.grid(column = 0, row = 1)


button = ttk.Button(window, text = "Enter", command = Enterpassword)
button.grid(column = 0, row = 2)

window.mainloop()
