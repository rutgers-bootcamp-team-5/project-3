# project-3

Rutgers Data Science Boot Camp 2023 - 2024
Project 3 

Track: Data Engineering

## Contributors

Leonid Lyakhovich<br>
Matthew Mosca<br>
Vibhuti Patel<br>
Balamurugen Sathiyanaaraayanan<br>
Phil Tsao

## Project Overview
The goal of this project is to create an ETL data pipeline that will consume data in the .csv format and create a postgreSQL database.

## Sources
https://www.kaggle.com/datasets/jordizar/climb-dataset/data

## Data Tables
Main:
 + Routes Rateds
 + Climer DF
 + Cluster

Supplemental:
 + Country Codes ISO-3166-1 [https://en.wikipedia.org/wiki/ISO_3166-1]
 + Grade Conversions [https://climbinghouse.com/grades-charts-conversion/]
  

# Process Flow - Of Jupiter Notebook
1. Use of a user interface to get the date paths of CSV files to be read into a Pandas Dataframe using Jupiter Notebook.

2. Transform - Using Jupiter Notebook 
  Routes Rated
    a. Change column names for storage
    b. Change 'crag', 'sector' and 'name' columns to be title case
    c. Change the Country Abbrivation to be all upper case
    d. Add a column called 'style' where it is transformed based on 'tall_sum_recommendation' value that is then dropped. 
        - if less than Zero : 'Short Person'
        - if greater than Zero: 'Tall Person"
        - if zero : 'Neutral'
    e. Clean up the grades by changing the data type from string to float

  Climers DF
    a. Read the Climer DF csv into a Pandas DataFrame
    b. Check Datatype for each column, check if there are any null values
    c. Change the sex column values where 0 = Male and 1 = Female
    d. Changing age column to have values for age range for data anonymization
    e. rename column height and weight to represent unit 
    f. change date to a date format

3. Load - Loading into a New postgreSQL data base
   a. Load both data sets from Jupiter Notebook to postgreSQL via Psycopg2   
   b. For each table Confirm that the load was successfull by querying getting all the data and printing it out.

## Create Project UI - Load Data
Created a User Interface to select files paths to be used in the program
User Interface is used to select the files and run the same python code as the Jupiter Notebook and load the file into SQL Database. 

## Create Project UI - Access Data
Create a User Intercase to recomend a route based to user input.
 - The program accesses the database of routes, filters it based on user input and then displays the top scoring route based to the filters.
 - If can not find an route then display a message. 

# Additional Library Used  
 - 'pycong2'  
    Psycopg is the most popular PostgreSQL adapter for the Python programming language. Its core is a complete implementation of the Python DB API 2.0 specifications. Several extensions allow access to many of the features offered by PostgreSQL.

    using Version 2.9.9

    Documenation: https://www.psycopg.org/docs/   

    Psycopg is released under the terms of the GNU Lesser General Public License, allowing use from both free and proprietary software.

  - 'tkinter' the standard Python interface to the Tcl/Tk GUI toolkit.
    
    Documenation: https://docs.python.org/3/library/tkinter.html

# Ethical Considerations
This dataset contains the following personally identifiable information on the surveyed climbers: home country, sex, height, weight, and age. Removing this data would significantly reduce the utility of the dataset. Consider that the dataset does not contain names, personal identification numbers, or specific directory information, pieces of data that increase the probability of identifying an individual. However, there is always the possibility of there being so few options that a the identity can be narrowed down to a few possible options. To avoid that, this dataset was transformer to have an age range and a height range instead of conreate values.<br><br>
*** Work in progress ***

