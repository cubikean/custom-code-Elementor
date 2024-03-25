from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import re

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    return "#{:02x}{:02x}{:02x}".format(rgb_color[0], rgb_color[1], rgb_color[2])

def replace_color(image_path, target_color, replacement_color, tolerance):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    for x in range(width):
        for y in range(height):
            current_color = pixels[x, y]
            if color_similarity(current_color, target_color) <= tolerance:
                pixels[x, y] = replacement_color

    output_path = "output.png"
    img.save(output_path)
    return output_path

def color_similarity(color1, color2):
    return sum((a - b) ** 2 for a, b in zip(color1, color2)) ** 0.5

def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    entry_file_path.delete(0, END)
    entry_file_path.insert(0, file_path)

def apply_color_change():
    file_path = entry_file_path.get()
    target_color = get_color_from_entry(entry_target_color)
    replacement_color = get_color_from_entry(entry_replacement_color)
    tolerance = float(entry_tolerance.get())

    if file_path and target_color and replacement_color:
        output_path = replace_color(file_path, target_color, replacement_color, tolerance)
        lbl_status.config(text=f"Color replacement complete. Saved as {output_path}")
    else:
        lbl_status.config(text="Error: Please fill in all the fields.")

def get_color_from_entry(entry_widget):
    color_string = entry_widget.get()
    if re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color_string):  # Check if it's a valid hex color
        return hex_to_rgb(color_string)
    elif re.match(r'^\d+,\s?\d+,\s?\d+$', color_string):  # Check if it's a valid RGB color
        return tuple(map(int, color_string.split(',')))
    else:
        return None

# GUI
root = Tk()
root.title("Color Replacement")

# File selection
lbl_file_path = Label(root, text="Select PNG file:")
lbl_file_path.grid(row=0, column=0, padx=10, pady=10)
entry_file_path = Entry(root, width=40)
entry_file_path.grid(row=0, column=1, padx=10, pady=10)
btn_choose_file = Button(root, text="Browse", command=choose_file)
btn_choose_file.grid(row=0, column=2, padx=10, pady=10)

# Target color
lbl_target_color = Label(root, text="Target color (Hex or R,G,B):")
lbl_target_color.grid(row=1, column=0, padx=10, pady=10)
entry_target_color = Entry(root, width=20)
entry_target_color.grid(row=1, column=1, padx=10, pady=10)

# Replacement color
lbl_replacement_color = Label(root, text="Replacement color (Hex or R,G,B):")
lbl_replacement_color.grid(row=2, column=0, padx=10, pady=10)
entry_replacement_color = Entry(root, width=20)
entry_replacement_color.grid(row=2, column=1, padx=10, pady=10)

# Tolerance
lbl_tolerance = Label(root, text="Color tolerance:")
lbl_tolerance.grid(row=3, column=0, padx=10, pady=10)
entry_tolerance = Entry(root, width=10)
entry_tolerance.grid(row=3, column=1, padx=10, pady=10)

# Apply button
btn_apply = Button(root, text="Apply Color Change", command=apply_color_change)
btn_apply.grid(row=4, column=1, pady=20)

# Status label
lbl_status = Label(root, text="")
lbl_status.grid(row=5, column=1)

root.mainloop()
