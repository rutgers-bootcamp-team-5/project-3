from os import getcwd
from scripts import create_and_import_tables
from tkinter import *
from tkinter import filedialog

# initialize Tkinter which manages the GUI elements
root = Tk()
root.geometry("800x500")
root.title('Project 3 - Team 5')
# Gets the requested values of the height and width.
winWidth = root.winfo_reqwidth()
winHeight = root.winfo_reqheight()
posRight = int(root.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(root.winfo_screenheight() / 2 - winHeight / 2)
posRight = int(posRight / 2)

root.geometry("+{}+{}".format(posRight, posDown))

SelectedFiles = StringVar()
SelectedFiles = ""

def Run():

    print(routes_entry.get())
    #print(ExecuterEntry.get())

    SelectedFiles = ""

    if  not routes_entry.get():
        SelectedFiles = " routes_rated" + ","
    
    if  not climbers_entry.get():
        SelectedFiles = SelectedFiles + " climber_df" + ","

    if  not clusters_entry.get():
        SelectedFiles = SelectedFiles + " clusters" + ","

    if  not countries_entry.get():
        SelectedFiles = SelectedFiles + " country_codes"

    if  not grades_entry.get():
        SelectedFiles = SelectedFiles + " grades_conversion"

    if  SelectedFiles:
        SelectedFiles = "Choose the files "  + SelectedFiles
        err = Toplevel(root)
        err.geometry("800x200")
        err.title("Failed")
        err.geometry("+{}+{}".format(posRight + 100, posDown))
        #Button(err, text='close', height=2, width=10, command=err.close()).pack(side=BOTTOM, pady=10)
        Label(err, text=SelectedFiles + " to proceed !", font=('Arial', 12)).pack(side=TOP, pady=50)
    else:
        ETLProcess()



File1Path = StringVar()
File2Path = StringVar()
File3Path = StringVar()
File4Path = StringVar()
File5Path = StringVar()


def open_file1():
    global fpath1
    file_path = filedialog.askopenfilename(initialdir = getcwd,
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
    file_path = filedialog.askopenfilename(initialdir = getcwd,
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
    file_path = filedialog.askopenfilename(initialdir = getcwd,
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
    file_path = filedialog.askopenfilename(initialdir = getcwd,
                                          title = "Select a File",
                                          filetypes = (("CSV files",
                                                        "*.csv*"),
                                                       ("All Files",
                                                        "*.*")))
    if file_path is not None:
        fpath4 = file_path
        File4Path.set(fpath4)
        return fpath4

def open_file5():
    global fpath5
    file_path = filedialog.askopenfilename(initialdir = getcwd,
                                          title = "Select a File",
                                          filetypes = (("CSV files",
                                                        "*.csv*"),
                                                       ("All Files",
                                                        "*.*")))
    if file_path is not None:
        fpath5 = file_path
        File5Path.set(fpath5)
        return fpath5


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
frame9 = Frame()
frame9.pack(fill=X)

biglabel = Label(frame1, text='ETL Process UI', font=('Calibri', 20), fg='blue')
biglabel.pack(side=TOP)

routes_button = Button(frame2, text='Choose routes_rated', height=2, width=20, command=open_file1)
label_file_explorer = Label(frame2, text='')
routes_entry = Entry(frame2, textvariable=File1Path, state=DISABLED, fg='black')
routes_button.pack(side=LEFT, padx=10, pady=5)
routes_entry.pack(fill=X, pady=20, padx=10)

climbers_button = Button(frame3, text='Choose climber_df', height=2, width=20, command=open_file2)
label_file_explorer = Label(frame3, text='')
climbers_entry = Entry(frame3, textvariable=File2Path, state=DISABLED, fg='black')
climbers_button.pack(side=LEFT, padx=10, pady=5)
climbers_entry.pack(fill=X, pady=20, padx=10)

clusters_button = Button(frame4, text='Choose clusters', height=2, width=20, command=open_file3)
label_file_explorer = Label(frame4, text='')
clusters_entry = Entry(frame4, textvariable=File3Path, state=DISABLED, fg='black')
clusters_button.pack(side=LEFT, padx=10, pady=5)
clusters_entry.pack(fill=X, pady=20, padx=10)

countries_button = Button(frame5, text='Choose country_codes', height=2, width=20, command=open_file4)
label_file_explorer = Label(frame5, text='')
countries_entry = Entry(frame5, textvariable=File4Path, state=DISABLED, fg='black')
countries_button.pack(side=LEFT, padx=10, pady=5)
countries_entry.pack(fill=X, pady=20, padx=10)

grades_button = Button(frame6, text='Choose grades_conversion', height=2, width=20, command=open_file5)
label_file_explorer = Label(frame5, text='')
grades_entry = Entry(frame6, textvariable=File5Path, state=DISABLED, fg='black')
grades_button.pack(side=LEFT, padx=10, pady=5)
grades_entry.pack(fill=X, pady=20, padx=10)

# Round Options to choose from
# ExecuterEntry = Entry(frame7, text='0', width=20)
# ExecuterEntryLabel = Label(frame7, text='Executer Name ', font=('Arial', 12))
# ExecuterEntryLabel.pack(side=LEFT, pady=5, padx=10)
# ExecuterEntry.pack(side=LEFT, padx=15, pady=10)

# CommentEntryLabel = Label(frame8, text='Enter Comments', font=('Arial', 12))
# CommentEntryLabel.pack(side=LEFT, padx=10)
# CommentEntry = Entry(frame8, text='', width=20)
# CommentEntry.pack(side=LEFT, padx=10, pady=10)

button = Button(frame9, text="Run", height=4, width=20, command=Run)
button.pack(side=BOTTOM, pady=30)

def ETLProcess():
    #print(fpath1)
    error_report = create_and_import_tables.main(
        routes_entry.get(), countries_entry.get(), grades_entry.get(), clusters_entry.get(), climbers_entry.get())
    for e in error_report:
        print(e)
    finished()



# Handles Popup once application is Finished
def finished():
    top = Toplevel(root)
    top.geometry("400x200")
    top.title("Success")
    top.geometry("+{}+{}".format(posRight + 100, posDown))
    Button(top, text='close', height=2, width=10, command=close).pack(side=BOTTOM, pady=10)
    #Label(top, text="Finished!", font=('Arial', 12)).pack(side=TOP, pady=50)
    Label(top, text="Successfully completed ETL process !!!", font=('Arial', 12)).pack(side=TOP, pady=50)


# Function to  Close Application once finished
def close():
    root.destroy()


root.mainloop()
