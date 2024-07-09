import random
import string
import tkinter as tk

def generate_password(length):
    return ''.join(random.choice(string.ascii_letters + string.digits+ string.punctuation ) for _ in range(length))

def on_click():
    try:
        length = int(entry.get())
        if length < 8:
            label2 = tk.Label(layout, text="Password length must be at least 8 characters", bg="light blue")
            label2.pack()
            
            return
    except Exception as e:
        label2 = tk.Label(layout, text=f"Invalid input", bg="light blue")
        label2.pack()
        return    
            
    
    for widget in layout.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text").startswith("Password:"):
            widget.destroy()
    password = generate_password(length)
    label2 = tk.Label(layout, text="Password: " + password, bg="light blue")
    label2.pack()


layout= tk.Tk()
layout.title("Password Generator")  
layout.geometry("400x500")
layout.configure(bg="light blue")
label = tk.Label(layout, text="Enter the length of the password: ", bg="light blue")
label.pack()
entry = tk.Entry(layout)
entry.pack()
button = tk.Button(layout, text="Generate", command=on_click)
button.pack()
layout.mainloop()


