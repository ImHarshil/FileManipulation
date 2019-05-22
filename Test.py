from tkinter import *
import easygui
from kivy import *
from FileManipulation import FileManupulation

root = Tk()
root.geometry("1300x600")
root.title("File Manipulation")
root.configure(bg="black")

heading = Label(root, text="File Manipulation Software", height=5, width=100, font=(
    "arial", 20, "bold"), relief="raised", border=2, bg="black", fg="white").pack()


frame = Frame(root, bg="black")
frame.pack()

label1 = Label(frame, text="Enter file path \n with file name", width=50,
               border=3, fg="white", bg="black").pack(side=LEFT)

inputtext = Entry(frame, textvariable="input file path", width=55,
                  font=("arial", 20, "italic"), bg="white", fg="black")
inputtext.pack(side=RIGHT)

frame1 = Frame(root, bg="black")
frame1.pack()


label1 = Label(frame1, text="Enter file2 path \n with file name", width=50, border=3, fg="white", bg="black").pack(
    side=LEFT)

inputtext1 = Entry(frame1, textvariable="input file1 path", width=55,
                   font=("arial", 20, "italic"), bg="yellow", fg="black")
inputtext1.pack(side=RIGHT)


def func_show():
    root2 = Toplevel()
    val = inputtext.get()
    con = FileManupulation(val).show_file()+""
    Label(root2, text=con, width=100, height=5, bg="white").pack()
    root2.mainloop()


def func_delete():
    FileManupulation(inputtext.get()).delete_file(inputtext.get())


def func_create():
    FileManupulation(inputtext.get()).create_file(inputtext.get())


def func_append_file():
    FileManupulation(inputtext.get()).append_file(inputtext1.get())


def func_append_content():
    e = easygui.codebox(msg='enter data to be appended', title="append content")
    if(e != ""):
        FileManupulation(inputtext.get()).append_content(e)


def func_replace():
    if(inputtext.get() == ""):
        easygui.exceptionbox(msg="enter file name with its path", title="WARNING")
        return

    e = easygui.enterbox(msg="enter value to be replaced", title="replace text", default="")
    e2 = easygui.enterbox(msg="replace previous value with", title="replace with text", default="")
    if(easygui.boolbox(msg="Are you  sure", title="confirm")):
        FileManupulation(inputtext.get()).replace_all(e, e2)


def func_delete_data():
    if(easygui.boolbox(msg="Are you  sure to delete content of file", title="confirm")):
        FileManupulation(inputtext.get()).delete_content()


bottomframe = Frame(root, width=1000, height=400, bg="white")
bottomframe.pack(side=BOTTOM)
show = Button(bottomframe, text="show file content", fg="white",
              bg="green", command=func_show, height=3).pack(side=LEFT)
replacetext = Button(bottomframe, text="replace text", fg="white", bg="purple",
                     height=3, command=func_replace).pack(side=LEFT)
deleteFile = Button(bottomframe, text="delete file", fg="white", bg="red",
                    height=3, command=func_delete).pack(side=LEFT)
createFile = Button(bottomframe, text="create file", fg="black", bg="yellow",
                    height=3, command=func_create).pack(side=LEFT)
deletedata = Button(bottomframe, text="delete data", fg="white", bg="brown",
                    height=3, command=func_delete_data).pack(side=LEFT)
appendcontent = Button(bottomframe, text="append content", fg="white",
                       bg="black", height=3, command=func_append_content).pack(side=LEFT)
appendfile = Button(bottomframe, text="apppend file", fg="black",
                    bg="white", height=3, command=func_append_file).pack()
root.mainloop()
