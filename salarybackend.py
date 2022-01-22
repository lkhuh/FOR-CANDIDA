import sqlite3

def Studentdata():
    con = sqlite3.connect('cps_data.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,StdID text,Firstname text,Lastname text,Dob text,\
    Age text,Gender text,Address text,Mobile text,Caste text)")
    con.commit()
    con.close()


def AddStdrec(StdID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile,Caste):
    con = sqlite3.connect('cps_data.db')
    cur = con.cursor()
    cur.execute("INSERT INTO students VALUES (NULL, ?,?,?,?,?,?,?,?,?)", \
                (StdID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile,Caste))
    con.commit()
    con.close()

def viewdata():
    con = sqlite3.connect('cps_data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    row = cur.fetchall()
    con.commit()
    con.close()
    return row
def delete_Rec(id):
    con = sqlite3.connect('cps_data.db')
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE id=?",(id,))
    row = cur.fetchall()
    con.commit()
    con.close()
def search_data(StdID="",Firstname="",Lastname="",Dob="",Age="",Gender="",Address="",Mobile="",Caste=""):
    con = sqlite3.connect('cps_data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM students WHERE StdID=? OR Firstname=? OR Lastname=? OR Dob=? OR Age=? OR Gender=? OR Address=? OR \
    Mobile=? OR Caste=?",(StdID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile,Caste))
    row = cur.fetchall()
    con.commit()
    con.close()
    return row
def data_update(id,StdID="",Firstname="",Lastname="",Dob="",Age="",Gender="",Address="",Mobile="",Caste=""):
    con = sqlite3.connect('cps_data.db')
    cur = con.cursor()
    cur.execute("UPDATE students SET StdID=?,Firstname=?,Lastname=?,Dob=?,Age=?,Gender=?,Address=?,Mobile=?,Caste=? WHERE id=?", \
                (StdID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile,Caste,id))
    con.commit()
    con.close()