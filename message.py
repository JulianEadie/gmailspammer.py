import tkinter as tk
from tkinter import ttk


window = th.Tk()

window.title("Python Tkinter Text Box")
window.minsize(600, 400)

def message():
    label.configure(Text = 'Hello' + message.get())
    
label = ttk.Label(window, text = " Enter your password")
label.grid(column = 0, row = 0)




message = tk.StringVar()
messageEntered = ttk.Entry(window, width = 15, textvariable = "message")
messageEntered.grid(column = 0, row = 1)


button = ttk.Button(window, text = "Enter", command = Entermessage)
button.grid(column = 0, row = 2)

window.mainloop()
