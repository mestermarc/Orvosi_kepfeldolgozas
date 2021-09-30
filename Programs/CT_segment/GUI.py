import tkinter as tk
from tkinter import ttk
import cv2
import PIL.Image, PIL.ImageTk
from matplotlib import cm
import numpy as np
import matplotlib.pylab as plt
from PIL import Image,ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import img_processing

"""
        def slider_changed(event):
            value_label.configure(text=get_current_value())
            if self.orig_dataset:
                photo = PIL.ImageTk.PhotoImage(
                    image=PIL.Image.fromarray(dataset[get_current_value()])
                )
            else:
                photo = PIL.ImageTk.PhotoImage(
                    image=PIL.Image.fromarray((np.uint8((internal[get_current_value()]) * 255))))
            self.imgLabel.config(image=photo)
            self.imgLabel.photo_ref = photo  # keep a reference
"""
class GUI_Panel:

    messageBox = tk.Text
    root = tk.Tk()
    imageCanvas = tk.Canvas(root, width=512, height=512)
    imgLabel = ttk.Label()
    orig_dataset=True

    def __init__(self,dataset):
        def get_current_value():
            return int(current_value.get())

        def changeView():
            self.orig_dataset = not self.orig_dataset
            print("dataset now is:", self.orig_dataset)

        #internal = img_processing.preprocessing(dataset)
        im = dataset[0]
        self.orig_dataset=True
        self.root.geometry('800x800')
        self.root.resizable(True, True)
        self.root.title('Image segmentation')

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)

        # slider current value
        current_value = tk.DoubleVar()

        slider_label = ttk.Label(
            self.root,
            text='Slider:',
        )

        slider_label.grid(
            column=0,
            row=0,
            sticky='w'
        )

        slider = ttk.Scale(
            self.root,
            from_=0,
            to=300,
            orient='horizontal',  # vertical
            #command=slider_changed,
            variable=current_value
        )

        slider.grid(
            column=1,
            row=0,
            sticky='we',
            padx=50,
            pady=20
        )

        # current value label
        current_value_label = ttk.Label(
            self.root,
            text='Current Value:'
        )

        current_value_label.grid(
            row=1,
            columnspan=1,
            sticky='ne',
            ipadx=10,
            ipady=10
        )


        # value label
        value_label = ttk.Label(
            self.root,
            text=get_current_value()

        )
        value_label.grid(
            row=1,
            columnspan=2,
            sticky='n',
            ipadx=10,
            ipady=10
        )

        ##      img processing:         ##

        # Use PIL (Pillow) to convert the NumPy ndarray to a PhotoImage
        #photo2 = ImageTk.PhotoImage(Image.open("rs.jpg"))
        photo2 = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(im))
        self.imgLabel.config(image=photo2)
        self.imgLabel.photo_ref = photo2  # keep a reference

        f = plt.figure()
        a = f.add_subplot(111)
        t = np.arange(0.0, 3.0, 0.01)
        a.imshow(im)

        canvas = FigureCanvasTkAgg(f, master=self.root)
        #canvas.show()
        canvas.get_tk_widget().grid(
            row=3,
            columnspan=3,
            sticky='w'
        )

        # Add a PhotoImage to the Canvas
    ##      messagebox init:         ##
        Output = tk.Text(self.root, height=5,
                      width=25,
                      bg="light gray")

        self.messageBox = Output

        self.messageBox.grid(
            row=3,
            columnspan=6,
            sticky='ne',
            padx=20,
            pady=20
        )

        viewButton = tk.Button(text="Change view", command=changeView)

        viewButton.grid(
            row=4,
            columnspan=2,
            sticky='s',
            padx=20,
            pady=20
        )
        self.root.configure(background='gray')

    def log(self,text):
        self.messageBox.insert(tk.END, text)


