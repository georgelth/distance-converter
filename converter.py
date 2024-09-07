import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("converter")
window.geometry("300x150")

# title
title_label = tk.Label(master = window, text = "miles to kilometers", font = "Calibri 24 bold")
title_label.pack()

# run
window.mainloop()