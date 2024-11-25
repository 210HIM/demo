from tkinter import *
from tkinter import messagebox
import mysql
import mysql.connector


class SET_Price:
    def __init__(self):
        self.my_curser = None
        self.title_boder = None
        self.root = None
        self.conn = None
        self.p_hour = None
        self.p_day = None
        self.p_week = None
        self.p_month1 = None
        self.p_month3 = None
        self.p_month6 = None
        self.p_year = None
        self.p_guest = None

        self.result = None
        self.data = None

    def set(self, root):
        self.root = root
        self.db_data()
        self.data = self.result[-1]
        self.title_boder = Frame(self.root, bg='#3c3f41', )
        self.title_boder.place(x=0, y=0, width=1230, height=30)
        Label(self.title_boder, text="Admin/Set Price", font=("arial", 10, 'bold')).place(x=0, y=2, )

        self.datafream = Frame(self.root, bd=5, padx=20, relief=RIDGE, bg="#a7d5ef")
        self.datafream.place(x=0, y=30, width=600, height=600)

        Label(self.datafream,text='Set Price',font=("arial", 10), relief=GROOVE, width=20, fg="black",
                      bg="#87ceeb").grid(row=1, columnspan=2, padx=10, pady=15)

        name = Label(self.datafream, text="One Hour:", font=("new time roman", 10, "bold"), width=15)
        name.grid(row=2, column=0, padx=10, pady=15)
        self.p_hour = Entry(self.datafream, font=("arial", 10, "bold"), bg='#81c3e5', width=22, fg='black')
        self.p_hour.grid(row=2, column=2, padx=15)
        self.p_hour.insert(0, self.data[0])
        name = Label(self.datafream, text="/hour", font=("new time roman", 9), width=12)
        name.grid(row=2, column=3, padx=10, pady=15)

        name = Label(self.datafream, text="One Day:", font=("new time roman", 10, "bold"), width=15)
        name.grid(row=3, column=0, padx=10, pady=15)
        self.p_day = Entry(self.datafream, font=("arial", 10, "bold"), bg='#81c3e5', width=22, fg='black')
        self.p_day.grid(row=3, column=2, padx=5)
        self.p_day.insert(0, self.data[1])
        name = Label(self.datafream, text="/day", font=("new time roman", 9), width=12)
        name.grid(row=3, column=3, padx=10, pady=15)

        name = Label(self.datafream, text="One Week:", font=("new time roman", 10, "bold"), width=15)
        name.grid(row=4, column=0, padx=10, pady=15)
        self.p_week = Entry(self.datafream, font=("arial", 10, "bold"), bg='#81c3e5', width=22, fg='black')
        self.p_week.grid(row=4, column=2, padx=5)
        self.p_week.insert(0, self.data[2])
        name = Label(self.datafream, text="/week", font=("new time roman", 9), width=12)
        name.grid(row=4, column=3, padx=10, pady=15)

        name = Label(self.datafream, text="One Month :", font=("new time roman", 10, "bold"), width=15)
        name.grid(row=5, column=0, padx=10, pady=15)
        self.p_month1 = Entry(self.datafream, font=("arial", 10, "bold"), bg='#81c3e5', width=22, fg='black')
        self.p_month1.grid(row=5, column=2, padx=5)
        self.p_month1.insert(0, self.data[3])
        name = Label(self.datafream, text="/month", font=("new time roman", 9), width=12)
        name.grid(row=5, column=3, padx=10, pady=15)

        name = Label(self.datafream, text="Three  Month's ", font=("new time roman", 10, "bold"), width=15)
        name.grid(row=6, column=0, padx=10, pady=15)
        self.p_month3 = Entry(self.datafream, font=("arial", 10, "bold"), bg='#81c3e5', width=22, fg='black')
        self.p_month3.grid(row=6, column=2, padx=5)
        self.p_month3.insert(0, self.data[4])
        name = Label(self.datafream, text="/3month", font=("new time roman", 9), width=12)
        name.grid(row=6, column=3, padx=10, pady=15)

        name = Label(self.datafream, text="Six Month's :", font=("new time roman", 10, "bold"), width=15)
        name.grid(row=7, column=0, padx=10, pady=15)
        self.p_month6 = Entry(self.datafream, font=("arial", 10, "bold"), bg='#81c3e5', width=22, fg='black')
        self.p_month6.grid(row=7, column=2, padx=5)
        self.p_month6.insert(0, self.data[5])
        name = Label(self.datafream, text="/6month", font=("new time roman", 9), width=12)
        name.grid(row=7, column=3, padx=10, pady=15)

        name = Label(self.datafream, text="One year :", font=("new time roman", 10, "bold"), width=15)
        name.grid(row=8, column=0, padx=10, pady=15)
        self.p_year = Entry(self.datafream, font=("arial", 10, "bold"), bg='#81c3e5', width=22, fg='black')
        self.p_year.grid(row=8, column=2, padx=5)
        self.p_year.insert(0, self.data[6])
        name = Label(self.datafream, text="/year", font=("new time roman", 9), width=12)
        name.grid(row=8, column=3, padx=10, pady=15)

        name = Label(self.datafream, text="G.S.T :", font=("new time roman", 10, "bold"), width=15)
        name.grid(row=9, column=0, padx=10, pady=15)
        self.p_guest = Entry(self.datafream, font=("arial", 10, "bold"), bg='#81c3e5', width=22, fg='black')
        self.p_guest.grid(row=9, column=2, padx=5)
        self.p_guest.insert(0, self.data[7])
        name = Label(self.datafream, text="amount", font=("new time roman", 9), width=12)
        name.grid(row=9, column=3, padx=10, pady=15)

        self.set = Button(self.datafream, text="set price", fg="black", command=self.set_price_db,
                                  font=("Pixelify Sans", 10, "bold"))
        self.set.grid(row=10, column=2)

    def set_price_db(self):
        p_hour = int(self.p_hour.get())
        p_day = int(self.p_day.get())
        p_week = int(self.p_week.get())
        p_mount1 = int(self.p_month1.get())
        p_mount3 = int(self.p_month3.get())
        p_mount6 = int(self.p_month6.get())
        p_year = int(self.p_year.get())
        p_guest = int(self.p_guest.get())

        # print(p_hour, p_day, p_week, p_mount1, p_mount3, p_mount6, p_year, p_guest)
        self.conn = mysql.connector.connect(username='root', host='localhost', password='rakesh',
                                            database="anpr_final_db")
        self.my_curser = self.conn.cursor()
        sql = f"INSERT INTO `anpr_final_db`.`price`(`hour`, `day`, `week`, `month1`, `month2`, `month3`, `year`, `guest`)" \
              f" VALUES({p_hour}, {p_day}, {p_week}, {p_mount1}, {p_mount3}, {p_mount6}, {p_year}, {p_guest});"
        # print(sql)

        try:
            self.my_curser.execute(sql)
            self.conn.commit()
            messagebox.showinfo('Updated',"Price List is updated")
        except():
            messagebox.showerror('Error',"Server Problem Data not updated, Try after some time.")
        finally:
            self.conn.close()


    def db_data(self):
        self.conn = mysql.connector.connect(username='root', host='localhost', password='rakesh',
                                            database="anpr_final_db")
        self.my_curser = self.conn.cursor()
        sql = "select * from anpr_final_db.price"
        self.my_curser.execute(sql)
        self.result = self.my_curser.fetchall()
        self.conn.close()

