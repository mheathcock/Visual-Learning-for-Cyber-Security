# Your main script

import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk
import create_arrows
import image_loader

app = CTk()
app.geometry("1920x1080")

set_appearance_mode("light")

right_arrow = Image.open("arrowR.png")
left_arrow = Image.open("arrow2.png")

image = Image.open("background.png")
background_image = CTkImage(image, size=(1920, 1080))

current_page_index = -1

images = [
    {"name": "Page 1", "image_paths": ["a2.png", "a1.png"]},
    {"name": "Page 2", "image_paths": ["neiman.png", "tutorialthing.png"]},
]

current_image_index = 0

for page in images:
    page["image_paths"] = [f"{image_path}" for image_path in page["image_paths"]]

def resize_image(original_image, new_width, new_height):
    resized_img = original_image.resize((new_width, new_height))
    return ImageTk.PhotoImage(resized_img)

def bg_resizer(e):
    if e.widget is app:
        i = CTkImage(image, size=(e.width, e.height))
        bg_lbl.configure(text="", image=i)

bg_lbl = CTkLabel(app, text="", image=background_image)
bg_lbl.place(x=0, y=0)

button_image_width = 100
button_image_height = 100

resized_img_right_arrow = resize_image(right_arrow, button_image_width, button_image_height)
resized_img_left = resize_image(left_arrow, button_image_width, button_image_height)

def Page1ButtonClick():
    global current_page_index
    current_page_index = 0
    update_buttons()

def Page2ButtonClick():
    global current_page_index
    current_page_index = 1
    update_buttons()

def BackButtonClick():
    global current_page_index
    current_page_index = -1
    hide_arrows()
    update_buttons()

def update_buttons():
    create_arrows.create_arrows(app, resized_img_right_arrow, resized_img_left,
                                button_image_height, button_image_width, images)

    for btn in [Page1btn, Page2btn, Backbtn]:
        btn.place_forget()

    if current_page_index == -1:
        Page1btn.place(relx=0.5, rely=0.5, anchor="center")
        Page2btn.place(relx=0.5, rely=0.2, anchor="center")
    else:
        create_arrows.update_arrow_positions(app, button_image_height, button_image_width)
        Backbtn.place(relx=0.2, rely=0.2, anchor="center")

# Declare buttons
Page1btn = CTkButton(master=app, text="Click", corner_radius=32, text_color="#000000", bg_color="#F3E5E1",
                     fg_color="transparent", hover_color="#4158D0", border_color="#FFCC70", border_width=2,
                     command=Page1ButtonClick)

Page2btn = CTkButton(master=app, text="Click", corner_radius=32, text_color="#000000", bg_color="#F3E5E1",
                     fg_color="transparent", hover_color="#4158D0", border_color="#FFCC70", border_width=2,
                     command=Page2ButtonClick)

Backbtn = CTkButton(master=app, text="Back", corner_radius=32, text_color="#000000", bg_color="#F3E5E1",
                    fg_color="transparent", hover_color="#4158D0", border_color="#FFCC70", border_width=2,
                    command=BackButtonClick)

# Initialize images and buttons
bg_lbl = CTkLabel(app, text="", image=background_image)
bg_lbl.place(x=0, y=0)

# Bind events and start the main loop
app.bind("<Configure>", bg_resizer)
update_buttons()
app.mainloop()
