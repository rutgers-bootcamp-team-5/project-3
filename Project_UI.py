import csv
import os
from tkinter import *
from datetime import datetime
from tkinter import filedialog
import pandas as pd
import psycopg2
import psycopg2.sql as sql

from pathlib import Path
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, text

# initialize Tkinter which manages the GUI elements
root = Tk()
root.geometry("800x500")
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
    #print(ExecuterEntry.get())

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
File5Path = StringVar()


def open_file1():
    global fpath1
    file_path = filedialog.askopenfilename(initialdir = os.getcwd,
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
    file_path = filedialog.askopenfilename(initialdir = os.getcwd,
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
    file_path = filedialog.askopenfilename(initialdir = os.getcwd,
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
    file_path = filedialog.askopenfilename(initialdir = os.getcwd,
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
    file_path = filedialog.askopenfilename(initialdir = os.getcwd,
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

biglabel = Label(frame1, text='Team 5', font=('Calibri', 20), fg='blue')
biglabel.pack(side=TOP)

f1button = Button(frame2, text='Choose routes_rated', height=2, width=20, command=open_file1)
label_file_explorer = Label(frame2, text='')
f1entry = Entry(frame2, textvariable=File1Path, state=DISABLED, fg='black')
f1button.pack(side=LEFT, padx=10, pady=5)
f1entry.pack(fill=X, pady=20, padx=10)

f2button = Button(frame3, text='Choose climber_df', height=2, width=20, command=open_file2)
label_file_explorer = Label(frame3, text='')
f2entry = Entry(frame3, textvariable=File2Path, state=DISABLED, fg='black')
f2button.pack(side=LEFT, padx=10, pady=5)
f2entry.pack(fill=X, pady=20, padx=10)

f3button = Button(frame4, text='Choose clusters', height=2, width=20, command=open_file3)
label_file_explorer = Label(frame4, text='')
f3entry = Entry(frame4, textvariable=File3Path, state=DISABLED, fg='black')
f3button.pack(side=LEFT, padx=10, pady=5)
f3entry.pack(fill=X, pady=20, padx=10)

f4button = Button(frame5, text='Choose country_codes', height=2, width=20, command=open_file4)
label_file_explorer = Label(frame5, text='')
f4entry = Entry(frame5, textvariable=File4Path, state=DISABLED, fg='black')
f4button.pack(side=LEFT, padx=10, pady=5)
f4entry.pack(fill=X, pady=20, padx=10)

f5button = Button(frame6, text='Choose grades_conversion', height=2, width=20, command=open_file5)
label_file_explorer = Label(frame5, text='')
f5entry = Entry(frame6, textvariable=File5Path, state=DISABLED, fg='black')
f5button.pack(side=LEFT, padx=10, pady=5)
f5entry.pack(fill=X, pady=20, padx=10)

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

#import routesratedcsv
def RoutesRated():
    routes_df = pd.read_csv(fpath1)
    climber_df = pd.read_csv(fpath2)
    # clusters_df = pd.read_csv(fpath3)
    # country_df = pd.read_csv(fpath4)
    # grades_df = pd.read_csv(fpath5)
    # Format case of text columns
    routes_df['country'] = routes_df['country'].str.upper()
    routes_df['crag'] = routes_df['crag'].str.title()
    routes_df['sector'] = routes_df['sector'].str.title()
    routes_df['name'] = routes_df['name'].str.title()

    # Create a new column called "style" which indicates if the route is preferred by short or tall climbers
    def style(x):
        if x < 0:
            return 'Short'
        elif x > 0:
            return 'Tall'
        else:
            return 'Neutral'

    routes_df['style'] = routes_df['tall_recommend_sum'].apply(style)
    
    # Clean up the dataframe by removing unnecessary columns
    routes_df = routes_df.drop('tall_recommend_sum', axis = 1)
    
    # Change grade_mean column from float to int
    routes_df['grade_mean'] = routes_df['grade_mean'].astype(int)

    #Replace sex column values where 0 = Male and 1 = Female for climber_df sheet
    df = pd.DataFrame(climber_df)
    df["sex"].replace([0,1], ["M","F"], inplace= True)

    #Changing age column to have values for age range for data anonymization for climber_df sheet
    #define age range function
    def AGE(x):
        if x <=10:
            return "0 - 10"
        if x<=20 and x>10:
            return "11 - 20"
        if x<=30 and x>20:
            return "21 - 30"
        if x<=40 and x>30:
            return "31 - 40"
        if x<=50 and x> 40:
            return "41 - 50"
        if x<=60 and x>50:
            return "51 - 60"
        if x<=70 and x>60:
            return "61-70"
        return "Above 70"
    df['age'] = df['age'].apply(AGE)
    # routes_df['style'] = routes_df['tall_recommend_sum'].apply(style)
    # routes_df.head()

    #rename column height and weight to represent unit for climber_df sheet
    df = df.rename(columns={'height': 'height_cm', 'weight': 'weight_kg', 'age': 'age_range'})

    #change datatype of column
    #placeholderdf['test'] = placeholderdf['test'].astype(desired_data_type)
    df['date_first'] = pd.to_datetime(df['date_first'])
    df['date_last'] = pd.to_datetime(df['date_last'])


    # Connect to postgres and create a database
    try:
        conn = psycopg2.connect("user=postgres password = 'admin'")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        database_name = "climber_db"
    # Create table statement
        sqlCreateDatabase = "CREATE DATABASE "+database_name+";"
    # Create a table in PostgreSQL database
        cursor.execute(sqlCreateDatabase)
    except: 
        print('Database already exists')
    
    # Set connection to new created database using psycopg2
    try:
        conn = psycopg2.connect(database = "climber_db", user = "postgres", password = "admin", host = "localhost", port = "5432")
    except:
        print("Database connection not successful") 

    # Create a table using psycopg2 connection
    cursor = conn.cursor()
    table_creation = '''
    CREATE TABLE IF NOT EXISTS route_ratings (
        name_id INT PRIMARY KEY,
        country VARCHAR(3),
        crag TEXT NOT NULL,
        sector TEXT NOT NULL,
        name TEXT NOT NULL,
        grade_mean INT,
        cluster INT,
        rating_tot FLOAT,
        style TEXT NOT NULL
    );
    '''
    cursor.execute(table_creation)
    conn.commit()

    # Insert dataframe into database table
    engine = create_engine('postgresql://postgres:admin@localhost:5432/climber_db')
    routes_df.to_sql('route_ratings', engine, if_exists='append', index = False)

    cursor = conn.cursor()
    table_creation = '''
    CREATE TABLE IF NOT EXISTS climber_data(
        user_id VARCHAR(255),
        country VARCHAR (255) NOT NULL,
        sex TEXT,
        height_cm INT,
        weight_kg INT,
        age_range VARCHAR(255),
        years_cl INT,
        date_first VARCHAR (255),
        date_last VARCHAR(255),
        grades_count INT,
        grades_first INT,
        grades_last INT,
        grades_max INT,
        grades_mean VARCHAR(255),
        Year_first INT,
        year_last INT)
    '''
    cursor.execute(table_creation)
    conn.commit()

    #Insert climber_data into database table
    engine = create_engine('postgresql://postgres:admin@localhost:5432/climber_db')
    df.to_sql('climber_data', engine, if_exists='append', index = False)

    # close connection and cursor
    cursor.close()
    conn.close()

def ETLProcess():
    #print(fpath1)
    RoutesRated()
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
