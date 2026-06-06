import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageOps, ImageTk
from colorthief import ColorThief
import os
from webcolors import rgb_to_hex
import pyperclip


#-------------------FUNCTIONS----------------------#
def on_label_click(labelElem):
    pyperclip.copy(labelElem["text"])
    copied_label.config(text="✅ Copied!")
    root.after(1000, lambda: copied_label.config(text=""))

def open_image():
    allowed = [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"]
    image_filters = [
        ("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff"),
        ("PNG Files", "*.png"),
        ("JPEG Files", "*.jpg *.jpeg"),
        ("All Files", "*.*")
    ]
    img_path = filedialog.askopenfilename(filetypes=image_filters)

    if not img_path:
        return
    ext = os.path.splitext(img_path)[1].lower()
    if ext not in allowed:
        messagebox.showwarning("Invalid File", f"'{ext}' is not a supported format!")
        return

    upload_img_btn.place_forget()

    original_im = Image.open(img_path)
    original_im = ImageOps.exif_transpose(original_im)

    root.update()
    w = image_card.winfo_width()
    h = image_card.winfo_height()

    display_im = original_im.copy()
    display_im.thumbnail((w, h), Image.LANCZOS)

    photo = ImageTk.PhotoImage(display_im)
    panel.config(image=photo)
    panel.image = photo

    change_img_btn.place(relx=0.3, rely=0.93)

    generate_colors(img_path)

def generate_colors(img_path):
    color_thief = ColorThief(img_path)

    dominant_rgb = color_thief.get_color(quality=1)
    dominant_hex = rgb_to_hex(dominant_rgb)
    dominant_btn.config(bg=dominant_hex , activebackground=dominant_hex, command=lambda h=dominant_hex, r=dominant_rgb: display_codes(h, r))

    rgb_pallete = color_thief.get_palette(color_count=11, quality=1)
    for index, rgb in enumerate(rgb_pallete):
        hex_pallete = rgb_to_hex(rgb)
        if index >= len(color_btns):
            break
        if hex_pallete == dominant_hex:
            continue
        else:
            color_btns[index].config(bg=hex_pallete, activebackground=hex_pallete,command=lambda h=hex_pallete, r=rgb: display_codes(h, r))
            index += 1

def display_codes(hex, rgb):
    hex_value_label.config(text=hex)
    rgb__value_label.config(text=str(rgb))


#------------------UI-----------------#
root = tk.Tk()
root.title("Custom Color Palette")
root.geometry("1200x800")
root.configure(bg="#121358")

title = tk.Label(root, text="Color Palette Generator", font=("Comic Sans MS",40,"bold"), bg="#121358",fg="#F1FF5E")
title.pack(pady=30)

image_card = tk.Frame(root, bg="whitesmoke", padx=40, pady=40)
image_card.place(relx=0.35, rely=0.55, anchor="center", width=850, height=750)

change_img_btn = tk.Button(root, text="Change Image", font=("Comic Sans MS", 18, "bold"), bg="snow", fg="black", relief="flat", command=open_image)

panel = tk.Label(image_card, bg="whitesmoke")
panel.place(relx=0.5, rely=0.5, anchor="center")

pallete_card = tk.Frame(root, bg="whitesmoke", padx=40, pady=40)
pallete_card.place(relx=0.75, rely=0.55, anchor="center", width=520, height=750)

upload_img_btn = tk.Button(image_card, text="Upload Image", font=("Comic Sans MS",20,"bold"),command=open_image)
upload_img_btn.place(relx=0.4, rely=0.4)

dominant_btn = tk.Button(
            pallete_card,
            bg="gray",
            activebackground="black",
            width=60,
            height=3,
            relief="flat",
    )
dominant_btn.grid(row=0,column=0,columnspan=3,pady=20)

columns = 3
color_btns = []
for index in range(9):
    row = index // columns
    col = index % columns
    color_btn = tk.Button(
        pallete_card,
        bg="gray",
        activebackground="black",
        width=17,
        height=8,
        relief="flat",
    )
    color_btn.grid(row=row + 1, column=col, padx=10, pady=7)
    color_btns.append(color_btn)

info_frame = tk.Frame(pallete_card, bg="whitesmoke")
info_frame.place(relx=0.5, rely=0.9, anchor="center")

rgb_label = tk.Label(info_frame, text="rgb:" , font=("Comic Sans MS",20,"bold"), bg="whitesmoke", fg="red")
rgb_label.grid(row=0, column=0, pady=5)

rgb__value_label = tk.Label(info_frame, text="xxx" , font=("Comic Sans MS",20,"bold"), bg="whitesmoke", fg="black")
rgb__value_label.grid(row=0, column=1, pady=5)
rgb__value_label.bind("<Button-1>", lambda event: on_label_click(rgb__value_label))

hex_label = tk.Label(info_frame, text="hex code:" , font=("Comic Sans MS",20,"bold"), bg="whitesmoke", fg="green")
hex_label.grid(row=1, column=0, pady=5)

hex_value_label = tk.Label(info_frame, text="xxx" , font=("Comic Sans MS",20,"bold"), bg="whitesmoke", fg="black")
hex_value_label.grid(row=1, column=1, pady=5)
hex_value_label.bind("<Button-1>", lambda event: on_label_click(hex_value_label))

copied_label = tk.Label(info_frame, text="", fg="green",bg="whitesmoke" ,font=("Comic Sans MS", 12))
copied_label.grid(row=2, column=1)

root.mainloop()
