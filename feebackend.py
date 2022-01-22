import sqlite3

def Studentdata():
    con = sqlite3.connect('fee_data.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS fee(id INTEGER PRIMARY KEY,StdID text,Firstname text,Lastname text,Dob text,\
    Age text,Gender text,Address text,Mobile text)")
    con.commit()
    con.close()


def AddStdrec(StdID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile):
    con = sqlite3.connect('fee_data.db')
    cur = con.cursor()
    cur.execute("INSERT INTO fee VALUES (NULL, ?,?,?,?,?,?,?,?)", \
                (StdID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile))
    con.commit()
    con.close()

def viewdata():
    con = sqlite3.connect('fee_data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM fee")
    row = cur.fetchall()
    con.commit()
    con.close()
    return row
def delete_Rec(id):
    con = sqlite3.connect('fee_data.db')
    cur = con.cursor()
    cur.execute("DELETE FROM fee WHERE id=?",(id,))
    row = cur.fetchall()
    con.commit()
    con.close()
def search_data(StdID="",Firstname="",Lastname="",Dob="",Age="",Gender="",Address="",Mobile=""):
    con = sqlite3.connect('fee_data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM fee WHERE StdID=? OR Firstname=? OR Lastname=? OR Dob=? OR Age=? OR Gender=? OR Address=? OR \
    Mobile=?",(StdID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile))
    row = cur.fetchall()
    con.commit()
    con.close()
    return row
def data_update(id,StdID="",Firstname="",Lastname="",Dob="",Age="",Gender="",Address="",Mobile=""):
    con = sqlite3.connect('fee_data.db')
    cur = con.cursor()
    cur.execute("UPDATE fee SET StdID=?,Firstname=?,Lastname=?,Dob=?,Age=?,Gender=?,Address=?,Mobile=? WHERE id=?", \
                (StdID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile,id))
    con.commit()
    con.close()


Studentdata()