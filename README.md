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

# Process Flow
1. Extract - Read the data in a CSV file into a Pandas Dataframe using Jupiter Notebook.

2. Transform - Using Jupiter Notebook
    a. Change column names for storage
    b. Change 'crag', 'sector' and 'name' columns to be title case
    c. Change the Country Abbrivation to be all upper case
    d. Add a column called 'style' where it is transformed based on 'tall_sum_recommendation' value that is then dropped. 
        - if less than Zero : 'Short Person'
        - if greater than Zero: 'Tall Person"
        - if zero : 'Neutral'
    e. Clean up the grades by changing the data type from string to float

3. Load - Loading into a New postgreSQL data base
   a. Load data from Jupiter Notebook to postgreSQL via Psycopg2   
   b. Confirm that the load was successfull by querying getting all the data and printing it out.

# Additional Library Used  
 - 'pycong2'  
    Psycopg is the most popular PostgreSQL adapter for the Python programming language. Its core is a complete implementation of the Python DB API 2.0 specifications. Several extensions allow access to many of the features offered by PostgreSQL.

    using Version 2.9.9

    Documenation: https://www.psycopg.org/docs/   

    Psycopg is released under the terms of the GNU Lesser General Public License, allowing use from both free and proprietary software.

# Ethical Considerations


