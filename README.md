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

## Create Project UI
Created a User Interface to select files paths to be used in the program
User Interface is used to select the files and run the same python code as the Jupiter Notebook and load the file into SQL Database. 

# Additional Library Used  
 - 'pycong2'  
    Psycopg is the most popular PostgreSQL adapter for the Python programming language. Its core is a complete implementation of the Python DB API 2.0 specifications. Several extensions allow access to many of the features offered by PostgreSQL.

    using Version 2.9.9

    Documenation: https://www.psycopg.org/docs/   

    Psycopg is released under the terms of the GNU Lesser General Public License, allowing use from both free and proprietary software.

  - 'tkinter' the standard Python interface to the Tcl/Tk GUI toolkit.
    
    Documenation: https://docs.python.org/3/library/tkinter.html

# Ethical Considerations
This dataset contains the following personally identifiable information (PII) on the surveyed climbers: 
- home country
- sex
- height
- weight
- age<br>
<br>
While it is best practice to eliminate PII from publicly available datasets, removing all this data would result in missed opportunities for interesting analysis. Instead, the data was obscured by transforming ages into a 5-year age ranges. In this way, the privacy of the participants was respected without significantly sacrificing analysis. Remember, there is always the possibility that this dataset may be linked to other datasets to deduce identifying information of participants.<br><br>
*** Work in progress ***

