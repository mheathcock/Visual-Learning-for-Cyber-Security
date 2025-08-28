from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import random


class DdosExampleGameWindow(Toplevel):
    def __init__(self, back_callback, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Load basic app info like the background, size and title
        background_img = Image.open("Images/ddosexamplebackgroubd.png")
        background_tk_img = ImageTk.PhotoImage(background_img)
        self.title("DOS Example Game")
        self.geometry("1920x1080")

        # create a canvas
        self.canvas = Canvas(self, width=1920, height=1080)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=background_tk_img)
        self.canvas.image = background_tk_img  # store a reference to prevent garbage collection

        '''Function for whent the user wants to go back to the main menu'''

        def back_button_click():
            back_callback()
            self.destroy()

        # creates a back button
        back_button = CTkButton(self, text="BACK", font=("Arial Rounded MT Bold", 16), corner_radius=32,
                                text_color="white", bg_color="#7C523E",
                                fg_color="#442D22", hover_color="#4158D0", border_color="#FFCC70", border_width=2,
                                command=back_button_click)
        back_button.place(relx=0.05, rely=0.05, anchor="center")

        self.back_callback = back_callback

        # define the border coordinates
        self.border_coordinates = (1325, 258, 1842, 888)

        # list to store created frames along with their labels and buttons
        self.frames = []
        self.frame_counter = 0  # counter to track the number of frames sent

        # starting instructions label
        self.start_label = Label(self.canvas,
                                 text="You are a server being sent maths problems to solve for the users! Click here to start solving!",
                                 font=("Arial Rounded MT Bold", 16), bg="#EFC8BD", cursor="hand2")

        # the starting insturctions label must be clicked to check the user has read the instructions
        self.start_label.bind("<Button-1>", self.start_sending_messages)
        self.start_label.place(relx=0.5, rely=0.5, anchor="center")

        # variable to track if the label has been clicked
        self.label_clicked = False

    '''Function to start the DOS example '''

    def start_sending_messages(self, event):
        # if the instructions have been clicked
        if not self.label_clicked:
            self.label_clicked = True
            self.start_label.destroy()  # remove the label
            self.create_frames_periodically(
                3000)  # start sending messages initially with a wait of 3 seconds inbetween

    '''Function to generate some random maths questions'''

    def generate_maths(self):
        var1 = random.randint(1, 20)
        var2 = random.randint(1, 20)
        var3_options = ['+', '-', '*', '/']
        var3 = random.choice(var3_options)
        return f"{var1} {var3} {var2}"

    '''Function to create the question boxes that'll move around the screen'''

    def create_frames_periodically(self, interval):
        # update the canvas to ensure accurate dimensions
        self.update_canvas()

        # create a frame
        if self.frame_counter < 20:  # if the frame count is less than 20
            frame, label, textbox, submitBtn = self.add_frame()
            self.frames.append((frame, label, textbox, submitBtn))  # append frame along with its labels and button
            self.frame_counter += 1  # increment frame counter
            print("Frame", self.frame_counter, "sent")  # print current frame number for DEBUG

            # Start frame animation
            self.animate_frames()
            # if frame count is 20
            if self.frame_counter == 20:
                print("HERE")  # DEBUG
                self.delete_all_frames()  # delete all frames
                self.display_example_ended_message()  # display the end message

        # If the amount of frames is over 3 than decrease the waiting time between each message being sent
        if self.frame_counter > 3:
            self.after(interval, self.create_frames_periodically, 1000)
        else:#if less than 3 carry on as normal
            self.after(interval, self.create_frames_periodically, interval)

    def update_canvas(self):
        # Update the canvas to ensure accurate dimensions
        self.canvas.update_idletasks()

    '''Function to make the frame and spawn it '''

    def add_frame(self):
        # set the starting position
        start_x = 400
        start_y = 613

        # calculate the final position
        end_x = random.randint(self.border_coordinates[0], self.border_coordinates[2])
        end_y = random.randint(self.border_coordinates[1], self.border_coordinates[3])

        # create a new frame with the fixed starting position
        new_frame = CTkFrame(master=self.canvas, width=200, height=200, fg_color="#EFC8BD", border_color="#FFCC70",
                             border_width=2)

        # place the frame at the exact coordinates within the canvas
        new_frame.place(x=start_x, y=start_y)

        # store the initial and final positions of the frame
        new_frame.initial_position = (start_x, start_y)
        new_frame.final_position = (end_x, end_y)
        new_frame.animation_complete = False  # flag to track animation completion

        # add label, entry, and submit button to the frame
        label = CTkLabel(new_frame, text=self.generate_maths(), font=("Arial Rounded MT Bold", 15),
                         bg_color="#EFC8BD", fg_color="transparent")
        label.pack(pady=5)
        textbox = CTkEntry(new_frame, corner_radius=16, border_color="#FFCC70", border_width=2)
        textbox.pack(pady=5)
        submitBtn = CTkButton(master=new_frame, text="Submit", font=("Arial Rounded MT Bold", 14),
                              corner_radius=16, text_color="white", bg_color="#7C523E",
                              fg_color="#442D22", hover_color="#4158D0", border_color="#FFCC70", border_width=2,
                              command=lambda frame=new_frame: self.delete_frame(frame))
        submitBtn.pack(pady=5)
        self.canvas.create_window(start_x, start_y, anchor="center", window=new_frame)

        return new_frame, label, textbox, submitBtn  # return frame along with its labels and button

    '''Function to delete a frame'''

    def delete_frame(self, frame_to_delete):
        frame_to_delete.destroy()
        # Remove the deleted frame from the list
        self.frames = [frame_info for frame_info in self.frames if frame_info[0] != frame_to_delete]

    '''Function to delete all frames'''

    def delete_all_frames(self):
        # Delete all frames
        for frame_info in self.frames:
            frame_info[0].destroy()
        self.frames = []  # Clear the frames list after deletion
    '''Function to display a message at the end of the example'''
    def display_example_ended_message(self):
        DDOS_Explained_frame = Frame(self.canvas, bg="#EFC8BD", highlightbackground="#FFCC70", highlightthickness=2)
        DDOS_ended = Label(DDOS_Explained_frame, text="Feeling overwhelmed?", font=("Arial Rounded MT Bold", 30),
                           bg="#EFC8BD")  # No need to specify background color
        DDOS_Explained = Label(DDOS_Explained_frame,
                               text="A DOS is a Denial Of Service. The attacker overwhelms the server by sending so many spam requests the server"
                                    " crashes", font=("Arial Rounded MT Bold", 15), bg="#EFC8BD")
        DDOS_Explained_frame.place(relx=0.5, rely=0.5, anchor="center")
        DDOS_ended.pack(pady=0.5)
        DDOS_Explained.pack(pady=0.5)

    def animate_frames(self):
        # animate each frame
        for frame_info in self.frames:
            if not frame_info[0].animation_complete:
                self.move_frame(frame_info)

    def move_frame(self, frame_info):
        #  the speed of the animation
        speed = 30
        if len(self.frames) > 3:
            speed = 20
        elif len(self.frames) > 7:
            speed = 15
        elif len(self.frames) > 15:
            speed = 10

        print(speed)#DEBUG

        # get initial and final positions of the frame
        initial_x, initial_y = frame_info[0].initial_position
        final_x, final_y = frame_info[0].final_position

        # calculate the movement increments for x and y coordinates
        dx = (final_x - initial_x) / speed
        dy = (final_y - initial_y) / speed

        # call the move_frame_helper to start the animation
        self.move_frame_helper(frame_info, dx, dy, speed, initial_x, initial_y)

    def move_frame_helper(self, frame_info, dx, dy, speed, current_x, current_y):
        # calculate new coordinates
        new_x = current_x + dx
        new_y = current_y + dy

        # move frame to the new position
        frame_info[0].place(x=new_x, y=new_y)

        # check if frame has reached its final position
        if (dx > 0 and new_x >= frame_info[0].final_position[0]) or (
                dx < 0 and new_x <= frame_info[0].final_position[0]) \
                or (dy > 0 and new_y >= frame_info[0].final_position[1]) or (
                dy < 0 and new_y <= frame_info[0].final_position[1]):
            frame_info[0].animation_complete = True
            print("Frame animation complete:", frame_info[0].final_position) #DEBUG

        # continue animation until the frame reaches the end point
        if not frame_info[0].animation_complete:
            self.after(speed, lambda: self.move_frame_helper(frame_info, dx, dy, speed, new_x, new_y))


# Sample usage
def callback():
    print("Back button clicked") #DEBUG
