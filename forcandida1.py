from tkinter import *
from tkinter import ttk
from tkinter import messagebox as tmsg
import backend
import teacherbackend
import billbackend
import Marksbackend
import feebackend
import salarybackend
def MoM():
    global root1
    class Teacher:
        def __init__(self,root):
            self.root = root1
            blank_space= ""
            self.root.title("CANDIDA PUBLIC SCHOOL")
            self.root.geometry('1300x800+0+0')
            TeacherID = StringVar()
            Firstname = StringVar()
            Lastname = StringVar()
            Dob = StringVar()
            Age  = StringVar()
            Gender = StringVar()
            Address = StringVar()
            Mobile = StringVar()


            def calc():



                LARGE_FONT_STYLE = ("Arial", 40, "bold")
                SMALL_FONT_STYLE = ("Arial", 16)
                DIGITS_FONT_STYLE = ("Arial", 24, "bold")
                DEFAULT_FONT_STYLE = ("Arial", 20)

                OFF_WHITE = "#F8FAFF"
                WHITE = "#FFFFFF"
                LIGHT_BLUE = "#CCEDFF"
                LIGHT_GRAY = "#F5F5F5"
                LABEL_COLOR = "#25265E"

                class Calculator:
                    def __init__(self):
                        self.window = Tk()
                        self.window.geometry("375x600")
                        self.window.resizable(0, 0)
                        self.window.title("Calculator")

                        self.total_expression = ""
                        self.current_expression = ""
                        self.display_frame = self.create_display_frame()

                        self.total_label, self.label = self.create_display_labels()

                        self.digits = {
                            7: (1, 1), 8: (1, 2), 9: (1, 3),
                            4: (2, 1), 5: (2, 2), 6: (2, 3),
                            1: (3, 1), 2: (3, 2), 3: (3, 3),
                            0: (4, 2), '.': (4, 1)
                        }
                        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
                        self.buttons_frame = self.create_buttons_frame()

                        self.buttons_frame.rowconfigure(0, weight=1)
                        for x in range(1, 5):
                            self.buttons_frame.rowconfigure(x, weight=1)
                            self.buttons_frame.columnconfigure(x, weight=1)
                        self.create_digit_buttons()
                        self.create_operator_buttons()
                        self.create_special_buttons()
                        self.bind_keys()

                    def bind_keys(self):
                        self.window.bind("<Return>", lambda event: self.evaluate())
                        for key in self.digits:
                            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

                        for key in self.operations:
                            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

                    def create_special_buttons(self):
                        self.create_clear_button()
                        self.create_equals_button()
                        self.create_square_button()
                        self.create_sqrt_button()

                    def create_display_labels(self):
                        total_label = Label(self.display_frame, text=self.total_expression, anchor=E,
                                               bg=LIGHT_GRAY,
                                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
                        total_label.pack(expand=True, fill='both')

                        label = Label(self.display_frame, text=self.current_expression, anchor=E, bg=LIGHT_GRAY,
                                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
                        label.pack(expand=True, fill='both')

                        return total_label, label

                    def create_display_frame(self):
                        frame = Frame(self.window, height=221, bg=LIGHT_GRAY)
                        frame.pack(expand=True, fill="both")
                        return frame

                    def add_to_expression(self, value):
                        self.current_expression += str(value)
                        self.update_label()

                    def create_digit_buttons(self):
                        for digit, grid_value in self.digits.items():
                            button = Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR,
                                               font=DIGITS_FONT_STYLE,
                                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
                            button.grid(row=grid_value[0], column=grid_value[1], sticky=NSEW)

                    def append_operator(self, operator):
                        self.current_expression += operator
                        self.total_expression += self.current_expression
                        self.current_expression = ""
                        self.update_total_label()
                        self.update_label()

                    def create_operator_buttons(self):
                        i = 0
                        for operator, symbol in self.operations.items():
                            button = Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR,
                                               font=DEFAULT_FONT_STYLE,
                                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
                            button.grid(row=i, column=4, sticky=NSEW)
                            i += 1

                    def clear(self):
                        self.current_expression = ""
                        self.total_expression = ""
                        self.update_label()
                        self.update_total_label()

                    def create_clear_button(self):
                        button = Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR,
                                           font=DEFAULT_FONT_STYLE,
                                           borderwidth=0, command=self.clear)
                        button.grid(row=0, column=1, sticky=NSEW)

                    def square(self):
                        self.current_expression = str(eval(f"{self.current_expression}**2"))
                        self.update_label()

                    def create_square_button(self):
                        button = Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR,
                                           font=DEFAULT_FONT_STYLE,
                                           borderwidth=0, command=self.square)
                        button.grid(row=0, column=2, sticky=NSEW)

                    def sqrt(self):
                        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
                        self.update_label()

                    def create_sqrt_button(self):
                        button = Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR,
                                           font=DEFAULT_FONT_STYLE,
                                           borderwidth=0, command=self.sqrt)
                        button.grid(row=0, column=3, sticky=NSEW)

                    def evaluate(self):
                        self.total_expression += self.current_expression
                        self.update_total_label()
                        try:
                            self.current_expression = str(eval(self.total_expression))

                            self.total_expression = ""
                        except Exception as e:
                            self.current_expression = "Error"
                        finally:
                            self.update_label()

                    def create_equals_button(self):
                        button = Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR,
                                           font=DEFAULT_FONT_STYLE,
                                           borderwidth=0, command=self.evaluate)
                        button.grid(row=4, column=3, columnspan=2, sticky=NSEW)

                    def create_buttons_frame(self):
                        frame = Frame(self.window)
                        frame.pack(expand=True, fill="both")
                        return frame

                    def update_total_label(self):
                        expression = self.total_expression
                        for operator, symbol in self.operations.items():
                            expression = expression.replace(operator, f' {symbol} ')
                        self.total_label.config(text=expression)

                    def update_label(self):
                        self.label.config(text=self.current_expression[:11])

                    def run(self):
                        self.window.mainloop()

                if __name__ == "__main__":
                    calc = Calculator()
                    calc.run()



            def iExit():
                iExit = tmsg.askyesno("CANDIDA PUBLIC SCHOOL","Do you really want to quit")
                if iExit > 0:
                    root.destroy()
                    return
            def Clear():
                self.txtTeacherID.delete(0,END)
                self.txtFirstname.delete(0,END)
                self.txtLastname.delete(0,END)
                self.txtDob.delete(0,END)
                self.txtAge.delete(0,END)
                self.cbogender.delete(0,END)
                self.txtAddress.delete(0,END)
                self.txtMobile.delete(0,END)
            def Display():
                teacherlist.delete(0,END)
                for row in teacherbackend.viewdata():
                    teacherlist.insert(END,row,str(""))
            def AddNew():
                if (len(TeacherID.get()) != 0):
                    teacherbackend.Addrec(TeacherID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),Gender.get(), \
                                      Address.get(),Mobile.get())
                    teacherlist.delete(0,END)
                    teacherlist.insert(END,TeacherID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),Gender.get() \
                                            ,Address.get(),Mobile.get())
            def Search():
                teacherlist.delete(0, END)
                for row in teacherbackend.search_data(TeacherID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),Gender.get(), \
                        Address.get(),Mobile.get()):
                    teacherlist.insert(END, row, str(""))
            def Delete():
                if (len(TeacherID.get()) != 0):
                    teacherbackend.delete_Rec(sd[0])
                    Clear()
                    Display()
            def Student_Rec(event):
                global sd
                searchStd = teacherlist.curselection()[0]
                sd =teacherlist.get(searchStd)
                self.txtTeacherID.delete(0,END)
                self.txtTeacherID.insert(END,sd[1])
                self.txtFirstname.delete(0,END)
                self.txtFirstname.insert(END,sd[2])
                self.txtLastname.delete(0,END)
                self.txtLastname.insert(END,sd[3])
                self.txtDob.delete(0,END)
                self.txtDob.insert(END,sd[4])
                self.txtAge.delete(0,END)
                self.txtAge.insert(END,sd[5])
                self.cbogender.delete(0,END)
                self.cbogender.insert(END,sd[6])
                self.txtAddress.delete(0,END)
                self.txtAddress.insert(END,sd[7])
                self.txtMobile.delete(0,END)
                self.txtMobile.insert(END,sd[8])
            def update():
                if (len(TeacherID.get()) != 0):
                    teacherbackend.delete_Rec(sd[0])
                if (len(TeacherID.get()) != 0):
                    teacherbackend.Addrec(TeacherID.get(), Firstname.get(), Lastname.get(), Dob.get(), Age.get(), Gender.get(), \
                                      Address.get(), Mobile.get())
                    teacherlist.delete(0, END)
                    teacherlist.insert(END, TeacherID.get(), Firstname.get(), Lastname.get(), Dob.get(), Age.get(), Gender.get() \
                                       , Address.get(), Mobile.get())

            MAINFRAME = Frame(self.root,bd=10,width=1350,height=700,relief=RIDGE,bg="cadet blue")
            MAINFRAME.grid()




            TOPFRAME = Frame(MAINFRAME, bd=5, width=400, height=50, relief=RIDGE)
            TOPFRAME.pack(side=BOTTOM)
            TITLEFRAME = Frame(MAINFRAME, bd=5, width=1340, height=100, relief=RIDGE)
            TITLEFRAME.pack(side=TOP,anchor='w')
            TOPFRAME1 = Frame(MAINFRAME, bd=5, width=1340, height=500, relief=RIDGE)
            TOPFRAME1.pack(side=TOP,anchor='w')
            #


            LEFTFRAME = Frame(TOPFRAME1,bd=5,width=1340,relief=RIDGE,padx=2,bg="cadet blue",height=400)
            LEFTFRAME.pack(side=LEFT)
            LEFTFRAME1 = Frame(LEFTFRAME, bd=5, width=600, relief=RIDGE, padx=2,pady=4, height=180)
            LEFTFRAME1.pack(side=TOP,padx=0,pady=4)

            RIGHTFRAME = Frame(TOPFRAME1,bd=5,width=320,relief=RIDGE,padx=2,pady=4,bg="cadet blue",height=400)
            RIGHTFRAME.pack(side=RIGHT)
            RIGHTFRAME1 = Frame(RIGHTFRAME, bd=5, width=310, relief=RIDGE, padx=2, pady=2, height=200)
            RIGHTFRAME1.pack(side=TOP)


            self.labeltitle = Label(TITLEFRAME,font='arial 56 bold',bd=7,text="CANDIDA PUBLIC SCHOOL")
            self.labeltitle.grid(row=0,column=0,padx=132)

            self.labelTeacherID = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Teacher ID",anchor='w',justify=LEFT)
            self.labelTeacherID.grid(row=0, column=0, padx=5)
            self.txtTeacherID = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left',textvariable=TeacherID)
            self.txtTeacherID.grid(row=0, column=1)

            self.labelFirstname = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Firstname", anchor='w', justify=LEFT)
            self.labelFirstname.grid(row=1, column=0, padx=5)
            self.txtFirstname = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Firstname)
            self.txtFirstname.grid(row=1, column=1)

            self.labelLastname = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Lastname", anchor='w', justify=LEFT)
            self.labelLastname.grid(row=2, column=0, padx=5)
            self.txtLastname = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left',textvariable=Lastname)
            self.txtLastname.grid(row=2, column=1)

            self.labelDob = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Date of Birth", anchor='w', justify=LEFT)
            self.labelDob.grid(row=3, column=0, padx=5)
            self.txtDob = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left',textvariable=Dob)
            self.txtDob.grid(row=3, column=1)

            self.labelAge = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Age", anchor='w', justify=LEFT)
            self.labelAge.grid(row=4, column=0, padx=5)
            self.txtAge = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Age)
            self.txtAge.grid(row=4, column=1)

            self.genderlbl = Label(LEFTFRAME1,text="Gender",font='arial 12 bold').grid(row=5,column=0)
            self.cbogender = ttk.Combobox(LEFTFRAME1, font='arial 12 bold', width=39,state='readonly',justify='left',textvariable=Gender)
            self.cbogender['values'] = ['','Male','Female']
            self.cbogender.current(0)
            self.cbogender.grid(row=5,column=1)






            self.labelAddress = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Address", anchor='w', justify=LEFT)
            self.labelAddress.grid(row=6, column=0, padx=5)
            self.txtAddress = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Address)
            self.txtAddress.grid(row=6, column=1)

            self.labelMobile = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Mobile", anchor='w', justify=LEFT)
            self.labelMobile.grid(row=7, column=0, padx=5)
            self.txtMobile = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Mobile)
            self.txtMobile.grid(row=7, column=1)


            scroll_bar = Scrollbar(RIGHTFRAME1)
            scroll_bar.grid(row=0,column=1,sticky="ns")


            teacherlist = Listbox(RIGHTFRAME1,width=41,height=16,font="arial 12 bold",yscrollcommand=scroll_bar.set)
            teacherlist.bind('<<ListboxSelect>>',Student_Rec)
            teacherlist.grid(row=0,column=0,padx=8)
            scroll_bar.config(command=teacherlist.yview)


            self.BtnAddnew = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Add New", width=11,
                                    padx=1,
                                    height=2, command=AddNew).grid(row=0, column=0, padx=1)
            self.BtnDisplay = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Display", width=11,
                                     padx=1,
                                     height=2, command=Display).grid(row=0, column=1, padx=1)
            self.BtnDelete = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Delete", width=11, padx=1,
                                    height=2, command=Delete).grid(row=0, column=2, padx=1)
            self.BtnClear = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Clear", width=11, padx=1,
                                   height=2, command=Clear).grid(row=0, column=3, padx=1)
            self.BtnExit = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Exit", width=11, padx=1,
                                  height=2, command=iExit).grid(row=0, column=4, padx=1)
            self.BtnSearch = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Search", width=11, padx=1,
                                    height=2, command=Search).grid(row=0, column=5, padx=1)
            self.BtnUpdate = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Update", width=11, padx=1,
                                    height=2, command=update).grid(row=0, column=6, padx=1)
            self.BtnCalculator = Button(LEFTFRAME1
            , pady=1, bd=4, font=('arial', 13, 'bold'), text="Calculator", width=12, padx=1,
                                    height=2, command=calc,bg="light green").grid(row=0, column=6, padx=1)
            self.BtnCalculator = Button(LEFTFRAME1, pady=1, bd=4, font=('arial', 13, 'bold'), text="student marks",
                                        width=12, padx=1,
                                        height=2, command=Students_marks, bg="light green").grid(row=1, column=6, padx=1)
            self.BtnCalculator = Button(LEFTFRAME1, pady=1, bd=4, font=('arial', 13, 'bold'), text="student fee",
                                        width=12, padx=1,
                                        height=2, command=Students_fee, bg="light green").grid(row=2, column=6,
                                                                                                 padx=1)
            self.BtnCalculator = Button(LEFTFRAME1, pady=1, bd=4, font=('arial', 13, 'bold'), text="teacher's salary",
                                        width=12, padx=1,
                                        height=2, command=Teacher_salary, bg="light green").grid(row=3, column=6,
                                                                                                 padx=1)
            self.BtnCalculator = Button(LEFTFRAME1, pady=1, bd=4, font=('arial', 13, 'bold'), text="Student's data",
                                        width=12, padx=1,
                                        height=2, command=main, bg="light green").grid(row=4, column=6,
                                                                                                 padx=1)


    if __name__ == '__main__':
        root1 = Tk()
        application = Teacher(root1)
        root1.mainloop()
def school_info():
    root1.destroy()
    class Student:
        def __init__(self,root):
            self.root = root
            blank_space= ""
            self.root.title("CANDIDA PUBLIC SCHOOL")
            self.root.geometry('1300x800+0+0')
            BillID = StringVar()
            Firstname = StringVar()
            Lastname = StringVar()
            Dob = StringVar()
            Age  = StringVar()
            Gender = StringVar()
            Address = StringVar()
            Mobile = StringVar()


            def iExit():
                iExit = tmsg.askyesno("CANDIDA PUBLIC SCHOOL","Do you really want to quit")
                if iExit > 0:
                    root.destroy()
                    return
            def Clear():
                self.txtStdID.delete(0,END)
                self.txtFirstname.delete(0,END)
                self.txtLastname.delete(0,END)
                self.txtDob.delete(0,END)
                self.txtAge.delete(0,END)
                self.cbogender.delete(0,END)
                self.txtAddress.delete(0,END)
                self.txtMobile.delete(0,END)
            def Display():
                studentlist.delete(0,END)
                for row in billbackend.viewdata():
                    studentlist.insert(END,row,str(""))
            def AddNew():
                if (len(BillID.get()) != 0):
                    billbackend.AddBillrec(BillID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),Gender.get(), \
                                      Address.get(),Mobile.get())
                    studentlist.delete(0,END)
                    studentlist.insert(END,BillID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),Gender.get() \
                                            ,Address.get(),Mobile.get())
            def Search():
                studentlist.delete(0, END)
                for row in billbackend.search_data(BillID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),Gender.get(), \
                        Address.get(),Mobile.get()):
                    studentlist.insert(END, row, str(""))
            def Delete():
                if (len(BillID.get()) != 0):
                    billbackend.delete_Rec(sd[0])
                    Clear()
                    Display()
            def Student_Rec(event):
                global sd
                searchStd = studentlist.curselection()[0]
                sd = studentlist.get(searchStd)
                self.txtStdID.delete(0,END)
                self.txtStdID.insert(END,sd[1])
                self.txtFirstname.delete(0,END)
                self.txtFirstname.insert(END,sd[2])
                self.txtLastname.delete(0,END)
                self.txtLastname.insert(END,sd[3])
                self.txtDob.delete(0,END)
                self.txtDob.insert(END,sd[4])
                self.txtAge.delete(0,END)
                self.txtAge.insert(END,sd[5])
                self.cbogender.delete(0,END)
                self.cbogender.insert(END,sd[6])
                self.txtAddress.delete(0,END)
                self.txtAddress.insert(END,sd[7])
                self.txtMobile.delete(0,END)
                self.txtMobile.insert(END,sd[8])
            def update():
                if (len(BillID.get()) != 0):
                    billbackend.delete_Rec(sd[0])
                if (len(BillID.get()) != 0):
                    billbackend.AddStdrec(BillID.get(), Firstname.get(), Lastname.get(), Dob.get(), Age.get(), Gender.get(), \
                                      Address.get(), Mobile.get())
                    studentlist.delete(0, END)
                    studentlist.insert(END,BillID.get(), Firstname.get(), Lastname.get(), Dob.get(), Age.get(), Gender.get() \
                                       , Address.get(), Mobile.get())
            MAINFRAME = Frame(self.root,bd=10,width=1350,height=700,relief=RIDGE,bg="cadet blue")
            MAINFRAME.grid()




            TOPFRAME = Frame(MAINFRAME, bd=5, width=400, height=50, relief=RIDGE)
            TOPFRAME.pack(side=BOTTOM)
            TITLEFRAME = Frame(MAINFRAME, bd=5, width=1340, height=100, relief=RIDGE)
            TITLEFRAME.pack(side=TOP,anchor='w')
            TOPFRAME1 = Frame(MAINFRAME, bd=5, width=1340, height=500, relief=RIDGE)
            TOPFRAME1.pack(side=TOP,anchor='w')
            #
            # BUTTONFRAME = Frame(TOPFRAME, bd=5, width=1340, height=50, relief=RIDGE, bg="light green")
            # BUTTONFRAME.pack(anchor='e',side=RIGHT)

            LEFTFRAME = Frame(TOPFRAME1,bd=5,width=1340,relief=RIDGE,padx=2,bg="cadet blue",height=400)
            LEFTFRAME.pack(side=LEFT)
            LEFTFRAME1 = Frame(LEFTFRAME, bd=5, width=600, relief=RIDGE, padx=2,pady=4, height=180)
            LEFTFRAME1.pack(side=TOP,padx=0,pady=4)

            RIGHTFRAME = Frame(TOPFRAME1,bd=5,width=320,relief=RIDGE,padx=2,pady=4,bg="cadet blue",height=400)
            RIGHTFRAME.pack(side=RIGHT)
            RIGHTFRAME1 = Frame(RIGHTFRAME, bd=5, width=310, relief=RIDGE, padx=2, pady=2, height=200)
            RIGHTFRAME1.pack(side=TOP)

            # BUTTONFRAME1 = Frame(BUTTONFRAME,bd=5,width=200,relief=RIDGE,padx=2,pady=2,height=200)
            # BUTTONFRAME1.pack(side=RIGHT)
            self.labeltitle = Label(TITLEFRAME,font='arial 56 bold',bd=7,text="CANDIDA PUBLIC SCHOOL")
            self.labeltitle.grid(row=0,column=0,padx=132)

            self.labelStdID = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Bill ID",anchor='w',justify=LEFT)
            self.labelStdID.grid(row=0, column=0, padx=5)
            self.txtStdID = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left',textvariable=BillID)
            self.txtStdID.grid(row=0, column=1)

            self.labelFirstname = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="WHY THIS BILL", anchor='w', justify=LEFT)
            self.labelFirstname.grid(row=1, column=0, padx=5)
            self.txtFirstname = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Firstname)
            self.txtFirstname.grid(row=1, column=1)

            self.labelLastname = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Bill costs", anchor='w', justify=LEFT)
            self.labelLastname.grid(row=2, column=0, padx=5)
            self.txtLastname = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left',textvariable=Lastname)
            self.txtLastname.grid(row=2, column=1)

            self.labelDob = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Date of Bill", anchor='w', justify=LEFT)
            self.labelDob.grid(row=3, column=0, padx=5)
            self.txtDob = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left',textvariable=Dob)
            self.txtDob.grid(row=3, column=1)

            self.labelAge = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="TAX ON THIS BILL", anchor='w', justify=LEFT)
            self.labelAge.grid(row=4, column=0, padx=5)
            self.txtAge = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Age)
            self.txtAge.grid(row=4, column=1)

            self.genderlbl = Label(LEFTFRAME1,text="IS THIS IMPORTANT",font='arial 12 bold').grid(row=5,column=0)
            self.cbogender = ttk.Combobox(LEFTFRAME1, font='arial 12 bold', width=39,state='readonly',justify='left',textvariable=Gender)
            self.cbogender['values'] = ['','IMPORTANT','PERSONAL']
            self.cbogender.current(0)
            self.cbogender.grid(row=5,column=1)






            self.labelAddress = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="G.S.T", anchor='w', justify=LEFT)
            self.labelAddress.grid(row=6, column=0, padx=5)
            self.txtAddress = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Address)
            self.txtAddress.grid(row=6, column=1)

            self.labelMobile = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="FROM WHICH SHOP", anchor='w', justify=LEFT)
            self.labelMobile.grid(row=7, column=0, padx=5)
            self.txtMobile = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Mobile)
            self.txtMobile.grid(row=7, column=1)


            scroll_bar = Scrollbar(RIGHTFRAME1)
            scroll_bar.grid(row=0,column=1,sticky="ns")


            studentlist = Listbox(RIGHTFRAME1,width=41,height=16,font="arial 12 bold",yscrollcommand=scroll_bar.set)
            studentlist.bind('<<ListboxSelect>>',Student_Rec)
            studentlist.grid(row=0,column=0,padx=8)
            scroll_bar.config(command=studentlist.yview)





            self.BtnAddnew = Button(TOPFRAME,pady=1,bd=4,font=('arial', 15,'bold'),text="Add New",width=11,padx=1,
                                    height=2,command=AddNew).grid(row=0,column=0,padx=1)
            self.BtnDisplay = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Display", width=11,padx=1,
                                    height=2,command=Display).grid(row=0, column=1, padx=1)
            self.BtnDelete = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Delete", width=11,padx=1,
                                    height=2,command=Delete).grid(row=0, column=2, padx=1)
            self.BtnClear = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Clear", width=11,padx=1,
                                    height=2,command=Clear).grid(row=0, column=3, padx=1)
            self.BtnExit = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Exit", width=11,padx=1,
                                    height=2,command=iExit).grid(row=0, column=4, padx=1)
            self.BtnSearch = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Search", width=11,padx=1,
                                    height=2,command=Search).grid(row=0, column=5, padx=1)
            self.BtnUpdate = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Update", width=11, padx=1,
                                    height=2, command=update).grid(row=0, column=6, padx=1)
            self.Btncalculator = Button(RIGHTFRAME1, pady=1, padx=1, font="arial 10 bold", width=12, bg="light green",
                                        height=2, command=MoM, text="main", ).grid(row=0, column=19)
    if __name__ == '__main__':
        root = Tk()
        application = Student(root)
        root.mainloop()
def main():
    global root
    class Student:
        def __init__(self,root):
            self.root = root
            blank_space= ""
            self.root.title("CANDIDA PUBLIC SCHOOL")
            self.root.geometry('1300x800+0+0')
            StdID = StringVar()
            Firstname = StringVar()
            Lastname = StringVar()
            Dob = StringVar()
            Age  = StringVar()
            Gender = StringVar()
            Address = StringVar()
            Mobile = StringVar()
            Caste = StringVar()

            def iExit():
                iExit = tmsg.askyesno("CANDIDA PUBLIC SCHOOL","Do you really want to quit")
                if iExit > 0:
                    root.destroy()
                    return
            def Clear():
                self.txtStdID.delete(0,END)
                self.txtFirstname.delete(0,END)
                self.txtLastname.delete(0,END)
                self.txtDob.delete(0,END)
                self.txtAge.delete(0,END)
                self.cbogender.delete(0,END)
                self.txtAddress.delete(0,END)
                self.txtMobile.delete(0,END)
                self.txtcaste.delete(0,END)
            def Display():
                studentlist.delete(0,END)
                for row in backend.viewdata():
                    studentlist.insert(END,row,str(""))
            def AddNew():
                if (len(StdID.get()) != 0):
                    backend.AddStdrec(StdID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),Gender.get(), \
                                      Address.get(),Mobile.get(),Caste.get())
                    studentlist.delete(0,END)
                    studentlist.insert(END,StdID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),Gender.get() \
                                            ,Address.get(),Mobile.get(),Caste.get())
            def Search():
                studentlist.delete(0, END)
                for row in backend.search_data(StdID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),Gender.get(), \
                        Address.get(),Mobile.get(),Caste.get()):
                    studentlist.insert(END, row, str(""))
            def Delete():
                if (len(StdID.get()) != 0):
                    backend.delete_Rec(sd[0])
                    Clear()
                    Display()
            def Student_Rec(event):
                global sd
                searchStd = studentlist.curselection()[0]
                sd = studentlist.get(searchStd)
                self.txtStdID.delete(0,END)
                self.txtStdID.insert(END,sd[1])
                self.txtFirstname.delete(0,END)
                self.txtFirstname.insert(END,sd[2])
                self.txtLastname.delete(0,END)
                self.txtLastname.insert(END,sd[3])
                self.txtDob.delete(0,END)
                self.txtDob.insert(END,sd[4])
                self.txtAge.delete(0,END)
                self.txtAge.insert(END,sd[5])
                self.cbogender.delete(0,END)
                self.cbogender.insert(END,sd[6])
                self.txtAddress.delete(0,END)
                self.txtAddress.insert(END,sd[7])
                self.txtMobile.delete(0,END)
                self.txtMobile.insert(END,sd[8])
                self.txtcaste.delete(0, END)
                self.txtcaste.insert(END, sd[9])

            def update():
                if (len(StdID.get()) != 0):
                    backend.delete_Rec(sd[0])
                if (len(StdID.get()) != 0):
                    backend.AddStdrec(StdID.get(), Firstname.get(), Lastname.get(), Dob.get(), Age.get(), Gender.get(), \
                                      Address.get(), Mobile.get(),Caste.get())
                    studentlist.delete(0, END)
                    studentlist.insert(END, StdID.get(), Firstname.get(), Lastname.get(), Dob.get(), Age.get(), Gender.get() \
                                       , Address.get(), Mobile.get(),Caste.get())
            MAINFRAME = Frame(self.root,bd=10,width=1350,height=700,relief=RIDGE,bg="cadet blue")
            MAINFRAME.grid()




            TOPFRAME = Frame(MAINFRAME, bd=5, width=400, height=50, relief=RIDGE)
            TOPFRAME.pack(side=BOTTOM)
            TITLEFRAME = Frame(MAINFRAME, bd=5, width=1340, height=100, relief=RIDGE)
            TITLEFRAME.pack(side=TOP,anchor='w')
            TOPFRAME1 = Frame(MAINFRAME, bd=5, width=1340, height=500, relief=RIDGE)
            TOPFRAME1.pack(side=TOP,anchor='w')
            #
            # BUTTONFRAME = Frame(TOPFRAME, bd=5, width=1340, height=50, relief=RIDGE, bg="light green")
            # BUTTONFRAME.pack(anchor='e',side=RIGHT)

            LEFTFRAME = Frame(TOPFRAME1,bd=5,width=1340,relief=RIDGE,padx=2,bg="cadet blue",height=400)
            LEFTFRAME.pack(side=LEFT)
            LEFTFRAME1 = Frame(LEFTFRAME, bd=5, width=600, relief=RIDGE, padx=2,pady=4, height=180)
            LEFTFRAME1.pack(side=TOP,padx=0,pady=4)

            RIGHTFRAME = Frame(TOPFRAME1,bd=5,width=320,relief=RIDGE,padx=2,pady=4,bg="cadet blue",height=400)
            RIGHTFRAME.pack(side=RIGHT)
            RIGHTFRAME1 = Frame(RIGHTFRAME, bd=5, width=310, relief=RIDGE, padx=2, pady=2, height=200)
            RIGHTFRAME1.pack(side=TOP)

            # BUTTONFRAME1 = Frame(BUTTONFRAME,bd=5,width=200,relief=RIDGE,padx=2,pady=2,height=200)
            # BUTTONFRAME1.pack(side=RIGHT)
            self.labeltitle = Label(TITLEFRAME,font='arial 56 bold',bd=7,text="CANDIDA PUBLIC SCHOOL")
            self.labeltitle.grid(row=0,column=0,padx=132)

            self.labelStdID = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Student ID",anchor='w',justify=LEFT)
            self.labelStdID.grid(row=0, column=0, padx=5)
            self.txtStdID = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left',textvariable=StdID)
            self.txtStdID.grid(row=0, column=1)

            self.labelFirstname = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Firstname", anchor='w', justify=LEFT)
            self.labelFirstname.grid(row=1, column=0, padx=5)
            self.txtFirstname = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Firstname)
            self.txtFirstname.grid(row=1, column=1)

            self.labelLastname = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Lastname", anchor='w', justify=LEFT)
            self.labelLastname.grid(row=2, column=0, padx=5)
            self.txtLastname = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left',textvariable=Lastname)
            self.txtLastname.grid(row=2, column=1)

            self.labelDob = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Date of Birth", anchor='w', justify=LEFT)
            self.labelDob.grid(row=3, column=0, padx=5)
            self.txtDob = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left',textvariable=Dob)
            self.txtDob.grid(row=3, column=1)

            self.labelAge = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Age", anchor='w', justify=LEFT)
            self.labelAge.grid(row=4, column=0, padx=5)
            self.txtAge = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Age)
            self.txtAge.grid(row=4, column=1)

            self.genderlbl = Label(LEFTFRAME1,text="Gender",font='arial 12 bold').grid(row=5,column=0)
            self.cbogender = ttk.Combobox(LEFTFRAME1, font='arial 12 bold', width=39,state='readonly',justify='left',textvariable=Gender)
            self.cbogender['values'] = ['','Male','Female']
            self.cbogender.current(0)
            self.cbogender.grid(row=5,column=1)






            self.labelAddress = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Address", anchor='w', justify=LEFT)
            self.labelAddress.grid(row=6, column=0, padx=5)
            self.txtAddress = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Address)
            self.txtAddress.grid(row=6, column=1)

            self.labelMobile = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Mobile", anchor='w', justify=LEFT)
            self.labelMobile.grid(row=7, column=0, padx=5)
            self.txtMobile = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Mobile)
            self.txtMobile.grid(row=7, column=1)



            self.labelcaste = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Caste/Religion", anchor='w', justify=LEFT)
            self.labelcaste.grid(row=8, column=0, padx=5)
            self.txtcaste = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Caste)
            self.txtcaste.grid(row=8, column=1)


            scroll_bar = Scrollbar(RIGHTFRAME1)
            scroll_bar.grid(row=0,column=1,sticky="ns")


            studentlist = Listbox(RIGHTFRAME1,width=41,height=16,font="arial 12 bold",yscrollcommand=scroll_bar.set)
            studentlist.bind('<<ListboxSelect>>',Student_Rec)
            studentlist.grid(row=0,column=0,padx=8)
            scroll_bar.config(command=studentlist.yview)





            self.BtnAddnew = Button(TOPFRAME,pady=1,bd=4,font=('arial', 15,'bold'),text="Add New",width=11,padx=1,
                                    height=2,command=AddNew).grid(row=0,column=0,padx=1)
            self.BtnDisplay = Button(TOPFRAME, pady=1, bd=4, font=('arial',15, 'bold'), text="Display", width=11,padx=1,
                                    height=2,command=Display).grid(row=0, column=1, padx=1)
            self.BtnDelete = Button(TOPFRAME, pady=1, bd=4, font=('arial',15, 'bold'), text="Delete", width=11,padx=1,
                                    height=2,command=Delete).grid(row=0, column=2, padx=1)
            self.BtnClear = Button(TOPFRAME, pady=1, bd=4, font=('arial',15, 'bold'), text="Clear", width=11,padx=1,
                                    height=2,command=Clear).grid(row=0, column=3, padx=1)
            self.BtnExit = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Exit", width=11,padx=1,
                                    height=2,command=iExit).grid(row=0, column=4, padx=1)
            self.BtnSearch = Button(TOPFRAME, pady=1, bd=4, font=('arial',15 , 'bold'), text="Search", width=11,padx=1,
                                    height=2,command=Search).grid(row=0, column=5, padx=1)
            self.BtnUpdate = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Update", width=11, padx=1,
                                    height=2, command=update).grid(row=0, column=6, padx=1)
            self.Btncalculator = Button(RIGHTFRAME1,pady=1,padx=1,font="arial 10 bold",width=12,bg="light green",height=2,command=MoM,text="main",).grid(row=0,column=19)
    # .grid(row=0,column=9)
    if __name__ == '__main__':
        root = Tk()
        application = Student(root)
        root.mainloop()
def Students_marks():
        root1.destroy()
        class Student:
            def __init__(self, root):
                self.root = root
                blank_space = ""
                self.root.title("CANDIDA PUBLIC SCHOOL")
                self.root.geometry('1300x800+0+0')
                StdID = StringVar()
                Firstname = StringVar()
                Lastname = StringVar()
                CourseCode = StringVar()
                ExamName = StringVar()
                grade = StringVar()
                TotalPercent = StringVar()
                TotalMarks = StringVar()
                Parents = StringVar()
                English = StringVar()
                Science = StringVar()
                Hindi = StringVar()
                Social = StringVar()
                Moral = StringVar()
                Gk = StringVar()
                Sanskrit = StringVar()
                Art = StringVar()
                Maths = StringVar()

                def iExit():
                    iExit = tmsg.askyesno("CANDIDA PUBLIC SCHOOL", "Do you really want to quit")
                    if iExit > 0:
                        root.destroy()
                        return

                def Clear():
                    self.txtStdID.delete(0, END)
                    self.txtFirstname.delete(0, END)
                    self.txtLastname.delete(0, END)
                    self.txtCourseCode.delete(0, END)
                    self.txtExamname.delete(0, END)
                    self.txtParents.delete(0, END)
                    self.txtTotalmarks.delete(0, END)
                    self.txtTotalPercent.delete(0, END)
                    self.txtEnglish.delete(0, END)
                    self.cbograde.delete(0,END)
                    self.txtMaths.delete(0, END)
                    self.txtScience.delete(0, END)
                    self.txtHindi.delete(0, END)
                    self.txtMoralScience.delete(0, END)
                    self.txtGK.delete(0, END)
                    self.txtSanskrit.delete(0, END)
                    self.txtSocialScience.delete(0, END)
                    self.txtArt.delete(0, END)

                def Display():
                    studentlist.delete(0, END)
                    for row in Marksbackend.viewdata():
                        studentlist.insert(END, row, str(""))

                def AddNew():
                    if (len(StdID.get()) != 0):
                        Marksbackend.AddStdrec(StdID.get(), Firstname.get(), Lastname.get(),CourseCode.get(),ExamName.get(),grade.get(),TotalPercent.get(),TotalMarks.get(),Parents.get(),English.get(),Science.get(),Maths.get(),Hindi.get(),Social.get(),Gk.get() ,Art.get(),Moral.get(),\
                                               Sanskrit.get(),)
                        studentlist.delete(0, END)
                        studentlist.insert(END,StdID.get(), Firstname.get(), Lastname.get(),CourseCode.get(),ExamName.get(),grade.get(),TotalPercent.get(),TotalMarks.get(),Parents.get(),English.get(),Science.get(),Maths.get(),Hindi.get(),Social.get(),Gk.get() ,Art.get(),Moral.get(),\
                                               Sanskrit.get(),)

                def Search():
                    studentlist.delete(0, END)
                    for row in Marksbackend.search_data(StdID.get(), Firstname.get(), Lastname.get(),CourseCode.get(),ExamName.get(),grade.get(),TotalPercent.get(),TotalMarks.get(),Parents.get(),English.get(),Science.get(),Maths.get(),Hindi.get(),Social.get(),Gk.get() ,Art.get(),Moral.get(),\
                                               Sanskrit.get()):
                        studentlist.insert(END, row, str(""))

                def Delete():
                    if (len(StdID.get()) != 0):
                        Marksbackend.delete_Rec(sd[0])
                        Clear()
                        Display()

                def Student_Rec(event):
                    global sd
                    searchStd = studentlist.curselection()[0]
                    sd = studentlist.get(searchStd)
                    self.txtStdID.delete(0, END)
                    self.txtStdID.insert(END, sd[1])
                    self.txtFirstname.delete(0, END)
                    self.txtFirstname.insert(END, sd[2])
                    self.txtLastname.delete(0, END)
                    self.txtLastname.insert(END, sd[3])
                    self.txtCourseCode.delete(0, END)
                    self.txtCourseCode.insert(END, sd[4])
                    self.txtExamname.delete(0, END)
                    self.txtExamname.insert(END, sd[5])
                    self.cbograde.delete(0, END)
                    self.cbograde.insert(END, sd[6])
                    self.txtTotalPercent.delete(0, END)
                    self.txtTotalPercent.insert(END, sd[7])
                    self.txtTotalmarks.delete(0, END)
                    self.txtTotalmarks.insert(END, sd[8])
                    self.txtParents.delete(0, END)
                    self.txtParents.insert(END, sd[9])


                    self.txtEnglish.delete(0, END)
                    self.txtEnglish.insert(END, sd[10])
                    self.txtScience.delete(0, END)
                    self.txtScience.insert(END, sd[11])
                    self.txtMaths.delete(0, END)
                    self.txtMaths.insert(END, sd[12])

                    self.txtHindi.delete(0, END)
                    self.txtHindi.insert(END, sd[13])
                    self.txtSocialScience.delete(0, END)
                    self.txtSocialScience.insert(END, sd[14])
                    self.txtGK.delete(0, END)
                    self.txtGK.insert(END, sd[15])
                    self.txtArt.delete(0, END)
                    self.txtArt.insert(END, sd[16])
                    self.txtMoralScience.delete(0, END)
                    self.txtMoralScience.insert(END, sd[17])
                    self.txtSanskrit.delete(0, END)
                    self.txtSanskrit.insert(END, sd[18])




                def update():
                    if (len(StdID.get()) != 0):
                        Marksbackend.delete_Rec(sd[0])
                    if (len(StdID.get()) != 0):
                        Marksbackend.AddStdrec(StdID.get(), Firstname.get(), Lastname.get(),CourseCode.get(),ExamName.get(),grade.get(),TotalPercent.get(),TotalMarks.get(),Parents.get(),English.get(),Science.get(),Maths.get(),Hindi.get(),Social.get(),Gk.get() ,Art.get(),Moral.get(),\
                                               Sanskrit.get())
                        studentlist.delete(0, END)
                        studentlist.insert(END,StdID.get(), Firstname.get(), Lastname.get(),CourseCode.get(),ExamName.get(),grade.get(),TotalPercent.get(),TotalMarks.get(),Parents.get(),English.get(),Science.get(),Maths.get(),Hindi.get(),Social.get(),Gk.get() ,Art.get(),Moral.get(),\
                                               Sanskrit.get())

                MAINFRAME = Frame(self.root, bd=10, width=1350, height=700, relief=RIDGE, bg="cadet blue")
                MAINFRAME.grid()

                TOPFRAME = Frame(MAINFRAME, bd=5, width=400, height=50, relief=RIDGE)
                TOPFRAME.pack(side=BOTTOM)
                TITLEFRAME = Frame(MAINFRAME, bd=5, width=1340, height=100, relief=RIDGE)
                TITLEFRAME.pack(side=TOP, anchor='w')
                TOPFRAME1 = Frame(MAINFRAME, bd=5, width=1340, height=500, relief=RIDGE)
                TOPFRAME1.pack(side=TOP, anchor='w')
                #
                # BUTTONFRAME = Frame(TOPFRAME, bd=5, width=1340, height=50, relief=RIDGE, bg="light green")
                # BUTTONFRAME.pack(anchor='e',side=RIGHT)

                LEFTFRAME = Frame(TOPFRAME1, bd=5, width=1340, relief=RIDGE, padx=2, bg="cadet blue", height=400)
                LEFTFRAME.pack(side=LEFT)
                LEFTFRAME1 = Frame(LEFTFRAME, bd=5, width=600, relief=RIDGE, padx=2, pady=4, height=180)
                LEFTFRAME1.pack(side=TOP, padx=0, pady=4)

                RIGHTFRAME = Frame(TOPFRAME1, bd=5, width=320, relief=RIDGE, padx=2, pady=4, bg="cadet blue",
                                   height=400)
                RIGHTFRAME.pack(side=RIGHT)
                RIGHTFRAME1 = Frame(RIGHTFRAME, bd=5, width=310, relief=RIDGE, padx=2, pady=2, height=200)
                RIGHTFRAME1.pack(side=TOP)

                self.labeltitle = Label(TITLEFRAME, font='arial 56 bold', bd=7, text="CANDIDA PUBLIC SCHOOL")
                self.labeltitle.grid(row=0, column=0, padx=132)

                self.labelStdID = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Student ID",anchor='w',justify=LEFT)
                self.labelStdID.grid(row=0, column=0, padx=5)
                self.txtStdID = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left',textvariable=StdID)
                self.txtStdID.grid(row=0, column=1)

                self.labelFirstname = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Firstname", anchor='w', justify=LEFT)
                self.labelFirstname.grid(row=1, column=0, padx=5)
                self.txtFirstname = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left', textvariable=Firstname)
                self.txtFirstname.grid(row=1, column=1)

                self.labelLastname = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Lastname", anchor='w', justify=LEFT)
                self.labelLastname.grid(row=2, column=0, padx=5)
                self.txtLastname = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left',textvariable=Lastname)
                self.txtLastname.grid(row=2, column=1)

                self.labelCourseCode = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Course code", anchor='w', justify=LEFT)
                self.labelCourseCode.grid(row=3, column=0, padx=5)
                self.txtCourseCode = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left',textvariable=CourseCode)
                self.txtCourseCode.grid(row=3, column=1)

                self.labelExamname = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Exam name", anchor='w', justify=LEFT)
                self.labelExamname.grid(row=4, column=0, padx=5)
                self.txtExamname = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left', textvariable=ExamName)
                self.txtExamname.grid(row=4, column=1)

                self.gradelbl = Label(LEFTFRAME1,text="grade ",font='arial 12 bold').grid(row=5,column=0)
                self.cbograde = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left', textvariable=grade)

                self.cbograde.grid(row=5,column=1)






                self.labelTotalPercent = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="TotalPercent", anchor='w', justify=LEFT)
                self.labelTotalPercent.grid(row=6, column=0, padx=5)
                self.txtTotalPercent = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left', textvariable=TotalPercent)
                self.txtTotalPercent.grid(row=6, column=1)


                self.labelTotalmarks = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Totalmarks", anchor='w',
                                         justify=LEFT)
                self.labelTotalmarks.grid(row=7, column=0, padx=5)
                self.txtTotalmarks = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left',
                                       textvariable=TotalMarks)
                self.txtTotalmarks.grid(row=7, column=1)

                self.labelParents = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Parents or Guardian", anchor='w',
                                             justify=LEFT)
                self.labelParents.grid(row=8, column=0, padx=5)
                self.txtParents = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left',
                                           textvariable=Parents)
                self.txtParents.grid(row=8, column=1)

                # subjects of labels and entry
                self.labelEnglish = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="English", anchor='w',
                                             justify=LEFT)
                self.labelEnglish.grid(row=0, column=3, padx=5)
                self.txtEnglish = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left',
                                           textvariable=English)
                self.txtEnglish.grid(row=0, column=4)

                self.labelScience = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Science", anchor='w',
                                          justify=LEFT)
                self.labelScience.grid(row=1, column=3, padx=5)
                self.txtScience = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left',
                                        textvariable=Science)
                self.txtScience.grid(row=1, column=4)


                self.labelMaths = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Maths", anchor='w',
                                          justify=LEFT)
                self.labelMaths.grid(row=2, column=3, padx=5)
                self.txtMaths = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left',
                                        textvariable=Maths)
                self.txtMaths.grid(row=2, column=4)

                self.labelHindi = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Hindi", anchor='w',
                                        justify=LEFT)
                self.labelHindi.grid(row=3, column=3, padx=5)
                self.txtHindi = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left',
                                      textvariable=Hindi)
                self.txtHindi.grid(row=3, column=4)



                self.labelSocialScience = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Social Science", anchor='w',
                                        justify=LEFT)
                self.labelSocialScience.grid(row=4, column=3, padx=5)
                self.txtSocialScience = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left',
                                      textvariable=Social)
                self.txtSocialScience.grid(row=4, column=4)

                self.labelGK = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="G.K", anchor='w',
                                        justify=LEFT)
                self.labelGK.grid(row=5, column=3, padx=5)
                self.txtGK = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left',
                                      textvariable=Gk)
                self.txtGK.grid(row=5, column=4)


                self.labelArt = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Art", anchor='w',
                                        justify=LEFT)
                self.labelArt.grid(row=6, column=3, padx=5)
                self.txtArt = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left',
                                      textvariable=Art)
                self.txtArt.grid(row=6, column=4)

                self.labelMoralScience = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Moral Science", anchor='w',
                                      justify=LEFT)
                self.labelMoralScience.grid(row=7, column=3, padx=5)
                self.txtMoralScience = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left',
                                    textvariable=Moral)
                self.txtMoralScience.grid(row=7, column=4)

                self.labelSanskrit = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Sanskrit", anchor='w',
                                      justify=LEFT)
                self.labelSanskrit.grid(row=8, column=3, padx=5)
                self.txtSanskrit = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=10, justify='left',
                                    textvariable=Sanskrit)
                self.txtSanskrit.grid(row=8, column=4)

                scroll_bar = Scrollbar(RIGHTFRAME1)
                scroll_bar.grid(row=0,column=1,sticky="ns")


                studentlist = Listbox(RIGHTFRAME1,width=41,height=16,font="arial 12 bold",yscrollcommand=scroll_bar.set)
                studentlist.bind('<<ListboxSelect>>',Student_Rec)
                studentlist.grid(row=0,column=0,padx=8)
                scroll_bar.config(command=studentlist.yview)





                self.BtnAddnew = Button(TOPFRAME,pady=1,bd=4,font=('arial', 15,'bold'),text="Add New",width=11,padx=1,
                                        height=2,command=AddNew).grid(row=0,column=0,padx=1)
                self.BtnDisplay = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Display", width=11,padx=1,
                                        height=2,command=Display).grid(row=0, column=1, padx=1)
                self.BtnDelete = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Delete", width=11,padx=1,
                                        height=2,command=Delete).grid(row=0, column=2, padx=1)
                self.BtnClear = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Clear", width=11,padx=1,
                                        height=2,command=Clear).grid(row=0, column=3, padx=1)
                self.BtnExit = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Exit", width=11,padx=1,
                                        height=2,command=iExit).grid(row=0, column=4, padx=1)
                self.BtnSearch = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Search", width=11,padx=1,
                                        height=2,command=Search).grid(row=0, column=5, padx=1)
                self.BtnUpdate = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Update", width=11, padx=1,
                                        height=2, command=update).grid(row=0, column=6, padx=1)
                self.Btncalculator = Button(RIGHTFRAME1, pady=1, padx=1, font="arial 10 bold", width=12,
                                            bg="light green", height=2, command=MoM, text="main", ).grid(row=0,
                                                                                                         column=19)

            # .grid(row=0,column=9)

        if __name__ == '__main__':
            root = Tk()
            application = Student(root)
            root.mainloop()
def Students_fee():
    root1.destroy()
    class Student:
        def __init__(self,root):
            self.root = root
            blank_space= ""
            self.root.title("CANDIDA PUBLIC SCHOOL")
            self.root.geometry('1300x800+0+0')
            StdID = StringVar()
            Firstname = StringVar()
            Lastname = StringVar()
            Dob = StringVar()
            Age  = StringVar()
            Gender = StringVar()
            Address = StringVar()
            Mobile = StringVar()


            def iExit():
                iExit = tmsg.askyesno("CANDIDA PUBLIC SCHOOL","Do you really want to quit")
                if iExit > 0:
                    root.destroy()
                    return
            def Clear():
                self.txtStdID.delete(0,END)
                self.txtFirstname.delete(0,END)
                self.txtLastname.delete(0,END)
                self.txtDob.delete(0,END)
                self.txtAge.delete(0,END)
                self.cbogender.delete(0,END)
                self.txtAddress.delete(0,END)
                self.txtMobile.delete(0,END)
            def Display():
                studentlist.delete(0,END)
                for row in feebackend.viewdata():
                    studentlist.insert(END,row,str(""))
            def AddNew():
                if (len(StdID.get()) != 0):
                    feebackend.AddStdrec(StdID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),Gender.get(), \
                                      Address.get(),Mobile.get())
                    studentlist.delete(0,END)
                    studentlist.insert(END,StdID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),Gender.get() \
                                            ,Address.get(),Mobile.get())
            def Search():
                studentlist.delete(0, END)
                for row in feebackend.search_data(StdID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),Gender.get(), \
                        Address.get(),Mobile.get()):
                    studentlist.insert(END, row, str(""))
            def Delete():
                if (len(StdID.get()) != 0):
                    feebackend.delete_Rec(sd[0])
                    Clear()
                    Display()
            def Student_Rec(event):
                global sd
                searchStd = studentlist.curselection()[0]
                sd = studentlist.get(searchStd)
                self.txtStdID.delete(0,END)
                self.txtStdID.insert(END,sd[1])
                self.txtFirstname.delete(0,END)
                self.txtFirstname.insert(END,sd[2])
                self.txtLastname.delete(0,END)
                self.txtLastname.insert(END,sd[3])
                self.txtDob.delete(0,END)
                self.txtDob.insert(END,sd[4])
                self.txtAge.delete(0,END)
                self.txtAge.insert(END,sd[5])
                self.cbogender.delete(0,END)
                self.cbogender.insert(END,sd[6])
                self.txtAddress.delete(0,END)
                self.txtAddress.insert(END,sd[7])
                self.txtMobile.delete(0,END)
                self.txtMobile.insert(END,sd[8])
            def update():
                if (len(StdID.get()) != 0):
                    feebackend.delete_Rec(sd[0])
                if (len(StdID.get()) != 0):
                    feebackend.AddStdrec(StdID.get(), Firstname.get(), Lastname.get(), Dob.get(), Age.get(), Gender.get(), \
                                      Address.get(), Mobile.get())
                    studentlist.delete(0, END)
                    studentlist.insert(END, StdID.get(), Firstname.get(), Lastname.get(), Dob.get(), Age.get(), Gender.get() \
                                       , Address.get(), Mobile.get())
            MAINFRAME = Frame(self.root,bd=10,width=1350,height=700,relief=RIDGE,bg="cadet blue")
            MAINFRAME.grid()




            TOPFRAME = Frame(MAINFRAME, bd=5, width=400, height=50, relief=RIDGE)
            TOPFRAME.pack(side=BOTTOM)
            TITLEFRAME = Frame(MAINFRAME, bd=5, width=1340, height=100, relief=RIDGE)
            TITLEFRAME.pack(side=TOP,anchor='w')
            TOPFRAME1 = Frame(MAINFRAME, bd=5, width=1340, height=500, relief=RIDGE)
            TOPFRAME1.pack(side=TOP,anchor='w')
            #
            # BUTTONFRAME = Frame(TOPFRAME, bd=5, width=1340, height=50, relief=RIDGE, bg="light green")
            # BUTTONFRAME.pack(anchor='e',side=RIGHT)

            LEFTFRAME = Frame(TOPFRAME1,bd=5,width=1340,relief=RIDGE,padx=2,bg="cadet blue",height=400)
            LEFTFRAME.pack(side=LEFT)
            LEFTFRAME1 = Frame(LEFTFRAME, bd=5, width=600, relief=RIDGE, padx=2,pady=4, height=180)
            LEFTFRAME1.pack(side=TOP,padx=0,pady=4)

            RIGHTFRAME = Frame(TOPFRAME1,bd=5,width=320,relief=RIDGE,padx=2,pady=4,bg="cadet blue",height=400)
            RIGHTFRAME.pack(side=RIGHT)
            RIGHTFRAME1 = Frame(RIGHTFRAME, bd=5, width=310, relief=RIDGE, padx=2, pady=2, height=200)
            RIGHTFRAME1.pack(side=TOP)

            # BUTTONFRAME1 = Frame(BUTTONFRAME,bd=5,width=200,relief=RIDGE,padx=2,pady=2,height=200)
            # BUTTONFRAME1.pack(side=RIGHT)
            self.labeltitle = Label(TITLEFRAME,font='arial 56 bold',bd=7,text="CANDIDA PUBLIC SCHOOL")
            self.labeltitle.grid(row=0,column=0,padx=132)

            self.labelStdID = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Student ID",anchor='w',justify=LEFT)
            self.labelStdID.grid(row=0, column=0, padx=5)
            self.txtStdID = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left',textvariable=StdID)
            self.txtStdID.grid(row=0, column=1)

            self.labelFirstname = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Firstname", anchor='w', justify=LEFT)
            self.labelFirstname.grid(row=1, column=0, padx=5)
            self.txtFirstname = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Firstname)
            self.txtFirstname.grid(row=1, column=1)

            self.labelLastname = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Lastname", anchor='w', justify=LEFT)
            self.labelLastname.grid(row=2, column=0, padx=5)
            self.txtLastname = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left',textvariable=Lastname)
            self.txtLastname.grid(row=2, column=1)

            self.labelDob = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Amount of fee", anchor='w', justify=LEFT)
            self.labelDob.grid(row=3, column=0, padx=5)
            self.txtDob = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left',textvariable=Dob)
            self.txtDob.grid(row=3, column=1)

            self.labelAge = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="of which month", anchor='w', justify=LEFT)
            self.labelAge.grid(row=4, column=0, padx=5)
            self.txtAge = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Age)
            self.txtAge.grid(row=4, column=1)

            self.genderlbl = Label(LEFTFRAME1,text="is his/her fee is pending",font='arial 12 bold').grid(row=5,column=0)
            self.cbogender = ttk.Combobox(LEFTFRAME1, font='arial 12 bold', width=39,state='readonly',justify='left',textvariable=Gender)
            self.cbogender['values'] = ['','pending','given','given advanced']
            self.cbogender.current(0)
            self.cbogender.grid(row=5,column=1)






            self.labelAddress = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="to which month", anchor='w', justify=LEFT)
            self.labelAddress.grid(row=6, column=0, padx=5)
            self.txtAddress = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Address)
            self.txtAddress.grid(row=6, column=1)

            self.labelMobile = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Mobile", anchor='w', justify=LEFT)
            self.labelMobile.grid(row=7, column=0, padx=5)
            self.txtMobile = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Mobile)
            self.txtMobile.grid(row=7, column=1)


            scroll_bar = Scrollbar(RIGHTFRAME1)
            scroll_bar.grid(row=0,column=1,sticky="ns")


            studentlist = Listbox(RIGHTFRAME1,width=41,height=16,font="arial 12 bold",yscrollcommand=scroll_bar.set)
            studentlist.bind('<<ListboxSelect>>',Student_Rec)
            studentlist.grid(row=0,column=0,padx=8)
            scroll_bar.config(command=studentlist.yview)

            self.BtnAddnew = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Add New", width=11,
                                    padx=1,
                                    height=2, command=AddNew).grid(row=0, column=0, padx=1)
            self.BtnDisplay = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Display", width=11,
                                     padx=1,
                                     height=2, command=Display).grid(row=0, column=1, padx=1)
            self.BtnDelete = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Delete", width=11, padx=1,
                                    height=2, command=Delete).grid(row=0, column=2, padx=1)
            self.BtnClear = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Clear", width=11, padx=1,
                                   height=2, command=Clear).grid(row=0, column=3, padx=1)
            self.BtnExit = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Exit", width=11, padx=1,
                                  height=2, command=iExit).grid(row=0, column=4, padx=1)
            self.BtnSearch = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Search", width=11, padx=1,
                                    height=2, command=Search).grid(row=0, column=5, padx=1)
            self.BtnUpdate = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Update", width=11, padx=1,
                                    height=2, command=update).grid(row=0, column=6, padx=1)
            self.Btncalculator = Button(RIGHTFRAME1, pady=1, padx=1, font="arial 10 bold", width=12, bg="light green",
                                        height=2, command=MoM, text="main", ).grid(row=0, column=19)
    if __name__ == '__main__':
        root = Tk()
        application = Student(root)
        root.mainloop()
def Teacher_salary():
    global root
    root1.destroy()
    class Student:
        def __init__(self,root):
            self.root = root
            blank_space= ""
            self.root.title("CANDIDA PUBLIC SCHOOL")
            self.root.geometry('1300x800+0+0')
            StdID = StringVar()
            Firstname = StringVar()
            Lastname = StringVar()
            Dob = StringVar()
            Age  = StringVar()
            Gender = StringVar()
            Address = StringVar()
            Mobile = StringVar()


            def iExit():
                iExit = tmsg.askyesno("CANDIDA PUBLIC SCHOOL","Do you really want to quit")
                if iExit > 0:
                    root.destroy()
                    return
            def Clear():
                self.txtStdID.delete(0,END)
                self.txtFirstname.delete(0,END)
                self.txtLastname.delete(0,END)
                self.txtDob.delete(0,END)
                self.txtAge.delete(0,END)
                self.cbogender.delete(0,END)
                self.txtAddress.delete(0,END)
                self.txtMobile.delete(0,END)
            def Display():
                studentlist.delete(0,END)
                for row in salarybackend.viewdata():
                    studentlist.insert(END,row,str(""))
            def AddNew():

                if (len(StdID.get()) != 0):
                    salarybackend.AddStdrec(StdID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),Gender.get(), \
                                      Address.get(),Mobile.get())
                    studentlist.delete(0,END)
                    studentlist.insert(END,StdID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),Gender.get() \
                                            ,Address.get(),Mobile.get())
                Clear()
            def Search():
                studentlist.delete(0, END)
                for row in salarybackend.search_data(StdID.get(),Firstname.get(),Lastname.get(),Dob.get(),Age.get(),Gender.get(), \
                        Address.get(),Mobile.get()):
                    studentlist.insert(END, row, str(""))
            def Delete():
                if (len(StdID.get()) != 0):
                    salarybackend.delete_Rec(sd[0])
                    Clear()
                    Display()
            def Student_Rec(event):
                global sd
                searchStd = studentlist.curselection()[0]
                sd = studentlist.get(searchStd)
                self.txtStdID.delete(0,END)
                self.txtStdID.insert(END,sd[1])
                self.txtFirstname.delete(0,END)
                self.txtFirstname.insert(END,sd[2])
                self.txtLastname.delete(0,END)
                self.txtLastname.insert(END,sd[3])
                self.txtDob.delete(0,END)
                self.txtDob.insert(END,sd[4])
                self.txtAge.delete(0,END)
                self.txtAge.insert(END,sd[5])
                self.cbogender.delete(0,END)
                self.cbogender.insert(END,sd[6])
                self.txtAddress.delete(0,END)
                self.txtAddress.insert(END,sd[7])
                self.txtMobile.delete(0,END)
                self.txtMobile.insert(END,sd[8])
            def update():
                if (len(StdID.get()) != 0):
                    salarybackend.delete_Rec(sd[0])
                if (len(StdID.get()) != 0):
                    salarybackend.AddStdrec(StdID.get(), Firstname.get(), Lastname.get(), Dob.get(), Age.get(), Gender.get(), \
                                      Address.get(), Mobile.get())
                    studentlist.delete(0, END)
                    studentlist.insert(END, StdID.get(), Firstname.get(), Lastname.get(), Dob.get(), Age.get(), Gender.get() \
                                       , Address.get(), Mobile.get())
            MAINFRAME = Frame(self.root,bd=10,width=1350,height=700,relief=RIDGE,bg="cadet blue")
            MAINFRAME.grid()




            TOPFRAME = Frame(MAINFRAME, bd=5, width=400, height=50, relief=RIDGE)
            TOPFRAME.pack(side=BOTTOM)
            TITLEFRAME = Frame(MAINFRAME, bd=5, width=1340, height=100, relief=RIDGE)
            TITLEFRAME.pack(side=TOP,anchor='w')
            TOPFRAME1 = Frame(MAINFRAME, bd=5, width=1340, height=500, relief=RIDGE)
            TOPFRAME1.pack(side=TOP,anchor='w')
            #
            # BUTTONFRAME = Frame(TOPFRAME, bd=5, width=1340, height=50, relief=RIDGE, bg="light green")
            # BUTTONFRAME.pack(anchor='e',side=RIGHT)

            LEFTFRAME = Frame(TOPFRAME1,bd=5,width=1340,relief=RIDGE,padx=2,bg="cadet blue",height=400)
            LEFTFRAME.pack(side=LEFT)
            LEFTFRAME1 = Frame(LEFTFRAME, bd=5, width=600, relief=RIDGE, padx=2,pady=4, height=180)
            LEFTFRAME1.pack(side=TOP,padx=0,pady=4)

            RIGHTFRAME = Frame(TOPFRAME1,bd=5,width=320,relief=RIDGE,padx=2,pady=4,bg="cadet blue",height=400)
            RIGHTFRAME.pack(side=RIGHT)
            RIGHTFRAME1 = Frame(RIGHTFRAME, bd=5, width=310, relief=RIDGE, padx=2, pady=2, height=200)
            RIGHTFRAME1.pack(side=TOP)

            # BUTTONFRAME1 = Frame(BUTTONFRAME,bd=5,width=200,relief=RIDGE,padx=2,pady=2,height=200)
            # BUTTONFRAME1.pack(side=RIGHT)
            self.labeltitle = Label(TITLEFRAME,font='arial 56 bold',bd=7,text="CANDIDA PUBLIC SCHOOL")
            self.labeltitle.grid(row=0,column=0,padx=132)

            self.labelStdID = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Teacher ID",anchor='w',justify=LEFT)
            self.labelStdID.grid(row=0, column=0, padx=5)
            self.txtStdID = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left',textvariable=StdID)
            self.txtStdID.grid(row=0, column=1)

            self.labelFirstname = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Firstname", anchor='w', justify=LEFT)
            self.labelFirstname.grid(row=1, column=0, padx=5)
            self.txtFirstname = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Firstname)
            self.txtFirstname.grid(row=1, column=1)

            self.labelLastname = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Lastname", anchor='w', justify=LEFT)
            self.labelLastname.grid(row=2, column=0, padx=5)
            self.txtLastname = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left',textvariable=Lastname)
            self.txtLastname.grid(row=2, column=1)

            self.labelDob = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="amount of salary", anchor='w', justify=LEFT)
            self.labelDob.grid(row=3, column=0, padx=5)
            self.txtDob = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left',textvariable=Dob)
            self.txtDob.grid(row=3, column=1)

            self.labelAge = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="from which month", anchor='w', justify=LEFT)
            self.labelAge.grid(row=4, column=0, padx=5)
            self.txtAge = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Age)
            self.txtAge.grid(row=4, column=1)

            self.genderlbl = Label(LEFTFRAME1,text="is pending or not?",font='arial 12 bold').grid(row=5,column=0)
            self.cbogender = ttk.Combobox(LEFTFRAME1, font='arial 12 bold', width=39,state='readonly',justify='left',textvariable=Gender)
            self.cbogender['values'] = ['','pending','given','advanced']
            self.cbogender.current(0)
            self.cbogender.grid(row=5,column=1)






            self.labelAddress = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="to which month", anchor='w', justify=LEFT)
            self.labelAddress.grid(row=6, column=0, padx=5)
            self.txtAddress = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Address)
            self.txtAddress.grid(row=6, column=1)

            self.labelMobile = Label(LEFTFRAME1, font='arial 12 bold', bd=7, text="Mobile", anchor='w', justify=LEFT)
            self.labelMobile.grid(row=7, column=0, padx=5)
            self.txtMobile = Entry(LEFTFRAME1, font='arial 12 bold', bd=5, width=40, justify='left', textvariable=Mobile)
            self.txtMobile.grid(row=7, column=1)


            scroll_bar = Scrollbar(RIGHTFRAME1)
            scroll_bar.grid(row=0,column=1,sticky="ns")


            studentlist = Listbox(RIGHTFRAME1,width=41,height=16,font="arial 12 bold",yscrollcommand=scroll_bar.set)
            studentlist.bind('<<ListboxSelect>>',Student_Rec)
            studentlist.grid(row=0,column=0,padx=8)
            scroll_bar.config(command=studentlist.yview)

            self.BtnAddnew = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Add New", width=11,
                                    padx=1,
                                    height=2, command=AddNew).grid(row=0, column=0, padx=1)
            self.BtnDisplay = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Display", width=11,
                                     padx=1,
                                     height=2, command=Display).grid(row=0, column=1, padx=1)
            self.BtnDelete = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Delete", width=11, padx=1,
                                    height=2, command=Delete).grid(row=0, column=2, padx=1)
            self.BtnClear = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Clear", width=11, padx=1,
                                   height=2, command=Clear).grid(row=0, column=3, padx=1)
            self.BtnExit = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Exit", width=11, padx=1,
                                  height=2, command=iExit).grid(row=0, column=4, padx=1)
            self.BtnSearch = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Search", width=11, padx=1,
                                    height=2, command=Search).grid(row=0, column=5, padx=1)
            self.BtnUpdate = Button(TOPFRAME, pady=1, bd=4, font=('arial', 15, 'bold'), text="Update", width=11, padx=1,
                                    height=2, command=update).grid(row=0, column=6, padx=1)
            self.Btncalculator = Button(RIGHTFRAME1, pady=1, padx=1, font="arial 10 bold", width=12, bg="light green",
                                        height=2, command=MoM, text="main", ).grid(row=0, column=19)
    if __name__ == '__main__':
        root = Tk()
        application = Student(root)
        root.mainloop()
main()