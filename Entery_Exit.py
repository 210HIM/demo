from datetime import datetime
from tkinter import messagebox
import mysql.connector


def add_pass():
    try:
        file = open("Text/password.txt", 'r')
        PWS = file.read()
        file.close()
        return PWS
    except:
        print("Password not get")

def update_capicity(val):
    if val == True:
        file = open("Text/avil_cap.txt", 'r')
        file.seek(0)
        data = int(file.read())
        file.close()

        file = open("Text/avil_cap.txt", 'w')
        data = data + 1
        file.truncate()
        file.write(str(data))
        file.close()

    else:
        file = open("Text/avil_cap.txt", 'r')
        file.seek(0)
        data = int(file.read())
        file.close()

        file = open("Text/avil_cap.txt", 'w')
        data = data - 1
        file.truncate()
        file.write(str(data))
        file.close()



def update_entry_get(number_p):
    PWS = add_pass()
    time = str(datetime.now())
    conn = mysql.connector.connect(host="localhost", username="root", password=PWS ,database="anpr_final_db")
    my_cursor = conn.cursor()
    sql = "INSERT INTO `anpr_final_db`.`rto` (`Vehicle_number`, `Entry_time`) VALUES (%s,%s);"
    data = (number_p,str(datetime.now()))
    try:
        my_cursor.execute(sql,data)
        conn.commit()
        update_capicity(True)
        messagebox.showinfo("Informetion", "Data updated ")
    except:
        messagebox.showerror("Error","Data is not update server probalme ")
    finally:
        conn.close()



def update_Exit_get(number_p):
    PWS = 'rakesh'

    conn = mysql.connector.connect(host="localhost", username="root", password=PWS, database="anpr_final_db")
    my_cursor = conn.cursor()
    sql = "SELECT * FROM anpr_final_db.rto where Vehicle_number = %s or Exit_time = %s;"
    data = (number_p,None)
    try:
        my_cursor.execute(sql,data)
        result = (my_cursor.fetchall())
        conn.commit()
    except:
        messagebox.showerror("Error", "Data is not update server probalme 1 ")
    finally:
        conn.close()

    index = None
    for i in range(len(result)):
        if result[i][-1] == None:
            index = result[i][0]

    update_bile(list(result[i]))
    conn = mysql.connector.connect(host="localhost", username="root", password="rakesh", database="anpr_final_db")
    my_cursor = conn.cursor()
    q1 = "UPDATE`anpr_final_db`.`rto`SET`Exit_time` =  %s WHERE(`index` = %s);"
    d = (str(datetime.now()),index)
    try:
        my_cursor.execute(q1,d)
        conn.commit()
        update_capicity(False)
        messagebox.showinfo("Informetion", "Data updated ")
    except:
        messagebox.showerror("Error", "Data is not update server probalme ")
    finally:
        conn.close()


def update_bile(rto_data):
    bile_id = get_bile_id()
    result = get_owner_data(rto_data[1])[0]
    if len(result) > 0:
        sql = f"INSERT INTO`anpr_final_db`.`billes`(`bill_id`, `owner_name`, `veh_num`, `Entry_date`, `Exit_date`, `addres`, `mobile_num`)"\
        f"VALUES('{bile_id}','{result[1]}','{rto_data[1]}', '{rto_data[2]}', '{str(datetime.now())}','{result[-1]}', '{result[2]}');"

    conn = mysql.connector.connect(host="localhost", username="root", password="rakesh", database="anpr_final_db")
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    conn.commit()
    conn.close()


def get_bile_id():
    conn = mysql.connector.connect(host="localhost", username="root", password="rakesh", database="anpr_final_db")
    my_cursor = conn.cursor()
    sql = "SELECT * FROM anpr_final_db.billes;"
    my_cursor.execute(sql)
    data = my_cursor.fetchall()
    bill_id = int(data[-1][0])
    return bill_id+1


def get_owner_data(index):
    conn = mysql.connector.connect(host="localhost", username="root", password="rakesh", database="anpr_final_db")
    my_cursor = conn.cursor()
    sql = f"SELECT * FROM anpr_final_db.owner_data where Vehicle_number = '{index}';"
    my_cursor.execute(sql)
    data = my_cursor.fetchall()
    conn.close()
    return data



Time = str(datetime.now())

