from tkinter import *
def open1(summary):
	with open("record of CANDIDA PUBLIC SCHOOL.txt","r") as f:
		content = f.read()
		print(content)


def get_me():

    entry_value = entry.get()
    answer.delete(1.0, END)
    answer_value = open1(entry_value)
    answer.insert(INSERT, answer_value)


root = Tk()

topframe = Frame(root)
entry = Entry(topframe)
entry.pack()
button = Button(topframe, text="search", command=get_me)
button.pack()
topframe.pack(side = TOP)


bottomframe = Frame(root)
scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)
answer =  Text(bottomframe, width=30, height=10, yscrollcommand = scroll.set, wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()
bottomframe.pack()

root.mainloop()

