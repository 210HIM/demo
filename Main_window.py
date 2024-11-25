from tkinter import *  # Python LIB GUI
from tkinter import ttk  # Python LIB GUI
from tkinter import filedialog  # Python LIB for access file menager
from Admin_info import *  # LIB get user informetion
from PIL import Image, ImageTk  # Python
import cv2 as cv
from Entery_Exit import *  # Python
from Program import *
import re
from datetime import datetime

# NEW
from _AGUI_fream import *


class Main_windows:
    def __init__(self):
        self.buttun_color = None
        self.Datafreame3 = None
        self.Datafreame2 = None
        self.root = None

    def Home_windos(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.wm_iconbitmap("Images/download.ico")
        self.camera_num = None
        self.temp = 0
        self.buttun_color = 'white'

        self.root.bind('<space>', lambda e: self.root.quit())

        # vareables
        self.Name_camera = None
        self.root.title("AMPS/Home")
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width, height))
        # Title
        lalttitle = Label(self.root, bd=5, relief=RAISED, text="Automated Parking Management System", fg='#e0e1e3',
                          bg='#455364', font=("times new roman", 15, 'bold'))
        lalttitle.place(x=0, y=0, width=1540)

        self.Datafreame_1 = Frame(self.root, bd=5, padx=20, bg='#19232d', relief=RIDGE)
        self.Datafreame_1.place(x=0, y=40, width=600, height=500)

        Label(self.Datafreame_1, text="Entry Get", font=("arial", 10, "bold"), relief=GROOVE, width=20,
                            fg="black", bg="#87ceeb").pack()

        self.vid_widget1 = Label(self.Datafreame_1, bg='#19232d')
        self.vid_widget1.pack()

        self.Datafreame_2 = Frame(self.root, bd=5, padx=20, bg='#19232d', relief=RIDGE)
        self.Datafreame_2.place(x=600, y=40, width=600, height=500)

        Label(self.Datafreame_2, text="Exit Get", font=("arial", 10, "bold"), relief=GROOVE, width=20,
                           fg="black", bg="#87ceeb").pack()

        self.vid_widget2 = Label(self.Datafreame_2, bg='#19232d')
        self.vid_widget2.pack()

        # Datafream2 is defaind userinfo
        self.Datafreame2 = Frame(self.root, bd=5, padx=20, bg='#a7d5ef', relief=GROOVE)
        self.Datafreame2.place(x=1205, y=40, width=330, height=400)

        # Datafream3 is defaind lower fream
        self.Datafreame3 = Frame(self.root, bd=5, padx=20, bg='#a7d5ef', relief=GROOVE)
        self.Datafreame3.place(x=1205, y=445, width=330, height=350)

        self.color = "#a7d5ef"
        # Datafream4 is defaindd lower left fream
        self.Datafreame4 = Frame(self.root, relief=GROOVE)
        self.Datafreame4.place(x=0, y=545, width=1200, height=250)

        # Admin _ data
        # self.obj = Admin(self.admin_id)
        # Admin_buttun = Button(self.Datafreame2,text ='Your Profile',command=self.obj.Admin__data,font=("arial",10,"bold"),relief=GROOVE,fg="black",bg="#87ceeb",width=15)
        # Admin_buttun.place(x = 10,y = 10)
        # self.changeOnHover(Admin_buttun,'#003153','#87ceeb')

        fream_obj = fream()
        self.Admin_buttun = Button(self.Datafreame2, text='Login', command=fream_obj.Login_fream, font=("arial", 10, "bold"),
                              relief=GROOVE, fg="black", bg="#87ceeb", width=15)
        self.Admin_buttun.place(x=10, y=10)
        self.changeOnHover(self.Admin_buttun, '#003153', '#87ceeb')

        # Entry and Exit
        self.status = StringVar()
        comNameTable_s = ttk.Combobox(self.Datafreame2, textvariable=self.status, font=("arial", 10, "bold"), width=15)

        comNameTable_s["values"] = ("Select form system", "En_Cemera_1", "En_Cemera_2", "En_Cemera_3")
        comNameTable_s.current(0)
        comNameTable_s.place(x=5, y=55)

        status_buttun = Button(self.Datafreame2, text='Select', command=self.Entry_get_cam_sel,
                               font=("arial", 8, "bold"), bg=self.buttun_color, width=10)
        status_buttun.place(x=180, y=55)
        self.changeOnHover(status_buttun, '#87ceeb', self.buttun_color)

        # done list
        self.Name_camera = StringVar()
        comNameTable = ttk.Combobox(self.Datafreame2, textvariable=self.Name_camera, font=("arial", 10, "bold"),
                                    width=15)

        comNameTable["values"] = ("Select form system", "Ex_Cemera_1", "Ex_Cemera_2", "Ex_Cemera_3")
        comNameTable.current(0)
        comNameTable.place(x=5, y=100)

        Admin_buttun = Button(self.Datafreame2, text='Select', command=self.print_data, font=("arial", 8, "bold"),
                              bg=self.buttun_color, width=10)
        Admin_buttun.place(x=180, y=100)
        self.changeOnHover(Admin_buttun, '#87ceeb', self.buttun_color)

        temp = datetime.now()
        date, time = list(str(temp).split())
        Label(self.Datafreame2, text="Data :", font=("arial", 10, "bold"), relief=GROOVE, width=15,
              bg=self.buttun_color).place(x=5, y=150)
        Label(self.Datafreame2, text=temp.strftime("%d-%b-%Y"), font=("arial", 10, "bold"),
              relief=GROOVE, width=15, bg=self.buttun_color).place(x=150, y=150)

        Label(self.Datafreame2, text="Capacities :", font=("arial", 10, "bold"), relief=GROOVE, width=15,
              bg=self.buttun_color).place(x=5, y=200)
        file = open("Text/complicity.txt", 'r')
        data = file.read()
        file.close()
        self.print_cap_label = Label(self.Datafreame2, text=data, font=("arial", 10, "bold"), width=15,
                                     bg=self.buttun_color, relief=GROOVE)
        self.print_cap_label.place(x=150, y=200)

        file = open("Text/avil_cap.txt", 'r')
        cap = file.read()
        file.close()

        vhi_count = Label(self.Datafreame2, text="Parked Car's :", font=("arial", 10, "bold"), relief=RIDGE, width=15,
                          bg=self.buttun_color)
        vhi_count.place(x=5, y=250)

        self.vhi_count_data = Label(self.Datafreame2, text=cap, font=("arial", 10, "bold"), relief=GROOVE, width=15,
                               bg=self.buttun_color)
        self.vhi_count_data.place(x=150, y=250)


        Label(self.Datafreame2, text="Available Cap :", font=("arial", 10, "bold"), relief=GROOVE,
                             width=15, bg=self.buttun_color).place(x=5, y=300)
        self.availabel_space =Label(self.Datafreame2, text=int(data)-int(cap), font=("arial", 10, "bold"), width=15, relief=GROOVE,
                                    bg=self.buttun_color)
        self.availabel_space.place(x=150, y=300)

        # Datafream_4
        # In Dataframe4 divedetion of block
        # fream1,2 is belong Entry_get
        self.fream_1 = Frame(self.Datafreame4, bd=4, bg="#19232d", relief=GROOVE)
        self.fream_1.place(x=0, y=0, width=300, height=240)

        self.fream_2 = Frame(self.Datafreame4, bd=4, bg="#19232d", relief=GROOVE)
        self.fream_2.place(x=300, y=0, width=300, height=240)

        self.fream_3 = Frame(self.Datafreame4, bd=4, bg="#19232d", relief=GROOVE)
        self.fream_3.place(x=600, y=0, width=300, height=240)

        self.fream_4 = Frame(self.Datafreame4, bd=4, bg="#19232d", relief=GROOVE)
        self.fream_4.place(x=900, y=0, width=300, height=240)


        Label(self.fream_1, text="Entry Get", font=("arial", 10, "bold"), relief=GROOVE, width=20,
                            fg="black", bg="#87ceeb").pack()
        self.Img = Label(self.fream_1, bg="#19232d", relief=GROOVE, fg="black", font=("arial", 15, "bold"))
        self.Img.pack()
        img_butt = Button(self.fream_1, text="Take img", font=("arial", 8, "bold"), fg="#e0e1e3", bg="#19232d",
                          width=10, command=self.select_img)
        img_butt.pack()


        Label(self.fream_2, text="Entry Get", font=("arial", 10, "bold"), relief=GROOVE, width=20,
                            fg="black", bg="#87ceeb").pack()
        self.lb_num_p = Label(self.fream_2, bg="#19232d", font=("arial", 10, "bold"), width=20)
        self.lb_num_p.pack()
        cunvert_butt = Button(self.fream_2, text="filter", font=("arial", 8, "bold"), fg="#e0e1e3", bg="#19232d",
                              width=10, command=self.filter_img)
        cunvert_butt.pack()
        self.lb_num_p_1 = Label(self.fream_2, bg="#19232d", font=("arial", 10, "bold"), width=20)
        self.lb_num_p_1.pack()

        # fream3,4 is belong Exit_get

        Label(self.fream_3, text="Exit Get", font=("arial", 10, "bold"), relief=GROOVE, width=20,
                            fg="black", bg="#87ceeb").pack()
        self.Img_1 = Label(self.fream_3, bg="#19232d", relief=GROOVE, fg="black", font=("arial", 15, "bold"))
        self.Img_1.pack()
        img_butt = Button(self.fream_3, text="Take img", font=("arial", 8, "bold"), fg="#e0e1e3", bg="#19232d",
                          width=10, command=self.select_img_1)
        img_butt.pack()


        Label(self.fream_4, text="Exit Get", font=("arial", 10, "bold"), relief=GROOVE, width=20,
                            fg="black", bg="#87ceeb").pack()

        self.lb_num_Exit = Label(self.fream_4, bg="#19232d", font=("arial", 10, "bold"), width=20)
        self.lb_num_Exit.pack()
        cunvert_butt = Button(self.fream_4, text="filter", font=("arial", 8, "bold"), fg="#e0e1e3", bg="#19232d",
                              width=10, command=self.filter_img_1)
        cunvert_butt.pack()
        self.lb_num_p_Exit = Label(self.fream_4, bg="#19232d", font=("arial", 10, "bold"), width=20)
        self.lb_num_p_Exit.pack()

        # Daatafream5 access for vhical
        # self.fream_5 = Frame(self.Datafreame3, bd=4, bg='#19232d', relief=GROOVE)
        # self.fream_5.place(x=1005, y=0, width=195, height=240)

        self.fream_5 = self.Datafreame3

        Acc_label_butt = Label(self.fream_5, text="Automatic Access Status", font=("arial", 10, "bold"), relief=GROOVE,
                               width=20, fg="black", bg="#87ceeb")
        Acc_label_butt.place(x=5, y=5)

        Label(self.fream_5,text="Status :",font=("arial", 10, "bold")).place(x=20, y=50)
        Access_button = Button(self.fream_5, text="Access", bg="red", width=10,bd=0, font=("arial", 10, "bold"))
        Access_button.place(x=130, y=50)
        self.changeOnHover(Access_button, 'red', 'red')

        Acc_label_b = Label(self.fream_5, text="Manually Access", font=("arial", 10, "bold"), relief=GROOVE, width=20,
                            fg="black", bg="#87ceeb")
        Acc_label_b.place(x=5, y=100)

        Label(self.fream_5, text="Status :", font=("arial", 10, "bold")).place(x=20, y=160)
        Access_button_men = Button(self.fream_5, text="Access", width=10, fg="black", bg='red',
                                   font=("arial", 10, "bold"))
        Access_button_men.place(x=130, y=160)
        self.changeOnHover(Access_button_men, 'green', 'red')

    def update_values(self):
        file = open("Text/avil_cap.txt", 'r')
        cap = file.read()
        file.close()

        file = open("Text/complicity.txt", 'r')
        data = file.read()
        file.close()

        self.vhi_count_data.config(text=cap)
        self.availabel_space.config(text=int(data)-int(cap))



    def select_img_1(self):
        name_img = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                              filetypes=(("Image files", "*.jpeg*"), ("all files", "*.*")))
        if len(name_img) == 0:
            print("return")
            return
        self.img = cv.imread(name_img)
        photo = cv.resize(self.img, (200, 180))
        new_img = photo
        opencv_image = cv.cvtColor(new_img, cv.COLOR_BGR2RGBA)
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)
        self.Img_1.photo_image = photo_image
        self.Img_1.configure(image=photo_image)

    def select_img(self):
        name_img = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                              filetypes=(("Image files", "*.jpeg*"), ("all files", "*.*")))
        if len(name_img) == 0:
            print("return")
            return
        self.img = cv.imread(name_img)
        photo = cv.resize(self.img, (200, 180))
        new_img = photo
        opencv_image = cv.cvtColor(new_img, cv.COLOR_BGR2RGBA)
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)
        self.Img.photo_image = photo_image
        self.Img.configure(image=photo_image)

    def filter_img(self):
        number_plate = number_plate_detection(self.img)
        if number_plate != None:
            res2 = str("".join(re.split("[^a-zA-Z0-9]*", number_plate)))
            res2 = res2.upper()
            self.Num_PL = res2
            self.lb_num_p_1.config(text=self.Num_PL, fg="red", font=('arial', 15, 'bold'))
            update_entry_get(self.Num_PL)
            self.update_values()
        else:
            self.Num_PL = None
            self.lb_num_p_1.config(text="NONE", fg="red", font=('arial', 15, 'bold'))

    def filter_img_1(self):
        number_plate = number_plate_detection(self.img)
        if number_plate != None:
            res2 = str("".join(re.split("[^a-zA-Z0-9]*", number_plate)))
            res2 = res2.upper()
            self.Num_PL = res2
            self.lb_num_p_Exit.config(text=self.Num_PL, fg="red", font=('arial', 15, 'bold'))
            update_Exit_get(self.Num_PL)
            self.update_values()
        else:
            self.Num_PL = None
            self.lb_num_p_Exit.config(text="NONE", fg="red", font=('arial', 15, 'bold'))



    def change_data(self):
        val = self.cep_Entry.get()
        self.print_cap_label.config(text=val)

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover, fg="black"))
        button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave, fg="black"))

    # Play video on mainscrren
    def open_video_Entry(self):
        try:
            isTrue, frame = self.vid.read()
        except:
            messagebox.showwarning("warning",
                                   "The video is currently unavailable and will be available again in a few time.")
            return
        # date and time
        temp = datetime.now()
        date_time = list(str(temp).split())
        cv.putText(frame, str(temp), (50, 350), cv.FONT_HERSHEY_TRIPLEX, 0.50, (0, 255, 0), 1)
        cv.rectangle(frame, (730, 420), (2, 180), (0, 255, 0), thickness=2)
        try:
            opencv_image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
        except:
            return
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)
        self.vid_widget2.photo_image = photo_image
        self.vid_widget2.configure(image=photo_image)
        self.vid_widget2.after(25, self.open_video_Entry)

    def open_video_Exit(self):
        try:
            isTrue, frame = self.vid_EX.read()
        except:
            messagebox.showwarning("warning",
                                   "The video is currently unavailable and will be available again in a few time.")
            return
        # date and time
        temp = datetime.now()
        date_time = list(str(temp).split())
        cv.putText(frame, str(temp), (50, 350), cv.FONT_HERSHEY_TRIPLEX, 0.50, (0, 255, 0), 1)
        cv.rectangle(frame, (730, 420), (2, 180), (0, 255, 0), thickness=2)
        try:
            opencv_image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
        except:
            return
        captured_image = Image.fromarray(opencv_image)
        photo_image = ImageTk.PhotoImage(image=captured_image)
        self.vid_widget1.photo_image = photo_image
        self.vid_widget1.configure(image=photo_image)
        self.vid_widget1.after(25, self.open_video_Exit)

    def print_data(self):
        self.camera_num = self.Name_camera.get()
        cam_list = ["Select form system", "Videos/car.mp4", "Videos/DON.mp4", "Videos/girl.mp4"]
        if cam_list[0] == self.camera_num:
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                       filetypes=(("Image files", "*.mp4*"), ("all files", "*.*")))
            print(self.filename)
            if len(self.filename) != 0:
                self.vid = cv.VideoCapture(self.filename)
                self.open_video_Entry()
        else:
            n = int(self.camera_num[-1])
            self.vid = cv.VideoCapture(cam_list[n])
            self.open_video_Entry()

    def Entry_get_cam_sel(self):
        self.camera_num_1 = self.status.get()
        cam_list = ["Select form system", "Videos/car.mp4", "Videos/DON.mp4", "Videos/girl.mp4"]
        if cam_list[0] == self.camera_num_1:
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                                       filetypes=(("Image files", "*.mp4*"), ("all files", "*.*")))
            print(self.filename)
            if len(self.filename) != 0:
                self.vid_EX = cv.VideoCapture(self.filename)
                self.open_video_Exit()
        else:
            n = int(self.camera_num_1[-1])
            self.vid_EX = cv.VideoCapture(cam_list[n])
            self.open_video_Exit()


if __name__ == "__main__":
    obj = Main_windows()
    obj.Home_windos()

    mainloop()
