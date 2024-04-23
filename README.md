# Climbing Around the World

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
The goal of this project is to create an ETL data pipeline. Data will be extracted from .csv files, transformed using Python, and loaded into a postgreSQL database.

## Additional Python Libraries 
### psycopg2 
psycopg2 is the most popular PostgreSQL adapter for the Python programming language. Its core is a complete implementation of the Python DB API 2.0 specifications. Several extensions allow access to many of the features offered by PostgreSQL.<br>
Version required: 2.9.9<br>
Documentation: [https://www.psycopg.org/docs/]<br>
psycopg2 is released under the terms of the GNU Lesser General Public License, allowing use from both free and proprietary software.

### tkinter
tkinter is the standard Python interface to the Tcl/Tk GUI toolkit.<br>
Documentation: [https://docs.python.org/3/library/tkinter.html]

## Database Design
An SQL database was chosen based on the structure of the data. Each of the data tables is organized into columns and rows. Primary and foreign key relationships exist between the main data tables (climbers and routes) and the ID reference tables (clusters, countries, and grades).

## Entity Relationship Diagram
Refer to the relationship_diagram folder for the ERD and schema file.

## Using This Project
Download the contents of this repository into a local folder and follow the instructions below.

### ETL Process Flow
This program will create a local postgreSQL database on your machine loaded with the data from the .csv files in the data folder.
1. Launch UI_ETL.py using Python version 3.10.13 or later.
2. Select the paths for each of the 5 required .csv files.
3. Select the Run button and wait for the ETL process to execute.
4. Check the terminal for notes, warnings, and/or errors issued by the program.

### Crag Recommender
This program offers a simple user interface to recommend a crag based on user input.
1. Launch UI_crag_recommender.py using Python version 3.10.13 or later.
2. Input your climbing preferences. V, YDS, and French grading systems are accommodated.
3. Select the Run button. A specific crag and a list of routes meeting your requirements will be displayed, ordered by climber community rating.

### development Folder
This folder contains code snippets used during the development process. None are required for the execution of the final product. It is included for completeness and may be used to better understand the development strategy.

## Ethical Considerations
The climber dataset contains the following personally identifiable information (PII) on the surveyed climbers: 
- home country
- sex
- height
- weight
- age<br>
<br>
While it is best practice to eliminate PII from publicly available datasets, removing all this data would result in missed opportunities for interesting analysis. Instead, the data was obscured by transforming ages into a 5-year age ranges. In this way, the privacy of the participants was respected without significantly sacrificing analysis. Remember, there is always the possibility that this dataset may be linked to other datasets to deduce identifying information of participants.<br>
In terms of representation, a 64% majority of the surveyed climbers come from Europe. North American follows with 14% of the participants. The remaining continents of Africa, Asia, Australia, and South America each contribute to 5% or less of the surveyed climbers. Such a skew in representation indicates that the data will be less relevant and therefore less useful to those living outside of Europe. While suboptimal, this dataset is intended to be used only for recreational purposes and will not negatively impact the lives of those unaccounted for. <br>

## Sources
+ Data table source: [https://www.kaggle.com/datasets/jordizar/climb-dataset/data]
+ Country Codes ISO-3166-1: [https://en.wikipedia.org/wiki/ISO_3166-1]
+ Grade Conversions: [https://climbinghouse.com/grades-charts-conversion/]
