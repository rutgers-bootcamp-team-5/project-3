import csv
import os
from tkinter import *
from datetime import datetime
from tkinter import filedialog


# initialize Tkinter which manages the GUI elements
root = Tk()
root.geometry("600x450")
root.title('Project 3')
# Gets the requested values of the height and width.
winWidth = root.winfo_reqwidth()
winHeight = root.winfo_reqheight()
posRight = int(root.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(root.winfo_screenheight() / 2 - winHeight / 2)
posRight = int(posRight / 2)

root.geometry("+{}+{}".format(posRight, posDown))



def Run():

    print(f1entry.get())
    print(ExecuterEntry.get())

    if  not f1entry.get():
        err = Toplevel(root)
        err.geometry("400x200")
        err.title("Failed")
        err.geometry("+{}+{}".format(posRight + 100, posDown))
        #Button(err, text='close', height=2, width=10, command=exitButton()).pack(side=BOTTOM, pady=10)
        Label(err, text="Failed, Select the file 1", font=('Arial', 12)).pack(side=TOP, pady=50)
        
    else:
        ETLProcess()



File1Path = StringVar()
File2Path = StringVar()
File3Path = StringVar()
File4Path = StringVar()


def open_file1():
    global fpath1
    file_path = filedialog.askopenfilename(initialdir = "C:\Data",
                                          title = "Select a File",
                                          filetypes = (("CSV files",
                                                        "*.csv*"),
                                                       ("All Files",
                                                        "*.*")))
    if file_path is not None:
        fpath1 = file_path
        File1Path.set(fpath1)
        return fpath1
    
def open_file2():
    global fpath2
    file_path = filedialog.askopenfilename(initialdir = "C:\Data",
                                          title = "Select a File",
                                          filetypes = (("CSV files",
                                                        "*.csv*"),
                                                       ("All Files",
                                                        "*.*")))
    if file_path is not None:
        fpath2 = file_path
        File2Path.set(fpath2)
        return fpath2
    
def open_file3():
    global fpath3
    file_path = filedialog.askopenfilename(initialdir = "C:\Data",
                                          title = "Select a File",
                                          filetypes = (("CSV files",
                                                        "*.csv*"),
                                                       ("All Files",
                                                        "*.*")))
    if file_path is not None:
        fpath3 = file_path
        File3Path.set(fpath3)
        return fpath3
    
def open_file4():
    global fpath4
    file_path = filedialog.askopenfilename(initialdir = "C:\Data",
                                          title = "Select a File",
                                          filetypes = (("CSV files",
                                                        "*.csv*"),
                                                       ("All Files",
                                                        "*.*")))
    if file_path is not None:
        fpath4 = file_path
        File4Path.set(fpath4)
        return fpath4

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
frame7 = Frame()
frame7.pack(fill=X)
frame8 = Frame()
frame8.pack(fill=X)

biglabel = Label(frame1, text='Team 5 Project', font=('Arial', 20), fg='blue')
biglabel.pack(side=TOP)

f1button = Button(frame2, text='Choose File 1', height=2, width=10, command=open_file1)
label_file_explorer = Label(frame2, text='')
f1entry = Entry(frame2, textvariable=File1Path, state=DISABLED, fg='black')
f1button.pack(side=LEFT, padx=10, pady=5)
f1entry.pack(fill=X, pady=20, padx=10)

f2button = Button(frame3, text='Choose File 2', height=2, width=10, command=open_file2)
label_file_explorer = Label(frame3, text='')
f2entry = Entry(frame3, textvariable=File2Path, state=DISABLED, fg='black')
f2button.pack(side=LEFT, padx=10, pady=5)
f2entry.pack(fill=X, pady=20, padx=10)

f3button = Button(frame4, text='Choose File 3', height=2, width=10, command=open_file3)
label_file_explorer = Label(frame4, text='')
f3entry = Entry(frame4, textvariable=File3Path, state=DISABLED, fg='black')
f3button.pack(side=LEFT, padx=10, pady=5)
f3entry.pack(fill=X, pady=20, padx=10)

f4button = Button(frame5, text='Choose File 4', height=2, width=10, command=open_file4)
label_file_explorer = Label(frame5, text='')
f4entry = Entry(frame5, textvariable=File4Path, state=DISABLED, fg='black')
f4button.pack(side=LEFT, padx=10, pady=5)
f4entry.pack(fill=X, pady=20, padx=10)

# Round Options to choose from
ExecuterEntry = Entry(frame6, text='0', width=20)
ExecuterEntryLabel = Label(frame6, text='Executer Name ', font=('Arial', 12))
ExecuterEntryLabel.pack(side=LEFT, pady=5, padx=10)
ExecuterEntry.pack(side=LEFT, padx=15, pady=10)

CommentEntryLabel = Label(frame7, text='Enter Comments', font=('Arial', 12))
CommentEntryLabel.pack(side=LEFT, padx=10)
CommentEntry = Entry(frame7, text='', width=20)
CommentEntry.pack(side=LEFT, padx=10, pady=10)

button = Button(frame8, text="Run", height=2, width=10, command=Run)
button.pack(side=BOTTOM, pady=30)

def ETLProcess():
    print(fpath1)
    finished()

# Handles Popup once application is Finished
def finished():
    top = Toplevel(root)
    top.geometry("400x200")
    top.title("Success")
    top.geometry("+{}+{}".format(posRight + 100, posDown))
    Button(top, text='close', height=2, width=10, command=close).pack(side=BOTTOM, pady=10)
    #Label(top, text="Finished!", font=('Arial', 12)).pack(side=TOP, pady=50)
    Label(top, text="Finished!", font=('Arial', 12)).pack(side=TOP, pady=50)


# Function to  Close Application once finished
def close():
    root.destroy()


root.mainloop()
