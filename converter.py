import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
from PIL import Image, ImageTk

# window
window = ttk.Window(themename = "darkly")
window.title("converter")
window.geometry("400x200")

# global variables
title_text = "miles to kilometers"
mi_to_km = True

# functions
def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

def switch_conversion():
    global mi_to_km
    if mi_to_km == True:
        mi_to_km = False
        title_text.set("kilometers to miles")
    else:
        mi_to_km = True
        title_text.set("miles to kilometers")
    print("switch conversion")

# title
title_text = tk.StringVar(value = "miles to kilometers")
title_label = tk.Label(master = window, textvariable = title_text, font = "Calibri 24 bold")
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)

entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)

button = ttk.Button(master = input_frame, text = "convert", command = convert)

image = Image.open("assets/conversion.png")
scaled_image = image.resize((20, 20), Image.Resampling.BOX)
photo = ImageTk.PhotoImage(scaled_image)
image_button = ttk.Button(master = input_frame, image = photo, command = switch_conversion)

entry.pack(side = "left", padx = 10)
image_button.pack(side = "left")
button.pack(side = "left", padx = 10)
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = tk.Label(master = window, text = "output", font = "Calibri 24", textvariable = output_string)
output_label.pack()

# run
window.mainloop()