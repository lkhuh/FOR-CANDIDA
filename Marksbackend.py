import sqlite3

def Marksdata():
    con = sqlite3.connect('marks_data.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS marks(id INTEGER PRIMARY KEY,StdID text,Firstname text,Lastname text,CourseCode text,ExamName text,grade text,TotalPercent text,TotalMarks  text,Parents text,English text,Science text,Hindi text,Social text,Moral text,Gk text,\
                Sanskrit text,Art text,Maths text)")
    con.commit()
    con.close()


def AddStdrec(StdID,Firstname,Lastname,CourseCode,ExamName,grade,TotalPercent,TotalMarks,Parents,English,Science ,Maths,Hindi,Social,Gk,Art,Moral,\
                Sanskrit):
    con = sqlite3.connect('marks_data.db')
    cur = con.cursor()
    cur.execute("INSERT INTO marks VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",\
                (StdID,Firstname,Lastname,CourseCode,ExamName,grade,TotalPercent,TotalMarks,Parents,English,Science ,Maths,Hindi,Social,Gk,Art,Moral,\
                Sanskrit))
    con.commit()
    con.close()

def viewdata():
    con = sqlite3.connect('marks_data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM marks")
    row = cur.fetchall()
    con.commit()
    con.close()
    return row
def delete_Rec(id):
    con = sqlite3.connect('marks_data.db')
    cur = con.cursor()
    cur.execute("DELETE FROM marks WHERE id=?",(id,))
    row = cur.fetchall()
    con.commit()
    con.close()
def search_data(StdID="",Firstname="",Lastname="",CourseCode="",ExamName="",grade="",TotalPercent="",TotalMarks="",Parents="",Science="" ,English="",Hindi="",Social="",Moral="",Gk="",\
                Sanskrit="",Art="",Maths=""):
    con = sqlite3.connect('marks_data.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM marks WHERE StdID=? OR Firstname=? OR Lastname=? OR CourseCode=? OR ExamName=? OR grade=? OR TotalPercent=? OR TotalMarks=? OR Parents=? OR Science=? OR English=? OR Hindi=? OR Social=? OR Moral=? OR Gk=? OR\
                Sanskrit=? OR Art=? OR Maths=?",
                (StdID,Firstname,Lastname,CourseCode,ExamName,grade,TotalPercent,TotalMarks,Parents,Science ,English,Hindi,Social,Moral,Gk ,\
                Sanskrit,Art,Maths))
    row = cur.fetchall()
    con.commit()
    con.close()
    return row
def data_update(id,StdID="",Firstname="",Lastname="",CourseCode="",ExamName="",grade="",TotalPercent="",TotalMarks="",Parents="",Science="" ,English="",Hindi="",Social="",Moral="",Gk="",\
                Sanskrit="",Art="",Maths=""):
    con = sqlite3.connect('marks_data.db')
    cur = con.cursor()
    cur.execute("UPDATE marks SET StdID=?,Firstname=?,Lastname=?,CourseCode=?,ExamName=?,grade=?,TotalPercent=?,TotalMarks=?,Parents=?,Science=?,English=?,Hindi=?,Social=?,Moral=?,Gk=?, \
                Sanskrit=?,Art=?,Maths=? WHERE id=?", \
                (StdID,Firstname,Lastname,CourseCode,ExamName,grade,TotalPercent,TotalMarks,Parents,Science ,English,Hindi,Social,Moral,Gk ,\
                Sanskrit,Art,Maths,id))
    con.commit()
    con.close()


Marksdata()
