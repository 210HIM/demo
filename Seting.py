from tkinter import *

class Additional:
    def __init__(self):
        self.root = None

    def add_capicity(self, root, title):

        self.root = root

        self.title_boder = Frame(self.root, bg='#3c3f41', )
        self.title_boder.place(x=0, y=0, width=1230, height=30)
        Label(self.title_boder, text="Admin/Settings", font=("arial", 10, 'bold')).place(x=0, y=2, )

        self.cap_fream = Frame(self.root, bd=5, padx=20, relief=RIDGE, bg="#a7d5ef")
        self.cap_fream.place(x=0, y=30, width=800, height=200)

        Label(self.cap_fream, text="SET CAPACITY",font=("arial", 10), relief=GROOVE, width=20, fg="black",
                      bg="#87ceeb").place(x=10, y=20)

        Label(self.cap_fream, text="Capacity :", font=("new time roman", 10, "bold"), width=15).place(x=100, y=80)
        file = open("Text/complicity.txt", 'r')
        data = file.read()
        file.close()
        self.CAP = Entry(self.cap_fream, font=("arial", 10, "bold"), bg='#81c3e5', width=22, fg='black')
        self.CAP.place(x=250, y=80)
        self.CAP.insert(0, data)

        self.setCpa_butt = Button(self.cap_fream,text="Update", fg="black", command=self.update_cap,
                                    font=("Pixelify Sans", 10, "bold"))
        self.setCpa_butt.place(x=270, y=120)

    def update_cap(self):
        file = open("Text/complicity.txt", 'w')
        file.truncate()
        file.seek(0)
        cap = self.CAP.get()
        file.write(cap)
        file.close()

    def add_camera(self):
        self.camera_fream = Frame(self.root, bd=5, padx=20, relief=RIDGE, bg="#a7d5ef")
        self.camera_fream.place(x=0, y=230, width=800, height=300)
        Label(self.camera_fream, text="ADD CAMERA", font=("arial", 10), relief=GROOVE, width=20, fg="black",
                      bg="#87ceeb").place(x=10, y=20)

        Label(self.camera_fream, text="Entry Camera :", font=("new time roman", 10, "bold"), width=15).place(x=100, y=80)
        self.Entery_cam = Entry(self.camera_fream, font=("arial", 10, "bold"), bg='#81c3e5', width=22, fg='black')
        self.Entery_cam.place(x=250, y=80)

        Label(self.camera_fream, text="Exit Camera :", font=("new time roman", 10, "bold"), width=15).place(x=100, y=130)
        self.Exit_cam = Entry(self.camera_fream, font=("arial", 10, "bold"), bg='#81c3e5', width=22, fg='black')
        self.Exit_cam.place(x=250, y=130)

        self.setCpa_butt = Button(self.camera_fream, text="Add Camera", fg="black", command=None,
                                  font=("Pixelify Sans", 10, "bold"))
        self.setCpa_butt.place(x=270, y=170)







