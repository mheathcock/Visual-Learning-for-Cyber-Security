from PIL import Image, ImageTk
import tkinter as tk

image_labels = {}
current_image_index = 0
current_page_index = 0

'''Function to load and display the images on the screen'''


def load_and_display_image(images):
    # global Variables
    global current_image_index, current_page_index, image_labels

    # destroy the existing label if it exists
    if current_image_index in image_labels:  # if the image number is in the collection of images
        image_labels[current_image_index].destroy()  # stop showing the image
        del image_labels[current_image_index]

    # create a new label for the image
    image_label = tk.Label(borderwidth=0)
    image_labels[current_image_index] = image_label  # the image in that particular index is set to the canvas image

    if images:  # if there are images
        current_image_paths = images[current_page_index]["image_paths"]  # path to the image set
        current_image_path = current_image_paths[current_image_index]  # current image = the image at the index

        # create the image
        img = Image.open(current_image_path)
        img = img.resize((img.width // 2, img.height // 2), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(img)

        center_x = (1920 - img.width) / 2
        center_y = (1080 - img.height) / 2

        # configure the label with the new image
        image_label.configure(image=image)
        image_label.image = image
        image_label.place(x=center_x, y=center_y)


'''Function to display the next image when the arrow button is pressed'''


def show_next_image(images):
    global current_image_index, current_page_index

    # clear images associated with the current page
    clear_images()

    # increment the image index
    current_image_index += 1

    # check if the image index is out of bounds and reset to the maximum index if needed
    if current_image_index >= len(images[current_page_index]["image_paths"]):
        current_image_index = 0

    load_and_display_image(images)


'''Function to display the previous image when the arrow button is pressed'''


def show_prev_image(images):
    global current_image_index, current_page_index

    # clear images associated with the current page
    clear_images()

    # decrement the image index
    current_image_index -= 1

    # check if the image index is less than 0 and reset to the maximum index if needed
    if current_image_index < 0:
        current_image_index = len(images[current_page_index]["image_paths"]) - 1

    load_and_display_image(images)


'''Function to remove an image'''


def clear_images():
    global image_labels
    for label in image_labels.values():
        label.destroy()
    image_labels = {}
