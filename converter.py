import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("converter")
window.geometry("300x150")

# title
title_label = tk.Label(master = window, text = "miles to kilometers", font = "Calibri 24 bold")
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = "convert")
entry.pack()
button.pack()
input_frame.pack()

# run
window.mainloop()