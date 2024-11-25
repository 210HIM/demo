from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql
import mysql.connector
from datetime import datetime


class Detels:
    def __init__(self):
        self.root = None
        self.result = None
        self.PWS = None
        self.PWS = 'rakesh'


    def data(self,root):
        self.root = root
        self.title_boder = Frame(self.root, bg='#3c3f41', )
        self.title_boder.place(x=0, y=0, width=1230, height=30)

        Label(self.title_boder, text="Admin/Entry&Exit Records", font=("arial", 10, 'bold')).place(x=0, y=2, )

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                             font=('Calibri', 12))  # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading",
                             font=('Calibri', 13, 'bold'))  # Modify the font of the headings
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.Datafreame1 = Frame(self.root, padx=20, relief=RIDGE)
        self.Datafreame1.place(x=0, y=30, width=1000, height=500)
        # --------------------------
        # search bar

        self.Search_text = Entry(self.Datafreame1, font=("arial", 10, "bold"), bg='#81c3e5', width=15, fg='black')
        self.Search_text.place(x=0, y=5, width=150, height=20)
        Search_butt = Button(self.Datafreame1, text='Search', command=self.Search, font=("arial", 8, "bold"),fg="black")
        Search_butt.place(x=152, y=5, height=20, width=50)

        # --------------------
        self.type_of_sort = StringVar()

        values= ["ALL", "Date", "Time", "Alphabet"]
        self.type_of_sort = StringVar()
        self.type_of_sort.set("ALL")
        drop = OptionMenu(self.Datafreame1, self.type_of_sort, *values)
        drop.place(x=210, y=0)
        Search = Button(self.Datafreame1, text='Sort', command=self.get_type, font=("arial", 8, "bold"),
                        fg="black")
        Search.place(x=280, y=5, height=20, width=50)


        # -----

        self.Datafreame2 = Frame(self.root, bd=2, bg='#19232d', highlightbackground="#47c5fe", highlightthickness=0)
        self.Datafreame2.place(x=0, y=60, width=1000, height=500)

        self.Datafreame3 = Frame(self.root, bd=2, bg='#929292')
        self.Datafreame3.place(x=0, y=560, width=1000, height=30)
        self.db_conect()


    def Search(self):
        number_plate = self.Search_text.get()
        number_plate = number_plate.upper()

        if len(number_plate) == 0:
            messagebox.showerror("Warning", "Data not filled.")

        if len(number_plate) > 10 or len(number_plate) < 10:
            messagebox.showerror("Warning", "Given data is not right formet.")

        self.conn = mysql.connector.connect(username='root', host='localhost', password=self.PWS,
                                            database="anpr_final_db")
        self.my_curser = self.conn.cursor()

        sql = f"SELECT * FROM anpr_final_db.rto where Vehicle_number = '{number_plate}';"

        try:
            self.my_curser.execute(sql)
            result = self.my_curser.fetchall()
        except:
            messagebox.showerror("WARNING", "Server not responding")
            return
        finally:
            self.conn.close()

        self.new_table(result)

    def get_type(self):
        data = []
        self.temp_copy = []
        if self.type_of_sort.get() == "ALL":
            self.new_table(self.result)

        if self.type_of_sort.get() == "Date":
            for i in self.result:
                data.append((i[2].strftime('%m/%d/%Y %I:%M%p')))
            sorted_lst = sorted(data, key=lambda x: datetime.strptime(x, '%m/%d/%Y %I:%M%p'))
            for i in sorted_lst:
                j = data.index(i)
                self.temp_copy.append(self.result[j])
            self.new_table(self.temp_copy)

        if self.type_of_sort.get() == "Time":
            for i in self.result:
                data.append((i[2].strftime('%m/%d/%Y %I:%M%p')))
            sorted_lst = sorted(data, key=lambda x: datetime.strptime(x, '%m/%d/%Y %I:%M%p'))
            for i in sorted_lst:
                j = data.index(i)
                self.temp_copy.append(self.result[j])
            self.new_table(self.temp_copy[::-1])

    def db_conect(self):
        self.conn = mysql.connector.connect(username='root', host='localhost', password=self.PWS,
                                            database="anpr_final_db")
        self.my_curser = self.conn.cursor()
        sql = "select * from anpr_final_db.rto"
        self.my_curser.execute(sql)
        self.result = self.my_curser.fetchall()
        self.conn.close()
        self.new_table(self.result)

    def new_table(self, result):
        # Add a Treeview widget
        tree = ttk.Treeview(self.Datafreame2, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=18,
                            selectmode="extended", style="mystyle.Treeview")
        tree.column("# 1", width=20, anchor="nw")
        tree.heading("# 1", text="ID")

        tree.column("# 2", width=150, anchor="nw")
        tree.heading("# 2", text="Vehicle Number")

        tree.column("# 3", width=150, anchor="nw")
        tree.heading("# 3", text="Entry Date")

        tree.column("# 4", width=150, anchor="nw")
        tree.heading("# 4", text="Entry Time")

        tree.column("# 5", width=150, anchor="nw")
        tree.heading("# 5", text="Exit Date")

        tree.column("# 6", width=150, anchor="nw")
        tree.heading("# 6", text="Exit Time")

        #print(result)
        for ind, val in enumerate(result):

            data_1 = val[2]
            # date_1, time_1 = data_1.split(' ')
            # time_1 = time_1[:8]

            date_1 = data_1.strftime("%d-%b-%Y")
            time_1 = data_1.strftime("%H:%M:%S:%p")

            data_2 = val[3]
            # date_2, time_2 = data_2.split(' ')
            # time_2 = time_2[:8]

            if data_2 != None:
                date_2 = data_2.strftime("%d-%b-%Y")
                time_2 = data_2.strftime("%H:%M:%S:%p")
            else:
                date_2 = None
                time_2 = None

            if ind % 2 != 0:
                tree.insert('', 'end', text=val[0], values=(ind + 1, val[1], date_1, time_1, date_2, time_2),
                            tags=('even',))
            else:
                tree.insert('', 'end', text=val[0], values=(ind + 1, val[1], date_1, time_1, date_2, time_2),
                            tags=('odd',))

        tree.tag_configure('odd', background='#E8E8E8')
        tree.tag_configure('even', background='#ffffff')

        self.y_scollbar = ttk.Scrollbar(self.Datafreame2, orient="vertical", command=tree.yview)
        self.y_scollbar.place(x=980, y=0, height=480)
        tree['yscroll'] = self.y_scollbar.set
        tree.place(width=1000, height=500)

#
# obj = Detels()
# obj.data()
# mainloop()