import tkinter as tk
from PIL import Image, ImageTk
import image_loader

right_arrow_button = None
left_arrow_button = None

def create_buttons(app, right_arrow, left_arrow, button_height, button_width, images):
    global right_arrow_button, left_arrow_button
    right_arrow_button = tk.Button(app, text="", compound=tk.RIGHT, image=right_arrow, width=button_width,
                                   height=button_height,
                                   bg="#F2DED9", fg="#EFE9E8", borderwidth=0, relief=tk.FLAT,
                                   activebackground="#F2DED9", highlightthickness=2, highlightbackground="#FFCC70",
                                   command=lambda: image_loader.show_next_image(images))
    right_arrow_button.place(relx=0.8, rely=0.8, anchor="center")

    left_arrow_button = tk.Button(app, text="", compound=tk.RIGHT, image=left_arrow, width=button_width,
                                  height=button_height,
                                  bg="#F2DED9", fg="#EFE9E8", borderwidth=0, relief=tk.FLAT,
                                  activebackground="#F2DED9", highlightthickness=2, highlightbackground="#FFCC70",
                                  command=lambda: image_loader.show_prev_image(images))
    left_arrow_button.place(relx=0.2, rely=0.8, anchor="center")


def hide_arrows():
    global left_arrow_button, right_arrow_button
    if left_arrow_button:
        left_arrow_button.place_forget()
    if right_arrow_button:
        right_arrow_button.place_forget()
