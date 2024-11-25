from tkinter import *  # GUI python Lib
from tkinter import messagebox  # GUI python Lib
from tkinter import ttk
import mysql  # Python LIb for Databace
import mysql.connector  # Python Lib for Databace connection


class Edit_vhi:
    def _init_(self):
        self.root = None
        self.PWS = 'rakesh'


    def find_vhi(self,root):
        self.root = root
        self.title_boder = Frame(self.root, bg='#3c3f41', )
        self.title_boder.place(x=0, y=0, width=1230, height=30)
        Label(self.title_boder, text="Admin/Edit User Profile", font=("arial", 10, 'bold')).place(x=0, y=2, )

        self.Datafreame1 = Frame(self.root, bd=5, padx=20, relief=RIDGE, bg='#a7d5ef')
        self.Datafreame1.place(x=0, y=30, width=400, height=170)

        Label(self.Datafreame1, text="Find Vhical ", font=("new time roman", 10), relief=GROOVE, fg="black",
                     bg="#87ceeb", width=15).place(x=100, y=10)

        vehicle_id = Label(self.Datafreame1, text="Vehicle Num :", font=("new time roman", 10, "bold"), width=15)
        vehicle_id.place(x=15, y=60)

        # self.id = StringVar()
        # comNameTable = ttk.Combobox(self.Datafreame1, textvariable=self.id, font=("arial", 10, "bold"),
        #                             width=15)
        # result = self.db_conect()
        # comNameTable["values"] = ([i[0] for i in result])
        # comNameTable.current(0)
        # comNameTable.place(x=150, y=60)

        self.result = self.db_conect()
        self.clicked = StringVar()
        self.clicked.set(self.result[0][0])
        drop = OptionMenu(self.Datafreame1, self.clicked, *list([i[0] for i in self.result]))
        drop.place(x=150, y=60)
        Search = Button(self.Datafreame1, text='search', command=self.get_data, font=("arial", 8, "bold"),
                        fg="black")
        Search.place(x=190, y=110)

    def db_conect(self):
        conn = mysql.connector.connect(host="localhost", username="root", password='rakesh', database="anpr_final_db")
        my_cursor = conn.cursor()
        sql = f"SELECT * FROM anpr_final_db.owner_data;"
        my_cursor.execute(sql)
        result = my_cursor.fetchall()
        return result

    def get_data(self):
        self.msg = str(self.clicked.get())
        conn = mysql.connector.connect(host="localhost", username="root", password='rakesh', database="anpr_final_db")
        my_cursor = conn.cursor()
        sql = f"SELECT * FROM anpr_final_db.owner_data where Vehicle_number = '{self.msg}';"
        try:
            my_cursor.execute(sql)
            self.result = my_cursor.fetchall()
        except:
            messagebox.showwarning('Warning', "Server not responding 🚬🔌")
            self.clearFrame(self.Datafreame1)
            self.find_vhi(self.root)
        finally:
            conn.close()

        if len(self.result) == 0:
            messagebox.showwarning('Warning', "Vehicle is not present 🚬")
            self.clearFrame(self.Datafreame1)
            self.find_vhi(self.root)
        else:
            self.result = list(self.result[0])

        if self.msg in self.result:
            messagebox.showinfo('Information', "The data should be filled with great care as it will not be returned.")
            self.clearFrame(self.Datafreame1)
            self.Edit_vhi_data()
        else:
            messagebox.showwarning('Warning', "Vehicle is not present 🚬")
            self.clearFrame(self.Datafreame1)
            self.find_vhi(self.root)


    def Edit_vhi_data(self):

        self.Datafreame1.config(bg='#a7d5ef')
        self.Datafreame1.place(x=0, y=30, width=400, height=390)

        note = Label(self.Datafreame1, text="Edit Details ", font=("new time roman", 10, "bold"), relief=GROOVE,
                     fg="black", bg="#87ceeb", width=25)
        note.grid(row=0, column=0, columnspan=2)

        vehicle_id = Label(self.Datafreame1, text="Vehicle Num :", font=("new time roman", 10, "bold"), width=15)
        vehicle_id.grid(row=1, column=0, padx=8, pady=15)

        vehicle_id_show = Label(self.Datafreame1, text=self.msg, font=("new time roman", 10, "bold"), width=15)
        vehicle_id_show.grid(row=1, column=1, padx=10, pady=15)

        name = Label(self.Datafreame1, text="Owner name :", font=("new time roman", 10, "bold"), width=15)
        name.grid(row=2, column=0, padx=8, pady=15)

        email_id = Label(self.Datafreame1, text="Email Id :", font=("new time roman", 10, "bold"), width=15)
        email_id.grid(row=3, column=0, padx=8, pady=15)

        mobile_num = Label(self.Datafreame1, text="Mobile number :", font=("new time roman", 10, "bold"), width=15)
        mobile_num.grid(row=4, column=0, padx=8, pady=15)

        address = Label(self.Datafreame1, text="Address :", font=("new time roman", 10, "bold"), width=15)
        address.grid(row=5, column=0, padx=8, pady=15)

        # entry....
        self.Name_entry = Entry(self.Datafreame1, font=("arial", 10, "bold"), bg='#81c3e5', width=22, fg='black')
        self.Name_entry.grid(row=2, column=1, padx=5)
        self.Name_entry.insert(0, self.result[1])

        self.email_id_entry = Entry(self.Datafreame1, font=("arial", 10, "bold"), bg='#81c3e5', width=22, fg='black')
        self.email_id_entry.grid(row=3, column=1, padx=5)
        self.email_id_entry.insert(0, self.result[3])

        self.mobile_num_entry = Entry(self.Datafreame1, font=("arial", 10, "bold"), bg='#81c3e5', width=22, fg='black')
        self.mobile_num_entry.grid(row=4, column=1, padx=5)
        self.mobile_num_entry.insert(0, self.result[2])

        self.address_entry = Entry(self.Datafreame1, font=("arial", 10, "bold"), bg='#81c3e5', width=22, fg='black')
        self.address_entry.grid(row=5, column=1, padx=5)
        self.address_entry.insert(0, self.result[4])

        self.submit_button = Button(self.Datafreame1, text="Update", fg="black", command=self.Ed_get_data)
        self.submit_button.grid(row=6, column=1, pady=10, sticky=W + E)

        self.submit_button = Button(self.Datafreame1, text="Back", fg="black", command=self.back)
        self.submit_button.grid(row=7, column=3, pady=10, sticky=W + E)


    def Ed_get_data(self):
        name = self.Name_entry.get()
        mobile_num = self.mobile_num_entry.get()
        address = self.address_entry.get()
        email_id = self.email_id_entry.get()

        if name == '':
            name = self.result[1]

        if mobile_num == '':
            mobile_num = self.result[3]

        if address == '':
            address = self.result[4]

        if email_id == '':
            email_id = self.result[2]

        conn = mysql.connector.connect(host="localhost", username="root", password="rakesh", database="anpr_final_db")
        my_cursor = conn.cursor()

        q2 = f"UPDATE `anpr_final_db`.`owner_data` SET `owner_name` = '{name}', `mobile_num` = '{mobile_num}', `email_id` = '{email_id}', `address` = '{address}' WHERE (`Vehicle_number` = '{self.msg}');"

        data = (name, mobile_num, email_id, address, self.msg)
        # print(data)
        # print(q2)
        ans = messagebox.askquestion("Informetion", "Do you want to update profile.")
        if ans == "yes":
            try:
                my_cursor.execute(q2)
                conn.commit()
                messagebox.showinfo('information', "Your profile has been updated.")
                self.clearFrame(self.Datafreame1)
                self.clearFrame(self.root)
                self.find_vhi(self.root)
            except:
                messagebox.showwarning('Warning', "Server not responding")
            finally:
                conn.close()
        else:
            self.clearFrame(self.Datafreame1)
            self.clearFrame(self.root)
            self.find_vhi(self.root)

    def back(self):
        self.clearFrame(self.Datafreame1)
        self.clearFrame(self.root)
        self.find_vhi(self.root)

    def clearFrame(self, frame):
        # destroy all widgets from frame
        for widget in frame.winfo_children():
            widget.destroy()

        # this will clear frame and frame will be empty
        # if you want to hide the empty panel then
        frame.pack_forget()


# obj = Edit_vhi()
# obj.find_vhi()
# mainloop()






