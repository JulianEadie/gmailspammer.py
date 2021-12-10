import tkinter as tk 
from tkinter import tkk


window = tk.Tk()

window.title("Python Tkinter Text Box")
window.minsize(600, 400)

def receiver_email():
    label.configure(text = 'Hello' + receiver_email.get())
    
label = ttk.Label(window, text = "Enter the receivers email)
label.grid(colomn = 0, row = 0)
                  
                  
                  
                  
receiver_email = tk.StringVar()
receiver_emailEntered = ttk.Entry(window, width = 15, textvariable = receiver_email)
receiver_emailEntered.grid(column = 0, row = 1)
                  

button = ttk.Button(window, text = "Enter", command = Enterpassword)
button.grid(column = 0, row = 1)
                  
window.mainloop()                  
