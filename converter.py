import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

# window
window = tk.Tk()
window.title("converter")
window.geometry("300x150")

# convert
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

# title
title_label = tk.Label(master = window, text = "miles to kilometers", font = "Calibri 24 bold")
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "convert", command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = tk.Label(master = window, text = "output", font = "Calibri 24", textvariable = output_string)
output_label.pack()

# run
window.mainloop()