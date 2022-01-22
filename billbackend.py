import sqlite3

def Billdata():
    con = sqlite3.connect('cps_bill.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bill(id INTEGER PRIMARY KEY,BillID text,Firstname text,Lastname text,Dob text,\
    Age text,Gender text,Address text,Mobile text)")
    con.commit()
    con.close()


def AddBillrec(BillID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile):
    con = sqlite3.connect('cps_bill.db')
    cur = con.cursor()
    cur.execute("INSERT INTO bill VALUES (NULL, ?,?,?,?,?,?,?,?)", \
                (BillID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile))
    con.commit()
    con.close()

def viewdata():
    con = sqlite3.connect('cps_bill.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM bill")
    row = cur.fetchall()
    con.commit()
    con.close()
    return row
def delete_Rec(id):
    con = sqlite3.connect('cps_bill.db')
    cur = con.cursor()
    cur.execute("DELETE FROM bill WHERE id=?",(id,))
    row = cur.fetchall()
    con.commit()
    con.close()
def search_data(BillID="",Firstname="",Lastname="",Dob="",Age="",Gender="",Address="",Mobile=""):
    con = sqlite3.connect('cps_bill.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM bill WHERE StdID=? OR Firstname=? OR Lastname=? OR Dob=? OR Age=? OR Gender=? OR Address=? OR \
    Mobile=?",(BillID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile))
    row = cur.fetchall()
    con.commit()
    con.close()
    return row
def data_update(id,BillID="",Firstname="",Lastname="",Dob="",Age="",Gender="",Address="",Mobile=""):
    con = sqlite3.connect('cps_bill.db')
    cur = con.cursor()
    cur.execute("UPDATE bill SET StdID=?,Firstname=?,Lastname=?,Dob=?,Age=?,Gender=?,Address=?,Mobile=? WHERE id=?", \
                (BillID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile,id))
    con.commit()
    con.close()


Billdata()