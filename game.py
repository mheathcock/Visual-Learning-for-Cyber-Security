# game.py
from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk

class DragDropGameWindow(Toplevel):
    def __init__(self, back_callback, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Drag and Drop Game")
        self.geometry("800x600")

        self.canvas = Canvas(self, bg="white", width=800, height=600)
        self.canvas.pack(expand=YES, fill=BOTH)

        img1 = ImageTk.PhotoImage(file="c.png")
        img2 = ImageTk.PhotoImage(file="s.png")
        self.myImg2 = self.canvas.create_image(460, 234, anchor="center", image=img2)
        self.myImg = self.canvas.create_image(260, 125, anchor="center", image=img1)

        def move(e):
            self.canvas.delete(self.myImg)

            self.myImg = self.canvas.create_image(e.x, e.y, image=img1)
            self.myImg2 = self.canvas.create_image(e.x, e.y, image=img2)

        def back_button_click():
            back_callback()
            self.destroy()

        self.bind('<B1-Motion>', move)

        back_button = CTkButton(self, text="Back", corner_radius=32, text_color="#000000", bg_color="#F3E5E1",
                                fg_color="transparent", hover_color="#4158D0", border_color="#FFCC70", border_width=2,
                                command=back_button_click)
        back_button.pack()

        self.back_callback = back_callback
