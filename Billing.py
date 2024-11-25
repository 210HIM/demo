from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql
import mysql.connector
from datetime import datetime

class GenreatBill:
    def __init__(self):
        self.id = None
        self.result = None
        self.conn = None
        self.my_curser = None
        self.root = None
        self.PWS = 'rakesh'

    def Bile(self, root):
        self.root = root
        self.title_boder = Frame(self.root, bg='#3c3f41', )
        self.title_boder.place(x=0, y=0, width=1230, height=30)
        Label(self.title_boder, text="Admin/View Bills", font=("arial", 10, 'bold')).place(x=0, y=2, )

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                             font=('Calibri', 11))  # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading",
                             font=('Calibri', 13, 'bold'))  # Modify the font of the headings
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.Datafreame1 = Frame(self.root, bd=5, bg='#19232d', relief=RIDGE)
        self.Datafreame1.place(x=0, y=60, width=1000, height=500)

        self.Datafreame2 = Frame(self.root, padx=20, relief=RIDGE)
        self.Datafreame2.place(x=0, y=30, width=1000, height=30)

        self.id = StringVar()
        # comNameTable_1= ttk.Combobox(self.Datafreame2, textvariable=self.id, font=("arial", 10, "bold"),
        #                             width=15)

        # comNameTable_1["values"] =([i[0] for i in self.result])
        # comNameTable_1.current(0)
        # comNameTable_1.place(x=300, y=5)
        # self.id = Entry(self.Datafreame2,font=("arial", 10, "bold"))
        # self.id.place(x=0, y=5)
        # Search = Button(self.Datafreame2, text='search', command=self.get_type, font=("arial", 8, "bold"),
        #                       fg="black")
        # Search.place(x=450, y=5, height=20, width=50)
        # -----
        self.db_conect()
        self.clicked = StringVar()
        self.clicked.set(self.result[0][0])
        drop = OptionMenu(self.Datafreame2, self.clicked, *list([i[0] for i in self.result]))
        drop.place(x=400,y=0)
        Search = Button(self.Datafreame2, text='search', command=self.get_type, font=("arial", 8, "bold"),
                        fg="black")
        Search.place(x=470, y=5, height=20, width=50)



    def set_data(self):
        temp = []
        self.db_conect()
        for i in self.result:
            if i[0] != '':
                temp.append(i[0])
        # self.comNameTable["values"] = temp
        return temp


    def db_conect(self):
        self.conn = mysql.connector.connect(username = 'root', host ='localhost', password = self.PWS,database = "anpr_final_db")
        self.my_curser = self.conn.cursor()
        sql = "select * from anpr_final_db.billes"
        self.my_curser.execute(sql)
        self.result = self.my_curser.fetchall()
        self.conn.close()
        self.new_table(self.result)
        #print(self.result)

    def new_table(self,result):
        # Add a Treeview widget
        tree = ttk.Treeview(self.Datafreame1, column=("c1", "c2", "c3",'c4'), show='headings', height=10,
                            selectmode = "extended" ,style="mystyle.Treeview")
        tree.column("# 1",width=10,anchor="nw")
        tree.heading("# 1", text="ID")

        tree.column("# 2",width=100, anchor="nw")
        tree.heading("# 2", text="Bill ID")

        tree.column("# 3",width=100, anchor="nw")
        tree.heading("# 3", text="Vehicle Number")

        tree.column("# 4", width=100, anchor="nw")
        tree.heading("# 4", text="Entry Date")

        for ind, val in enumerate(result):

            data_1 = val[3]
            # date_1, time_1 = data_1.split(' ')
            # time_1 = time_1[:8]

            date_1 = data_1.strftime("%d-%b-%Y")
            time_1 = data_1.strftime("%H:%M:%S:%p")

            data_2 = val[4]
            # date_2, time_2 = data_2.split(' ')
            # time_2 = time_2[:8]

            if data_2 != None:
                date_2 = data_2.strftime("%d-%b-%Y")
                time_2 = data_2.strftime("%H:%M:%S:%p")
            else:
                date_2 = None
                time_2 = None

        # print(result)
            if ind % 2 != 0:
                tree.insert('', 'end', text=val[0], values=(ind + 1, val[0], val[2], date_1),
                            tags=('even',))
            else:
                tree.insert('', 'end', text=val[0], values=(ind + 1, val[0], val[2], date_1),
                            tags=('odd',))

        tree.tag_configure('odd', background='#E8E8E8')
        tree.tag_configure('even', background='#ffffff')

        self.y_scollbar = ttk.Scrollbar(self.Datafreame1,orient ="vertical",command = tree.yview)
        self.y_scollbar.place(x=980, y=0,height=485)
        tree['yscroll'] = self.y_scollbar.set
        tree.place(width=1000, height=500)


    def get_type(self):
        # number_plate = str(self.id.get())
        number_plate= self.clicked.get()
        self.conn = mysql.connector.connect(username='root', host='localhost', password='rakesh',
                                            database="anpr_final_db")
        self.my_curser = self.conn.cursor()

        sql = f"SELECT * FROM anpr_final_db.billes where bill_id = '{number_plate}';"
        #print(sql)
        try:
            self.my_curser.execute(sql)
            self.result = self.my_curser.fetchall()
            self.clearFrame(self.Datafreame1)
            self.clearFrame(self.Datafreame2)
            #print(self.result)
            self.create_bill(self.result[0])


        except():
            messagebox.showerror("WARNING", "Server not responding")
        finally:
            self.conn.close()

    def clearFrame(self, frame):
        # destroy all widgets from frame
        for widget in frame.winfo_children():
            widget.destroy()

        # this will clear frame and frame will be empty
        # if you want to hide the empty panel then
        frame.pack_forget()

    def create_bill(self, result):
        day, mini = self.difference(result[3], result[4])
        x = self.amount_calculate(day,mini)
        if x > 0:
            amount = x+(x*(18//100))
        else:
            amount = x
        self.Datafreame1.config(bg='#ffffff', bd=0)
        self.Datafreame1.place(x=0, y=30, width=300, height=400)

        self.Datafreame2.config(bg='#f7f7f3', bd=0)
        self.Datafreame2.place(x=0, y=430, width=300, height=30)

        Label(self.Datafreame1, text="Parking Bill", font=("Young Serif", 13, "bold"),
                     fg="black", bg='#ffffff').place(x=100, y=10)

        name = Label(self.Datafreame1, text=result[0], font=("new time roman", 10, "bold"), width=15, bg='#ffffff')
        name.place(x=90, y=50)

        Label(self.Datafreame1, text="=== ==== === === === === === === === ==", font=("new time roman", 10, "bold"),
              bg='#ffffff').place(x=5, y=70)

        name = Label(self.Datafreame1, text="CAR PARK:", font=("new time roman", 10, "bold"), width=15, bg='#ffffff')
        name.place(x=10, y=100)

        show_NUM_PLATE = Label(self.Datafreame1, text=result[2], font=("new time roman", 10, "bold"), width=15,
                               bg='#ffffff')
        show_NUM_PLATE.place(x=150, y=100)

        DATE = Label(self.Datafreame1, text="     DATE:", font=("new time roman", 10, "bold"), width=15, bg='#ffffff')
        DATE.place(x=10, y=140)

        show_date = Label(self.Datafreame1, text=datetime.now().strftime("%d-%b-%Y/%H:%M"), font=("new time roman", 8, "bold"), width=15,
                          bg='#ffffff')
        show_date.place(x=150, y=140)

        From = Label(self.Datafreame1, text="  FROM:", font=("new time roman", 10, "bold"), width=15, bg='#ffffff')
        From.place(x=10, y=180)

        show_From = Label(self.Datafreame1, text=result[3].strftime("%d-%b-%Y/%H:%M"), font=("new time roman", 8, "bold"), width=15, bg='#ffffff')
        show_From.place(x=150, y=180)

        TO = Label(self.Datafreame1, text="      TO:", font=("new time roman", 10, "bold"), width=15, bg='#ffffff')
        TO.place(x=10, y=220)

        show_TO = Label(self.Datafreame1, text=result[4].strftime("%d-%b-%Y/%H:%M"), font=("new time roman", 8, "bold"), width=15,
                          bg='#ffffff')
        show_TO.place(x=150, y=220)

        Label(self.Datafreame1,text="=== ==== === === === === === === === ==",font=("new time roman", 10, "bold"),
              bg='#ffffff').place(x=5, y=245)

        Amount = Label(self.Datafreame1, text="AMOUNT:", font=("new time roman", 10, "bold"), width=15, bg='#ffffff')
        Amount.place(x=10, y=270)

        show_Amount = Label(self.Datafreame1, text=str(amount), font=("new time roman", 10, "bold"), width=15,
                          bg='#ffffff')
        show_Amount.place(x=150, y=270)

        gst = Label(self.Datafreame1, text="G.S.T:", font=("new time roman", 10, "bold"), width=15, bg='#ffffff')
        gst.place(x=10, y=290)

        show_gst = Label(self.Datafreame1, text="18%", font=("new time roman", 10, "bold"), width=15,
                          bg='#ffffff')
        show_gst.place(x=150, y=290)

        Label(self.Datafreame1, text=result[-1], font=("new time roman", 10, "bold"),
              bg='#ffffff').place(x=65, y=330)

        Label(self.Datafreame1, text="THANK YOU AND DRIVE SAFELY!!", font=("new time roman", 10, "bold"),
              bg='#ffffff').place(x=35, y=360)

        back_but = Button(self.Datafreame2, text='Back', font=("Young Serif", 9, "bold"), bg='#f7f7f3', fg='black',
                         command=self.back)
        back_but.place(x=230, y=2)

    def back(self):
        self.clearFrame(self.Datafreame1)
        self.clearFrame(self.Datafreame2)
        self.Bile(self.root)

    def difference(self, Entry_date, Exit_date):
        first_time = Entry_date
        later_time = Exit_date

        diff = later_time - first_time
        minutes, seconds = divmod(diff.total_seconds(), 60)
        f = first_time.strftime("%Y-%m-%d")
        l = later_time.strftime("%Y-%m-%d")
        days = self.days_between(f, l)
        return days, int(minutes)

    def days_between(self, date1, date2):
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((d2 - d1).days)

    def db_data(self):
        self.conn = mysql.connector.connect(username='root', host='localhost', password='rakesh',
                                            database="anpr_final_db")
        self.my_curser = self.conn.cursor()
        sql = "select * from anpr_final_db.price"
        self.my_curser.execute(sql)
        result = self.my_curser.fetchall()
        self.conn.close()
        return list(result[-1])

    def amount_calculate(self,d,m):
        self.result=self.db_data()
        p_hour = self.result[0]
        p_day =self.result[1]
        p_week = self.result[2]
        p_month1 = self.result[3]
        p_month3 = self.result[4]
        p_month6 = self.result[5]
        p_year = self.result[6]
        p_guest = self.result[7]

        amount = 0
        if m > 0:
            amount = m * p_hour

        if d == 0 or m == 0:
            return amount

        if 1 <= d <= 7:
            return amount + (d * p_day)
        elif 7 <= d < 30:
            x = d // 7
            amount = (p_week * x) + (d - (x * 7)) * p_hour + amount
            return amount
        elif 30 <= d <= 90:
            x = d // 30
            amount = (p_month1 * x) + (d - (x * 7)) * p_hour + amount
            return amount
        elif 90 <= d <= 180:
            x = d // 30
            amount = (p_month3 * x) + (d - (x * 7)) * p_hour + amount
            return amount
        elif 180 <= d <= 365:
            x = d // 30
            amount = (p_month6 * x) + (d - (x * 7)) * p_hour + amount
            return amount
        elif d > 365:
            return (amount // 365) * p_year











#
# obj = drop_file()
# obj.data()
# mainloop()
