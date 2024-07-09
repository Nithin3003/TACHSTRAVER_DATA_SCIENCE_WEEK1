import tkinter as TK
import qrcode
import os

def on_click():
    url = entry.get()
    qr = qrcode.make(url)
    qr.save("qrcode.png","PNG")
    label2 = TK.Label(layout, text="QR code generated, opening...", bg="light blue")
    label2.pack()
    os.system("qrcode.png")

layout = TK.Tk()
layout.title("QR Code Generator")
layout.geometry("400x500")
layout.configure(bg="light blue")
label = TK.Label(layout, text="Enter the URL: ", bg="light blue")
label.pack()
entry = TK.Entry(layout)
entry.configure(width=int(layout.winfo_width() * 50))
entry.insert(0, "https://www.codedpad.me")
entry.pack()
button = TK.Button(layout, text="Generate", command=on_click, cursor="hand2", compound="right")
button.pack()
layout.mainloop()

