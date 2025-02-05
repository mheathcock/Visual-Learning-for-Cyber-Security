from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk

class FlashlightGameWindow(Toplevel):
    def __init__(self, back_callback, *args, **kwargs):

        super().__init__(*args, **kwargs)

        background_img = Image.open("backgroundFlashlightGame.png")
        background_tk_img = ImageTk.PhotoImage(background_img)
        self.title("Flashlight Game")
        self.geometry("1920x1080")

        self.canvas = Canvas(self, width=1920, height=1080)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=background_tk_img)
        self.canvas.image = background_tk_img  # Store a reference to prevent garbage collection

        flashlight_img = ImageTk.PhotoImage(file="flashlight.png")  # Replace with your flashlight image path

        # Resize the hidden text image to a smaller size
        hidden_text_pil = Image.open("imagetext.png")  # Replace with your hidden text image path
        desired_width = 220  # Replace with the desired width
        desired_height = 93  # Replace with the desired height
        hidden_text_pil = hidden_text_pil.resize((desired_width, desired_height), Image.ANTIALIAS)
        hidden_text_img = ImageTk.PhotoImage(hidden_text_pil)

        self.flashlight = self.canvas.create_image(1000, 125, anchor="center", image=flashlight_img)
        self.hidden_text = self.canvas.create_image(1244, 444, anchor="center", image=hidden_text_img, state="hidden")

        self.flashlight_img = flashlight_img  # Store reference to avoid garbage collection
        self.hidden_text_img = hidden_text_img  # Store reference to avoid garbage collection

        # Create a frame to contain the label
        self.frame = Frame(self.canvas, bg="#EFC8BD", highlightbackground="#FFCC70", highlightthickness=2)
        self.frame.place(relx=0.5, rely=0.1, anchor="center")

        # Create a label inside the frame
        self.label = Label(self.frame, text="Someone has attempted to hide a secret in invisible ink. Can you figure out which item can exploit its vulnerability? ... Click here to continue",
                      font=("Arial Rounded MT Bold", 16), bg="#EFC8BD")
        self.label.pack(padx=10, pady=10)

        # Variable to track if the label has been clicked
        self.label_clicked = False

#Move the flashlight around
        def move(e):
            # Check if the label has been clicked
            if self.label_clicked:
                x, y = e.x, e.y

                # Get the bounding box coordinates of the flashlight image
                flashlight_x, flashlight_y = self.canvas.coords(self.flashlight)
                flashlight_width = self.flashlight_img.width()
                flashlight_height = self.flashlight_img.height()

                # Check if the mouse coordinates are within the bounding box of the flashlight image
                if (flashlight_x - flashlight_width / 2 < x < flashlight_x + flashlight_width / 2) and \
                        (flashlight_y - flashlight_height / 2 < y < flashlight_y + flashlight_height / 2):

                    # Move the existing flashlight image to the new position
                    self.canvas.coords(self.flashlight, x, y)

                    # Get the coordinates and dimensions of the hidden text image
                    hidden_x, hidden_y = self.canvas.coords(self.hidden_text)
                    hidden_width = self.hidden_text_img.width()
                    hidden_height = self.hidden_text_img.height()

                    # Print flashlight coordinates
                  #  print(f"Flashlight coordinates: ({x}, {y})")

                    # Check if the flashlight is within the bounding box of the hidden text
                    if hidden_x - hidden_width / 2 < x < hidden_x + hidden_width / 2 and \
                            hidden_y - hidden_height / 2 < y < hidden_y + hidden_height / 2:
                        # Show the hidden text
                        self.canvas.itemconfigure(self.hidden_text, state="normal")
                        print("Hidden text found!")#DEBUG
                        self.HiddenFound = True
                    else:
                        # Hide the hidden text if not within the bounding box
                        self.canvas.itemconfigure(self.hidden_text, state="hidden")

                    if self.HiddenFound:
                        self.frame2 = Frame(self.canvas, bg="#EFC8BD", highlightbackground="#FFCC70",
                                            highlightthickness=2)
                        self.frame2.place(relx=0.5, rely=0.1, anchor="center")

                        # Create a label inside the frame
                        self.label2 = Label(self.frame2, text="Congratulations! You figured out the vulnerability of the invisible ink and exploited it using the UV flashlight!",
                                            font=("Arial Rounded MT Bold", 16), bg="#EFC8BD")
                        self.label2.pack(padx=10, pady=10)

        def label_click(event):
            # Set the label_clicked variable to True
            self.label_clicked = True
            # Delete the label and the frame from the canvas
            self.label.destroy()
            self.frame.destroy()

        # Bind the label click event to the label_click function
        self.label.bind('<Button-1>', label_click)


        def back_button_click():
            back_callback()
            self.destroy()

        back_button = CTkButton(self, text="BACK", font=("Arial Rounded MT Bold", 16), corner_radius=32, text_color="white", bg_color="#7C523E",
                                fg_color="#442D22", hover_color="#4158D0", border_color="#FFCC70", border_width=2,
                                command=back_button_click)
        back_button.place(relx=0.05, rely=0.05, anchor="center")

        self.back_callback = back_callback

        # Start updating coordinates
       # self.after(100, update_coordinates)

        # Bind motion event only after label click
        self.bind('<B1-Motion>', move)





if __name__ == "__main__":
    root = Tk()

    def back_callback():
        print("Back button clicked!")

    game_window = FlashlightGameWindow(back_callback)
    root.mainloop()
