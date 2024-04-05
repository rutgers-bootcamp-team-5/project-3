import csv
import os
from tkinter import *
from datetime import datetime
from tkinter import filedialog


# initialize Tkinter which manages the GUI elements
root = Tk()
root.geometry("600x400")
root.title('Project 3')
# Gets the requested values of the height and width.
winWidth = root.winfo_reqwidth()
winHeight = root.winfo_reqheight()
posRight = int(root.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(root.winfo_screenheight() / 2 - winHeight / 2)
posRight = int(posRight / 2)

root.geometry("+{}+{}".format(posRight, posDown))




def Run():

    #if not temp1 :
        finished()
    #else:
        #err = Toplevel(root)
        #err.geometry("400x200")
        #err.title("Failed")
        #err.geometry("+{}+{}".format(posRight + 100, posDown))
        #Button(err, text='close', height=2, width=10, command=exitButton()).pack(side=BOTTOM, pady=10)
        #Label(err, text="Failed, Select the file", font=('Arial', 12)).pack(side=TOP, pady=50)



File1Path = StringVar()
File2Path = StringVar()


def open_file1():
    global temp1
    file_path = filedialog.askopenfilename(initialdir = "C:\Data",
                                          title = "Select a File",
                                          filetypes = (("CSV files",
                                                        "*.csv*"),
                                                       ("All Files",
                                                        "*.*")))
    if file_path is not None:
        temp1 = file_path
        File1Path.set(temp1)
        return temp1
    
def open_file2():
    global temp2
    file_path = filedialog.askopenfilename(initialdir = "C:\Data",
                                          title = "Select a File",
                                          filetypes = (("CSV files",
                                                        "*.csv*"),
                                                       ("All Files",
                                                        "*.*")))
    if file_path is not None:
        temp2 = file_path
        File2Path.set(temp2)
        return temp2

frame1 = Frame()
frame1.pack(fill=X)
frame2 = Frame()
frame2.pack(fill=X)
frame3 = Frame()
frame3.pack(fill=X)
frame4 = Frame()
frame4.pack(fill=X)
frame5 = Frame()
frame5.pack(fill=X)
frame6 = Frame()
frame6.pack(fill=X)

biglabel = Label(frame1, text='Team 5 Project', font=('Arial', 20), fg='blue')
biglabel.pack(side=TOP)

f1button = Button(frame2, text='Choose File 1', height=2, width=10, command=open_file1)
label_file_explorer = Label(frame3, text='')
entry = Entry(frame2, textvariable=File1Path, state=DISABLED, fg='black')
f1button.pack(side=LEFT, padx=10, pady=5)
entry.pack(fill=X, pady=20, padx=10)

f2button = Button(frame3, text='Choose File 2', height=2, width=10, command=open_file2)
label_file_explorer = Label(frame3, text='')
entry = Entry(frame3, textvariable=File2Path, state=DISABLED, fg='black')
f2button.pack(side=LEFT, padx=10, pady=5)
entry.pack(fill=X, pady=20, padx=10)

# Round Options to choose from
ExecuterEntry = Entry(frame4, text='0', width=20)
ExecuterEntryLabel = Label(frame4, text='Executer Name ', font=('Arial', 12))
ExecuterEntryLabel.pack(side=LEFT, pady=5, padx=10)
ExecuterEntry.pack(side=LEFT, padx=15, pady=10)

CommentEntryLabel = Label(frame5, text='Enter Comments', font=('Arial', 12))
CommentEntryLabel.pack(side=LEFT, padx=10)
CommentEntry = Entry(frame5, text='', width=20)
CommentEntry.pack(side=LEFT, padx=10, pady=10)

button = Button(frame6, text="Run", height=2, width=10, command=Run)
button.pack(side=BOTTOM, pady=30)

# Handles Popup once application is Finished
def finished():
    top = Toplevel(root)
    top.geometry("400x200")
    top.title("Success")
    top.geometry("+{}+{}".format(posRight + 100, posDown))
    Button(top, text='close', height=2, width=10, command=close).pack(side=BOTTOM, pady=10)
    Label(top, text="Finished!", font=('Arial', 12)).pack(side=TOP, pady=50)


# Function to  Close Application once finished
def close():
    root.destroy()


root.mainloop()
