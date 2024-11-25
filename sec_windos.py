from Admin import *
from Vch_rec import *
from register_user import *
from new_reg import *
from Drop_data import *
from Edit_vhi_info import *
from Billing import *
from Menuale import *
from Seting import *
from Analysis import *
from Price import *

class Windos:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1590x1000")
        self.root.title("Admin/functions")
        self.root.state("zoomed")

        self.title_fraem = Frame(self.root, bd=5, bg='#47c5fe')
        self.title_fraem.place(height=80, width=1590, x=0, y=0)

        Label(self.title_fraem, text="Admin", font=("arial", 18, "bold"),bg='#47c5fe').place(x=30 , y=15)
        self.datafream1 = Frame(self.root, bd=5, bg='#222d31')
        self.datafream1.place(height=800, width=300, x=0, y=80)

        self.datafream2 = Frame(self.root, bd=5, highlightbackground="black", highlightthickness=2)
        self.datafream2.place(height=720, width=1230, x=300, y=80)


    def button(self):
        Button_1 = Button(self.datafream1, text="Record's", font=("arial", 10, "bold"), fg="#e0e1e3", bg="#57737d", width=20,
                          command=self.ButtonOne)
        Button_1.grid(row=1, column=2, padx=50, pady=15)
        self.changeOnHover(Button_1, '#e0e1e3', '#57737d')

        Button_2 = Button(self.datafream1, text="User's", font=("arial", 10, "bold"), fg="#e0e1e3", bg="#57737d", width=20,
                          command=self.ButtonTwo)
        Button_2.grid(row=2, column=2, padx=35, pady=15)
        self.changeOnHover(Button_2, '#e0e1e3', '#57737d')

        Button_3 = Button(self.datafream1, text="New registration ", font=("arial", 10, "bold"), fg="#e0e1e3",
                          bg="#57737d", width=20, command=self.ButtonTree)
        Button_3.grid(row=3, column=2, padx=35, pady=15)
        self.changeOnHover(Button_3, '#e0e1e3', '#57737d')

        Button_4 = Button(self.datafream1, text="Delete user", font=("arial", 10, "bold"), fg="#e0e1e3", bg="#57737d", width=20,
                          command=self.ButtonFore)
        Button_4.grid(row=4, column=2, padx=35, pady=15)
        self.changeOnHover(Button_4, '#e0e1e3', '#57737d')

        Button_5 = Button(self.datafream1, text="Edit Info", font=("arial", 10, "bold"), fg="#e0e1e3", bg="#57737d", width=20,
                          command=self.ButtonFive)
        Button_5.grid(row=5, column=2, padx=35, pady=15)
        self.changeOnHover(Button_5, '#e0e1e3', '#57737d')

        Button_6 = Button(self.datafream1, text="Pricing", font=("arial", 10, "bold"), fg="#e0e1e3", bg="#57737d",
                          width=20,command=self.ButtonSix)
        Button_6.grid(row=6, column=2, padx=35, pady=15)
        self.changeOnHover(Button_6, '#e0e1e3', '#57737d')

        Button_7 = Button(self.datafream1, text="Billing", font=("arial", 10, "bold"), fg="#e0e1e3", bg="#57737d",
                          width=20, command=self.ButtonSeven)
        Button_7.grid(row=7, column=2, padx=35, pady=15)
        self.changeOnHover(Button_7, '#e0e1e3', '#57737d')

        Button_8 = Button(self.datafream1, text="Analysis", font=("arial", 10, "bold"), fg="#e0e1e3", bg="#57737d",
                          width=20,command= self.ButtonAthe)
        Button_8.grid(row=8, column=2, padx=35, pady=10)
        self.changeOnHover(Button_8, '#e0e1e3', '#57737d')

        Button_9 = Button(self.datafream1, text="Manuele", font=("arial", 10, "bold"), fg="#e0e1e3", bg="#57737d",
                          width=20,command=self.ButtonNine)
        Button_9.grid(row=9, column=2, padx=35, pady=15)
        self.changeOnHover(Button_9, '#e0e1e3', '#57737d')

        Button_10 = Button(self.datafream1, text="Seating", font=("arial", 10, "bold"), fg="#e0e1e3", bg="#57737d",
                           width= 20, command=self.ButtonTem)
        Button_10.grid(row=10, column=2, padx=35, pady=15)
        self.changeOnHover(Button_10, '#e0e1e3', '#57737d')

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover, fg="black"))
        button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave, fg="#e0e1e3"))

    def ButtonOne(self):
        self.datafream2.config(bg='#5b8aa8')
        self.clearFrame(self.datafream2)
        self.root.state("zoomed")
        obj = Detels()
        obj.data(self.datafream2)

    def ButtonTwo(self):
        self.datafream2.config(bg='#5b8aa8')
        self.clearFrame(self.datafream2)
        obj_2 = Find()
        obj_2.data(self.datafream2)

    def ButtonTree(self):
        self.datafream2.config(bg='#5b8aa8')
        self.clearFrame(self.datafream2)
        obj_3 = new_memb()
        obj_3.add_new_vhi(self.datafream2)

    def ButtonFore(self):
        self.datafream2.config(bg='#5b8aa8')
        self.clearFrame(self.datafream2)
        obj_4 = drop_file()
        obj_4.data(self.datafream2)

    def ButtonFive(self):
        self.datafream2.config(bg='#5b8aa8')
        self.clearFrame(self.datafream2)
        obj_5 = Edit_vhi()
        obj_5.find_vhi(self.datafream2)

    def ButtonSix(self):
        self.datafream2.config(bg='#5b8aa8')
        self.clearFrame(self.datafream2)
        obj6 = SET_Price()
        obj6.set(self.datafream2)


    def ButtonSeven(self):
        self.datafream2.config(bg='#5b8aa8')
        self.clearFrame(self.datafream2)
        obj_7 = GenreatBill()
        obj_7.Bile(self.datafream2)

    def ButtonAthe(self):
        self.datafream2.config(bg='#5b8aa8')
        self.clearFrame(self.datafream2)
        obj8 =Data_Analysis()
        obj8.Analysis(self.datafream2)

    def ButtonNine(self):
        self.datafream2.config(bg= '#5b8aa8')
        self.clearFrame(self.datafream2)
        obj9 = Menual()
        obj9.informetion(self.datafream2)

    def ButtonTem(self):
        self.datafream2.config(bg='#5b8aa8')
        self.title_fraem.config()
        self.clearFrame(self.datafream2)
        obj10=Additional()
        obj10.add_capicity(self.datafream2, self.title_fraem)
        obj10.add_camera()


    def clearFrame(self, frame):
        # destroy all widgets from frame
        for widget in frame.winfo_children():
            widget.destroy()

        # this will clear frame and frame will be empty
        # if you want to hide the empty panel then
        frame.pack_forget()





obj = Windos()
obj.button()
mainloop()