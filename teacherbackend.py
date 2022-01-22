import sqlite3

def Teacherdata():
    con = sqlite3.connect('cps_teacher.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS teacher(id INTEGER PRIMARY KEY,TeacherID text,Firstname text,Lastname text,Dob text,\
    Age text,Gender text,Address text,Mobile text)")
    con.commit()
    con.close()


def Addrec(TeacherID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile):
    con = sqlite3.connect('cps_teacher.db')
    cur = con.cursor()
    cur.execute("INSERT INTO teacher VALUES (NULL, ?,?,?,?,?,?,?,?)", \
                (TeacherID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile))
    con.commit()
    con.close()

def viewdata():
    con = sqlite3.connect('cps_teacher.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM teacher")
    row = cur.fetchall()
    con.commit()
    con.close()
    return row
def delete_Rec(id):
    con = sqlite3.connect('cps_teacher.db')
    cur = con.cursor()
    cur.execute("DELETE FROM teacher WHERE id=?",(id,))
    row = cur.fetchall()
    con.commit()
    con.close()
def search_data(TeacherID="",Firstname="",Lastname="",Dob="",Age="",Gender="",Address="",Mobile=""):
    con = sqlite3.connect('cps_teacher.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM teacher WHERE TeacherID=? OR Firstname=? OR Lastname=? OR Dob=? OR Age=? OR Gender=? OR Address=? OR \
    Mobile=?",(TeacherID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile))
    row = cur.fetchall()
    con.commit()
    con.close()
    return row
def data_update(id,TeacherID="",Firstname="",Lastname="",Dob="",Age="",Gender="",Address="",Mobile=""):
    con = sqlite3.connect('cps_teacher.db')
    cur = con.cursor()
    cur.execute("UPDATE teacher SET TeacherID=?,Firstname=?,Lastname=?,Dob=?,Age=?,Gender=?,Address=?,Mobile=? WHERE id=?", \
                (TeacherID,Firstname,Lastname,Dob,Age,Gender,Address,Mobile,id))
    con.commit()
    con.close()


Teacherdata()