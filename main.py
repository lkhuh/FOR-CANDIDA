from tkinter import *
import mysql.connector
root = Tk()

mydb = mysql.connector.connect(
       host = "localhost",
       user = "root",
       passwd = "Sparsh123",
     )
print(mydb)
root.mainloop()