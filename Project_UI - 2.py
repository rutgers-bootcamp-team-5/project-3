import csv
import os
from tkinter import *
from datetime import datetime
from tkinter import filedialog


# initialize Tkinter which manages the GUI elements
root = Tk()
root.geometry("600x350")
root.title('Project 3')
# Gets the requested values of the height and width.
winWidth = root.winfo_reqwidth()
winHeight = root.winfo_reqheight()
posRight = int(root.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(root.winfo_screenheight() / 2 - winHeight / 2)
posRight = int(posRight / 2)

root.geometry("+{}+{}".format(posRight, posDown))

EnteredText = StringVar()
EnteredText = ""

def Run():

    EnteredText = ""

    #print(f1entry.get())
    print(CountryEntry.get())
    print(GradeUpperEntry.get())
    print(GradeLowerEntry.get())
    print(TallEntry.get())

    if  not CountryEntry.get():
        EnteredText = "Country Name" + ","
    
    if  not GradeUpperEntry.get():
        EnteredText = EnteredText + " Grade Range (Upper bound)" + ","

    if  not GradeLowerEntry.get():
        EnteredText = EnteredText + " Grade Range (Lower bound)" + ","

    if  not TallEntry.get():
        EnteredText = EnteredText + " Tall\Short"
    

    if  EnteredText:
        EnteredText = "Enter "  + EnteredText
        err = Toplevel(root)
        err.geometry("800x200")
        err.title("Failed")
        err.geometry("+{}+{}".format(posRight + 100, posDown))
        #Button(err, text='close', height=2, width=10, command=err.close()).pack(side=BOTTOM, pady=10)
        Label(err, text=EnteredText + " to proceed !", font=('Arial', 12)).pack(side=TOP, pady=50)
    else:
        ETLProcess()

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

biglabel = Label(frame1, text='Team 5 Project', font=('Arial', 20), fg='blue')
biglabel.pack(side=TOP)

# Round Options to choose from
CountryEntry = Entry(frame1, text='0', width=20)
CountryEntryLabel = Label(frame1, text='Enter Country Name :                          ', font=('Arial', 12))
CountryEntryLabel.pack(side=LEFT, pady=5, padx=10)
CountryEntry.pack(side=LEFT, padx=15, pady=10)

GradeUpperEntryLabel = Label(frame2, text='Enter Grade Range (Upper bound) :  ', font=('Arial', 12))
GradeUpperEntryLabel.pack(side=LEFT, padx=10)
GradeUpperEntry = Entry(frame2, text='', width=20)
GradeUpperEntry.pack(side=LEFT, padx=10, pady=10)

GradeLowerEntryLabel = Label(frame3, text='Enter Grade Range (Lower bound) :  ', font=('Arial', 12))
GradeLowerEntryLabel.pack(side=LEFT, padx=10)
GradeLowerEntry = Entry(frame3, text='', width=20)
GradeLowerEntry.pack(side=LEFT, padx=10, pady=10)

TallEntryLabel = Label(frame4, text='Enter Tall\Short :                                   ', font=('Arial', 12))
TallEntryLabel.pack(side=LEFT, padx=10)
TallEntry = Entry(frame4, text='', width=20)
TallEntry.pack(side=LEFT, padx=10, pady=10)

button = Button(frame5, text="Run", height=2, width=10, command=Run)
button.pack(side=BOTTOM, pady=30)

def ETLProcess():
    #print(fpath1)
    finished()

# Handles Popup once application is Finished
def finished():
    SelectedText = StringVar()
    SelectedText = "Entered text : " +  CountryEntry.get() + "," + GradeUpperEntry.get() + "," + GradeLowerEntry.get() + "," + TallEntry.get()

    print(SelectedText)

    top = Toplevel(root)
    top.geometry("400x200")
    top.title("Success")
    top.geometry("+{}+{}".format(posRight + 100, posDown))
    Button(top, text='close', height=2, width=10, command=close).pack(side=BOTTOM, pady=10)
    #Label(top, text="Finished!", font=('Arial', 12)).pack(side=TOP, pady=50)
    Label(top, text=SelectedText, font=('Arial', 12)).pack(side=TOP, pady=50)


# Function to  Close Application once finished
def close():
    root.destroy()


root.mainloop()
