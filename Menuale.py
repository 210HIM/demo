from tkinter import *
from tkinter import ttk
import cv2 as cv  # python lib for open image and video play
from PIL import ImageTk, Image  # Python lib for open image
from PIL import *
from tkinter import filedialog


class Menual:
    def __init__(self):
        self.root = None
        file = open("Text/Menuall.txt", 'r')
        self.mesg = file.read()
        self.path = None

    def informetion(self,root):
        self.root = root

        self.title_boder = Frame(self.root, bg='#3c3f41', )
        self.title_boder.place(x=0, y=0, width=1230, height=30)
        Label(self.title_boder, text="Admin/Manuele", font=("arial", 10, 'bold')).place(x=0, y=2, )


        Datafream1 = Frame(self.root, bg="#f0f8ff")
        Datafream1.place(x=0, y=30, width=650, height=680)

        text = Text(Datafream1, width=69, height=41, font=("Courier New", 11), bg='#f0f8ff')
        text.place(x=0, y=0)
        text.insert(END, self.mesg)

        self.y_scollbar = ttk.Scrollbar(Datafream1, orient="vertical", command=text.yview)
        self.y_scollbar.place(x=630, y=0, height=680)
        text['yscroll'] = self.y_scollbar.set
        text.config(state=DISABLED, xscrollcommand=self.y_scollbar.set)

        Datafream2 = Frame(self.root, bd=5, bg="#3da8d8")
        Datafream2.place(x=650, y=35, width=150, height=680)

        values = ("Block Daigram", "Flow chart", "Process chart")
        self.path = StringVar()
        self.path.set("Block Daigram")
        Table_s = OptionMenu(Datafream2, self.path, *values)
        Table_s.place(x=0, y=0, width=10)

        status_buttun = Button(Datafream2, text='Select', font=("arial", 8, "bold"), fg="#e0e1e3", bg="#003153",
                               width=10,command=self.select_img)
        status_buttun.place(x=30, y=0)

    def Exit(self):
        self.root.destroy()

    def select_img(self):
        file_name = self.path.get()
        # print(file_name)
        value = ["Block Daigram", "Flow chart", "Process chart"]
        Path_offile = ["Images/Block Diagram.jpg", "Images/Flowchart.jpg", "Images/Process chart.jpg"]
        ind = value.index(file_name)
        img = cv.imread(Path_offile[ind])
        cv.imshow("img", img)

