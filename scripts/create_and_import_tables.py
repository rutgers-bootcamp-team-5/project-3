import pandas as pd
import psycopg2
import user_credentials # user_credentials.py must be created locally. Initialize variables for 
                        # username and password in this file with your postgres credentials.

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, exc

def main(routes_csv, countries_csv, grades_csv, clusters_csv, climbers_csv):
    error_report = []
    
    # Read routes data into dataframe
    routes_df = pd.read_csv(routes_csv)
    routes_df.rename(columns={'name_id' : 'route_id'}, inplace=True)

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
    routes_df = routes_df.drop('tall_recommend_sum', axis=1)

    # Change grade_mean column from float to int to allow for grade conversions.
    routes_df['grade_mean'] = routes_df['grade_mean'].astype(int)

    # Connect to postgres and create a database
    database_name = 'climbing_db'
    try:
        conn = psycopg2.connect(f'user={user_credentials.username} password={user_credentials.password}')
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        cursor.execute(f'CREATE DATABASE {database_name};')
    except psycopg2.errors.DuplicateDatabase: 
        error_report.append(f'NOTE: {database_name} database already exists.')
    finally:
        cursor.close()
        conn.close()

    # Set connection to new created database using psycopg2
    host = 'localhost'
    port = '5432'
    try:
        conn = psycopg2.connect(
            database=database_name, user=user_credentials.username, password=user_credentials.password, host =host, port=port)
    except psycopg2.errors.OperationalError:
        error_report.append(f'ERROR: Connection to {database_name} failed.')
        return error_report

    #Read country_codes.csv into dataframe
    countries_df = pd.read_csv(countries_csv)
    #Read grades_conversions.csv into dataframe
    grades_df = pd.read_csv(grades_csv)
    #Read clusters.csv into dataframe
    clusters_df = pd.read_csv(clusters_csv)

    # Create countries table using psycopg2 connection
    countries_table = 'countries'
    cursor = conn.cursor()
    table_creation = f'''
    CREATE TABLE IF NOT EXISTS {countries_table} (
        country_id VARCHAR(5) PRIMARY KEY,
        country VARCHAR(100)
    );
    '''
    cursor.execute(table_creation)
    conn.commit()

    # Insert dataframe into database table
    try:
        engine = create_engine(f'postgresql://{user_credentials.username}:{user_credentials.password}@{host}:{port}/{database_name}')
        countries_df.to_sql(countries_table, engine, if_exists='append', index = False)
    except exc.IntegrityError:
        error_report.append(f'WARNING: Attempted to insert a duplicate key into {countries_table} table. ' +
                            f'Check whether your data is already present in {database_name}.')

    # Create clusters table using psycopg2 connection
    clusters_table = 'clusters'
    cursor = conn.cursor()
    table_creation = f'''
    CREATE TABLE IF NOT EXISTS {clusters_table} (
        cluster_id INT PRIMARY KEY,
        description VARCHAR(100)
    );
    '''
    cursor.execute(table_creation)
    conn.commit()

    # Insert dataframe into database table
    try:
        engine = create_engine(f'postgresql://{user_credentials.username}:{user_credentials.password}@{host}:{port}/{database_name}')
        clusters_df.to_sql(clusters_table, engine, if_exists='append', index = False)
    except exc.IntegrityError:
        error_report.append(f'WARNING: Attempted to insert a duplicate key into {clusters_table} table. ' +
                            f'Check whether your data is already present in {database_name}.')

    # Create grades table using psycopg2 connection
    grades_table = 'grades'
    cursor = conn.cursor()
    table_creation = f'''
    CREATE TABLE IF NOT EXISTS {grades_table} (
        grade_id INT PRIMARY KEY,
        grade_fra VARCHAR(7),
        grade_yds VARCHAR(5),
        grade_v VARCHAR(3)
    );
    '''
    cursor.execute(table_creation)
    conn.commit()

    # Insert dataframe into database table
    try:
        engine = create_engine(f'postgresql://{user_credentials.username}:{user_credentials.password}@{host}:{port}/{database_name}')
        grades_df.to_sql(grades_table, engine, if_exists='append', index = False)
    except exc.IntegrityError:
        error_report.append(f'WARNING: Attempted to insert a duplicate key into {grades_table} table. ' + 
                            f'Check whether your data is already present in {database_name}.')

    # Create a table using psycopg2 connection
    routes_table = 'routes'
    cursor = conn.cursor()
    table_creation = f'''
    CREATE TABLE IF NOT EXISTS {routes_table} (
        route_id INT PRIMARY KEY,
        country VARCHAR(5),
        crag VARCHAR(50) NOT NULL,
        sector VARCHAR(50) NOT NULL,
        name VARCHAR(100) NOT NULL,
        grade_mean INT,
        cluster INT,
        rating_tot FLOAT,
        style VARCHAR(7) NOT NULL,
        FOREIGN KEY(country) REFERENCES countries(country_id),
        FOREIGN KEY(grade_mean) REFERENCES grades(grade_id),
        FOREIGN KEY(cluster) REFERENCES clusters(cluster_id)
    );
    '''
    cursor.execute(table_creation)
    conn.commit()

    # Insert dataframe into database table
    try:
        engine = create_engine(f'postgresql://{user_credentials.username}:{user_credentials.password}@{host}:{port}/{database_name}')
        routes_df.to_sql(routes_table, engine, if_exists='append', index = False)
    except exc.IntegrityError:
        error_report.append(f'WARNING: Attempted to insert a duplicate key into {routes_table} table. ' + 
                            f'Check whether your data is already present in {database_name}.')

    # Read climber data in dataframe
    climber_df = pd.read_csv(climbers_csv)

    # Replace sex column values where 0 = Male and 1 = Female
    climber_df['sex'].replace([0, 1], ['M', 'F'], inplace=True)

    # Convert ages to age ranges to anonymize age data
    max_age = int(climber_df['age'].max())
    age_bins = [x for x in range(0, max_age + 5, 5)]
    age_labels = [f'{i+1}-{j}' for i, j in zip(age_bins[:-1], age_bins[1:])]
    climber_df['age'] = pd.cut(climber_df['age'], bins=age_bins, labels=age_labels)

    # Rename columns for clarity 
    climber_df.rename(columns={'height': 'height_cm', 'weight': 'weight_kg', 'age': 'age_range'}, inplace=True)

    # change datatype of column
    climber_df['date_first'] = pd.to_datetime(climber_df['date_first'])
    climber_df['date_last'] = pd.to_datetime(climber_df['date_last'])

    #Convert grades_mean from float to int
    climber_df['grades_mean'] = climber_df['grades_mean'].astype(int)

    # Create a table using psycopg2 connection
    climbers_table = 'climbers'
    cursor = conn.cursor()
    table_creation = f'''
    CREATE TABLE IF NOT EXISTS {climbers_table}(
        user_id INT PRIMARY KEY,
        country VARCHAR (5) NOT NULL,
        sex CHAR(1) NOT NULL,
        height_cm INT,
        weight_kg INT,
        age_range VARCHAR(5) NOT NULL,
        years_cl INT,
        date_first TIMESTAMP,
        date_last TIMESTAMP,
        grades_count INT,
        grades_first INT,
        grades_last INT,
        grades_max INT,
        grades_mean INT,
        year_first INT,
        year_last INT,
        FOREIGN KEY(country) REFERENCES countries(country_id),
        FOREIGN KEY (grades_first) REFERENCES grades(grade_id),
        FOREIGN KEY (grades_last) REFERENCES grades(grade_id),
        FOREIGN KEY (grades_max) REFERENCES grades(grade_id),
        FOREIGN KEY (grades_mean) REFERENCES grades(grade_id)
        );
    '''
    cursor.execute(table_creation)
    conn.commit()

    # Insert dataframe into database table
    try:
        engine = create_engine(f'postgresql://{user_credentials.username}:{user_credentials.password}@{host}:{port}/{database_name}')
        climber_df.to_sql(climbers_table, engine, if_exists='append', index = False)
    except exc.IntegrityError:
        error_report.append(f'WARNING: Attempted to insert a duplicate key into {climbers_table} table. ' +
                            f'Check whether your data is already present in {database_name}.')

    cursor.close()
    conn.close()

    return error_report
