# app.py
import tkinter as tk
from customtkinter import *
from PIL import Image, ImageTk
import create_arrows
import image_loader
from game import DragDropGameWindow
from flashlightgame import FlashlightGameWindow
from DdosExample import DdosExampleGameWindow

app = CTk()
app.geometry("1920x1080")

set_appearance_mode("light")

right_arrow = Image.open("arrowR.png")
left_arrow = Image.open("arrow2.png")

image = Image.open("background.png")
background_image = CTkImage(image, size=(1920, 1080))

current_page_index = -1

images = [
    {"name": "Page 1", "image_paths": ["Images/PhishingComic.png", "Images/PhishingPoster.png"]},
    {"name": "Page 2", "image_paths": ["Images/ddoscomic.png", "Images/DOS poster.png"]},
    {"name": "Page 3", "image_paths": ["Images/SoftwareUpdate2.png", "Images/SoftwareUpdate1.png"]},
    {"name": "Page 4", "image_paths": ["Images/wormVSvirus.png", "Images/Trojan.png", "Images/Trojan2.png"]},
    {"name": "Page 5", "image_paths": ["Images/VulnerabilityPoster.png", "Images/VulnerabilityComic.png" ]}
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

opacity = 0.5
title_frame = tk.Frame(app, bg="#F2ECEC", highlightbackground="#FFCC70", highlightthickness=5,  width=600)
title_label = CTkLabel(title_frame, text="TOPICS", font=("Arial Rounded MT Bold", 70), bg_color="#F2ECEC", fg_color="transparent", text_color="#D67FFF")
title_label.configure(width=20)
title_frame.place(relx=0.5, rely=0.05, anchor="center")
title_label.pack(padx=10, pady=10)




def set_title(new_title):
    title_label.configure(text=new_title)

def Page1ButtonClick():
    global current_page_index
    current_page_index = 0
    image_loader.current_page_index = current_page_index
    set_title(Page1btn.cget("text"))
    main_menu()
    image_loader.load_and_display_image(images)

def Page2ButtonClick():
    global current_page_index
    current_page_index = 1
    image_loader.current_page_index = current_page_index
    set_title(Page2btn.cget("text"))
    main_menu()
    image_loader.load_and_display_image(images)


def Page3ButtonClick():
    global current_page_index
    current_page_index = 2
    image_loader.current_page_index = current_page_index
    set_title(Page3btn.cget("text"))
    main_menu()
    image_loader.load_and_display_image(images)

def Page4ButtonClick():
    global current_page_index
    current_page_index = 3
    image_loader.current_page_index = current_page_index
    set_title(Page4btn.cget("text"))
    main_menu()
    image_loader.load_and_display_image(images)

def Page5ButtonClick():
    global current_page_index
    current_page_index = 4
    image_loader.current_page_index = current_page_index
    set_title(Page5btn.cget("text"))
    main_menu()
    image_loader.load_and_display_image(images)



def BackButtonClick():
    global current_page_index
    current_page_index = -1
    image_loader.current_page_index = current_page_index
    set_title("TOPICS")
    main_menu()
    for label in image_loader.image_labels.values():
        label.destroy()
    image_loader.image_labels = {}
    create_arrows.hide_arrows()



def FlashlightGameButtonClick():
    game_window = FlashlightGameWindow(main_menu)
    game_window.mainloop()


def DosExampleGameBtnClick():
    game_window = DdosExampleGameWindow(main_menu)
    game_window.mainloop()



FlashLightGame = CTkButton(master=app, text="VULNERABILITIES INTERACTIVE GAME", font=("Arial Rounded MT Bold", 40), corner_radius=32, text_color="#7FC9FF", bg_color="#F3E5E1",
                    fg_color="#F2ECEC", hover_color="#4158D0", border_color="#FFCC70", border_width=4,
                    command=FlashlightGameButtonClick)

DosExampleGame = CTkButton(master=app, text="DOS INTERACTIVE GAME",font=("Arial Rounded MT Bold", 40), corner_radius=32, text_color="#FF7F7F", bg_color="#F3E5E1",
                    fg_color="#F2ECEC", hover_color="#4158D0", border_color="#FFCC70", border_width=4,
                    command=DosExampleGameBtnClick)


Page1btn = CTkButton(master=app, text="PHISHING", font=("Arial Rounded MT Bold", 40), corner_radius=32, text_color="#FF7FED", bg_color="#F3E5E1",
                     fg_color="#F2ECEC", hover_color="#4158D0", border_color="#FFCC70", border_width=4,
                     command=Page1ButtonClick)

Page2btn = CTkButton(master=app, text="DOS", font=("Arial Rounded MT Bold", 40),corner_radius=32, text_color="#7F92FF", bg_color="#F3E5E1",
                     fg_color="#F2ECEC", hover_color="#4158D0", border_color="#FFCC70", border_width=4,
                     command=Page2ButtonClick)
Page3btn = CTkButton(master=app, text="SOFTWARE PATCHES", font=("Arial Rounded MT Bold", 40), corner_radius=32, text_color="#7FFF8E", bg_color="#F3E5E1",
                     fg_color="#F2ECEC", hover_color="#4158D0", border_color="#FFCC70", border_width=4,
                     command=Page3ButtonClick)
Page4btn = CTkButton(master=app, text="MALWARE", font=("Arial Rounded MT Bold", 40), corner_radius=32, text_color="#7FC9FF", bg_color="#F3E5E1",
                     fg_color="#F2ECEC", hover_color="#4158D0", border_color="#FFCC70", border_width=4,
                     command=Page4ButtonClick)

Page5btn = CTkButton(master=app, text="VULNERABILITIES AND EXPLOITS", font=("Arial Rounded MT Bold", 40), corner_radius=32, text_color="#FF7FB6", bg_color="#F3E5E1",
                     fg_color="#F2ECEC", hover_color="#4158D0", border_color="#FFCC70", border_width=4,
                     command=Page5ButtonClick)

Backbtn = CTkButton(master=app, text="BACK", font=("Arial Rounded MT Bold", 30), corner_radius=32,
                                text_color="white", bg_color="#7C523E",
                                fg_color="#442D22", hover_color="#4158D0", border_color="#FFCC70", border_width=4,
                                command=BackButtonClick)


InfoBox = CTkFrame(master=app, fg_color="#F2ECEC", bg_color="#F3E5E1", border_color="#FFCC70", border_width=4)

InfoLabel = CTkLabel(master=InfoBox, text="This program is an educational tool for\n teaching cyber-security through art!\n"
                                          "Click any of the topics to\n get started and use the arrow\n"
                                          "buttons on screen to flick\n through the related artworks.", font=("Arial Rounded MT Bold", 35))

def main_menu():
    InfoBox.place_forget()
    InfoLabel.pack_forget()
    # when not on the main menu screen clear all the main menu buttons   MAYBE ADD THIS TO THE ELSE STATEMENT
    for btn in [Page1btn, Page2btn, Page3btn, Page4btn, Backbtn, FlashLightGame, Page5btn, DosExampleGame]:
        btn.place_forget()
    # if on main menu clear any image that was on the screen and hide the arrows to navigate the images
    for label in image_loader.image_labels.values():
        label.destroy()
    image_loader.image_labels = {}
    create_arrows.hide_arrows()

    Backbtn.forget()


    #if on the main menu screen place all the topic pages
    if current_page_index == -1:

        Page1btn.place(relx=0.8, rely=0.2, anchor="center")
        Page2btn.place(relx=0.5, rely=0.5, anchor="center")
        Page3btn.place(relx=0.8, rely=0.6, anchor="center")
        Page4btn.place(relx=0.2, rely=0.8, anchor="center")
        Page5btn.place(relx=0.2, rely=0.2, anchor="center")

        InfoBox.place(relx=0.5, rely=0.8, anchor="center")
        InfoLabel.pack(pady=10, padx=30)


    else:#if not on main menu then add the arrows to navigate the images and add the feedback buttons

        create_arrows.create_buttons(app, resized_img_right_arrow, resized_img_left,
                                     button_image_height, button_image_width, images)
        Backbtn.place(relx=0.2, rely=0.2, anchor="center")
        if current_page_index == 4:
            FlashLightGame.place(relx=0.5, rely=0.15, anchor="center")
        elif current_page_index == 1:
            DosExampleGame.place(relx=0.5, rely=0.13, anchor="center")


print(current_page_index)
main_menu()

app.bind("<Configure>", bg_resizer)
app.mainloop()
