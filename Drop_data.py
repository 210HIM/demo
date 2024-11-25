from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql
import mysql.connector
from datetime import datetime

class drop_file:
    def __init__(self):
        self.root = None
        self.PWS = 'rakesh'

    def data(self, root):
        self.root = root

        self.title_boder = Frame(self.root, bg='#3c3f41', )
        self.title_boder.place(x=0, y=0, width=1230, height=30)
        Label(self.title_boder, text="Admin/Delete Record", font=("arial", 10, 'bold')).place(x=0, y=2, )

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                             font=('Calibri', 11))  # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading",
                             font=('Calibri', 13, 'bold'))  # Modify the font of the headings
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders


        self.Datafreame1 = Frame(self.root, bd=5, bg='#19232d', relief=RIDGE)
        self.Datafreame1.place(x=0, y=30, width=1000, height=500)

        self.Datafreame2 = Frame(self.root, padx=20, bg='#929292', relief=RIDGE)
        self.Datafreame2.place(x=0, y=530, width=1000, height=30)
        # --------------------------


        # --------------------
        # self.id = StringVar()
        # comNameTable = ttk.Combobox(self.Datafreame2, textvariable=self.id, font=("arial", 10, "bold"),
        #                             width=15)
        # self.db_conect()
        # comNameTable["values"] = list(set([i[0] for i in self.result]))
        # comNameTable.current(0)
        # comNameTable.place(x=320, y=2)
        #
        # Search = Button(self.Datafreame2, text='search', command=self.get_type, font=("arial", 8, "bold"),
        #                 fg="black")
        # Search.place(x=450, y=5, height=20, width=50)
        # -----

        self.db_conect()
        self.clicked = StringVar()
        self.clicked.set(self.result[0][0])
        drop = OptionMenu(self.Datafreame2, self.clicked, *list([i[0] for i in self.result]))
        drop.place(x=400, y=0)
        Search = Button(self.Datafreame2, text='search', command=self.get_type, font=("arial", 8, "bold"),
                        fg="black")
        Search.place(x=525, y=5, height=20, width=50)

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
        sql = "select * from anpr_final_db.owner_data"
        self.my_curser.execute(sql)
        self.result = self.my_curser.fetchall()
        self.conn.close()
        self.new_table(self.result)

    def new_table(self,result):
        # Add a Treeview widget
        tree = ttk.Treeview(self.Datafreame1, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=10,selectmode = "extended" ,style="mystyle.Treeview")
        tree.column("# 1",width=10,anchor="nw")
        tree.heading("# 1", text="ID")

        tree.column("# 2",width=100, anchor="nw")
        tree.heading("# 2", text="Vehicle Number")

        tree.column("# 3",width=100, anchor="nw")
        tree.heading("# 3", text="Entry Date")

        tree.column("# 4",width=100, anchor="nw")
        tree.heading("# 4", text="Entry Time")

        tree.column("# 5",width=100, anchor="nw")
        tree.heading("# 5", text="Exit Date")

        tree.column("# 6",width=100, anchor="nw")
        tree.heading("# 6", text="Exit Time")

        # print(result)
        for ind,val in enumerate(result):
            if ind % 2 != 0:
                tree.insert('', 'end',values=(ind+1,val[0],val[1],val[2],val[3],val[4]),tags=('even',))
            else:
                tree.insert('', 'end', values=(ind+1,val[0],val[1],val[2],val[3],val[4]),tags=('odd',))

        tree.tag_configure('odd', background='#E8E8E8')
        tree.tag_configure('even', background='#ffffff')

        self.y_scollbar = ttk.Scrollbar(self.Datafreame1,orient ="vertical",command = tree.yview)
        self.y_scollbar.place(x=1000, y=0,height=480)
        tree['yscroll'] = self.y_scollbar.set
        tree.place(width=1000, height=500)


    def get_type(self):
        #value = self.id.get()
        value = self.clicked.get()
        self.conn = mysql.connector.connect(username='root', host='localhost', password=self.PWS,
                                            database="anpr_final_db")
        self.my_curser = self.conn.cursor()
        sql = f"DELETE FROM `anpr_final_db`.`owner_data` WHERE (`Vehicle_number` = '{value}');"
        #print(sql)
        try:
            self.my_curser.execute(sql)
            self.conn.commit()
            self.db_conect()
            self.new_table(self.result)
        except:
            messagebox.showerror("Error","Not delete me")
        finally:
            self.conn.close()
#
# obj = drop_file()
# obj.data()
# mainloop()
