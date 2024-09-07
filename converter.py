import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
from PIL import Image, ImageTk

# window
window = ttk.Window(themename = "darkly")
window.title("converter")
window.geometry("400x200")

# functions
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

def switch_conversion():
    print("switch conversion")

# title
title_label = tk.Label(master = window, text = "miles to kilometers", font = "Calibri 24 bold")
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)

entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = "convert", command = convert)

image = Image.open("assets/conversion.png")
photo = ImageTk.PhotoImage(image)
image_button = ttk.Button(master = input_frame, image = photo, command = switch_conversion)

entry.pack(side = "left", padx = 10)
image_button.pack(side = "left")
button.pack(side = "left")
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = tk.Label(master = window, text = "output", font = "Calibri 24", textvariable = output_string)
output_label.pack()

# run
window.mainloop()