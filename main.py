from PIL import Image
from tkinter import Tk, Button, Label, filedialog, simpledialog, messagebox
from tkinter.filedialog import askopenfilenames

def convert_image():
    input_files = filedialog.askopenfilenames(title="Select Input Files", filetypes=[("Image Files", (".jpg", ".jpeg", ".png", ".bmp", ".webp", ".gif", ".avi"))])
    if input_files:
        output_format = simpledialog.askstring("Input", "Enter output format (e.g., PNG, JPEG, BMP, WebP, GIF)", initialvalue="PNG")
        if output_format:
            for input_file in input_files:
                try:
                    with Image.open(input_file) as img:
                        # Add resizing option
                        width, height = img.size
                        resize_option = simpledialog.askstring("Input", "Enter new width and height (e.g., 800 600)", initialvalue=f"{width} {height}")
                        if resize_option:
                            width, height = map(int, resize_option.split())
                            img = img.resize((width, height))
                        # Add rotation option
                        rotation_option = simpledialog.askstring("Input", "Enter rotation (0, 90, 180, 270)", initialvalue="0")
                        if rotation_option:
                            img = img.rotate(int(rotation_option))
                        # Add flipping option
                        flip_option = simpledialog.askstring("Input", "Flip (H)orizontal or (V)ertical?", initialvalue="N")
                        if flip_option.upper() == "H":
                            img = img.transpose(Image.FLIP_LEFT_RIGHT)
                        elif flip_option.upper() == "V":
                            img = img.transpose(Image.FLIP_TOP_BOTTOM)
                        # Save the image in the specified format
                        output_file = input_file.split('.')[0] + '.' + output_format.lower()
                        img.save(output_file, output_format.upper())
                    print(f"Image converted successfully from {input_file} to {output_file}")
                except Exception as e:
                    print(f"An error occurred: {str(e)}")

def batch_convert():
    input_files = filedialog.askopenfilenames(title="Select Input Files", filetypes=[("Image Files", (".jpg", ".jpeg", ".png", ".bmp", ".webp", ".gif", ".avi"))])
    if input_files:
        output_format = simpledialog.askstring("Input", "Enter output format (e.g., PNG, JPEG, BMP, WebP, GIF)", initialvalue="PNG")
        if output_format:
            for input_file in input_files:
                try:
                    with Image.open(input_file) as img:
                        # Add resizing option
                        width, height = img.size
                        resize_option = simpledialog.askstring("Input", "Enter new width and height (e.g., 800 600)", initialvalue=f"{width} {height}")
                        if resize_option:
                            width, height = map(int, resize_option.split())
                            img = img.resize((width, height))
                        # Add rotation option
                        rotation_option = simpledialog.askstring("Input", "Enter rotation (0, 90, 180, 270)", initialvalue="0")
                        if rotation_option:
                            img = img.rotate(int(rotation_option))
                        # Add flipping option
                        flip_option = simpledialog.askstring("Input", "Flip (H)orizontal or (V)ertical?", initialvalue="N")
                        if flip_option.upper() == "H":
                            img = img.transpose(Image.FLIP_LEFT_RIGHT)
                        elif flip_option.upper() == "V":
                            img = img.transpose(Image.FLIP_TOP_BOTTOM)
                        # Save the image in the specified format
                        output_file = input_file.split('.')[0] + '.' + output_format.lower()
                        img.save(output_file, output_format.upper())
                except Exception as e:
                    print(f"An error occurred: {str(e)}")

def settings():
    settings_window = Tk()
    settings_window.title("Settings")
    settings_window.geometry("200x150")

def save_settings():
        # ... (save settings code)

    btn_save = Button(settings_window, text="Save", command=save_settings)
    btn_save.pack(pady=20)

    settings_window.mainloop()

def history():
    history_window = Tk()
    history_window.title("History")
    history_window.geometry("200x150")

def clear_history():
        # ... (clear history code)

    btn_clear = Button(history_window, text="Clear", command=clear_history)
    btn_clear.pack(pady=20)

    history_window.mainloop()

root = Tk()
root.title("Image Converter")
root.geometry("300x250")

btn_convert = Button(root, text="Convert Image", command=convert_image)
btn_convert.pack(pady=20)

btn_batch_convert = Button(root, text="Batch Convert", command=batch_convert)
btn_batch_convert.pack(pady=20)

btn_settings = Button(root, text="Settings", command=settings)
btn_settings.pack(pady=20)

btn_history = Button(root, text="History", command=history)
btn_history.pack(pady=20)

root.mainloop()
