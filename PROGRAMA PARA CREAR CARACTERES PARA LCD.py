import tkinter as tk

def toggle_pixel(pixel):
    if pixel["bg"] == "white":
        pixel.config(bg="green")
    else:
        pixel.config(bg="white")
    update_binary()

def update_binary():
    binary_str = "//www.youtube.com/@electro_arduino\n"
    binary_str += "//SUSCRIBETE\n"
    binary_str += "#include <LiquidCrystal.h>\n"
    binary_str += "LiquidCrystal lcd(12, 11, 5, 4, 3, 2); // RS, E, D4, D5, D6, D7\n\n"
    binary_str += "byte nombre[] = {\n"
    
    for row in range(8):
        row_binary = ""
        for col in range(5):
            if pixels[row][col]["bg"] == "white":
                row_binary += "0"
            else:
                row_binary += "1"
        binary_str += "    0b" + row_binary
        if row < 7:
            binary_str += ",\n"
        else:
            binary_str += "\n"
    binary_str += "}"
    binary_text.delete("1.0", tk.END)
    binary_text.insert(tk.END, binary_str)

# Crear la ventana
root = tk.Tk()
root.title("Creador de caracteres by @electro_arduino")

# Crear los pixels
pixels = []
for row in range(8):
    pixel_row = []
    for col in range(5):
        pixel = tk.Button(root, width=2, height=1, bg="white", command=lambda r=row, c=col: toggle_pixel(pixels[r][c]))
        pixel.grid(row=row, column=col, padx=1, pady=1)
        pixel_row.append(pixel)
    pixels.append(pixel_row)

# Crear la caja de texto para el código binario

binary_text = tk.Text(root, width=40, height=15)
binary_text.grid(row=0, column=5, rowspan=8, padx=10, pady=10)

# Iniciar la ventana

root.mainloop()
