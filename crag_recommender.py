import pandas as pd
import psycopg2
import user_credentials

def main(country, grade_lower, grade_upper, style):
    country = country.title()
    style = style.title()

    # Choose desired grading scale
    try:
        if '.' in grade_lower:
            selected_scale = 'grade_yds'
        elif 'v' in grade_lower.lower():
            selected_scale = 'grade_v'
        else:
            selected_scale = 'grade_fra'
    except TypeError:
        pass    # Handle bad grade error

    # Connect to the climbing_db database
    database_name = "climbing_db"
    try:
        conn = psycopg2.connect(database = database_name, user = user_credentials.username, password = user_credentials.password, 
                                host = "localhost", port = "5432")
        cursor = conn.cursor()
    except psycopg2.errors.OperationalError:
        print("Database connection not successful")

    # Query data
    cursor.execute(f'''
    SELECT c.country, r.crag, r.sector, r.name, r.grade_mean, r.rating_tot, r.style, g.{selected_scale}
    FROM countries AS c
    JOIN routes AS r ON c.country_id = r.country
    JOIN grades AS g on r.grade_mean = g.grade_id
    WHERE c.country = '{country}'
    ''')
    data = cursor.fetchall()

    # Extract the data into a dataframe
    df = pd.DataFrame(data, columns=['country', 'crag', 'sector', 'route name', 'grade_mean', 'rating', 'style', 'grade'])

    cursor.close()
    conn.close()

    # Filter for style
    filtered_df = df[df['style'] == style]

    # Filter for grade range
    min_grade = filtered_df[filtered_df['grade'] == grade_lower]['grade_mean'].min()
    max_grade = filtered_df[filtered_df['grade'] == grade_upper]['grade_mean'].max()
    filtered_df = filtered_df[(filtered_df['grade_mean'] >= min_grade) & (filtered_df['grade_mean'] <= max_grade)]

    # Keep crags with at least 5 routes
    filtered_df = filtered_df.groupby('crag').filter(lambda x: len(x) > 4)

    # Select the crag containing routes with the greatest average rating
    best_crag = filtered_df.groupby('crag')['rating'].mean().sort_values(ascending=False).index[0]
    filtered_df = filtered_df[filtered_df['crag'] == best_crag].sort_values('rating', ascending=False)

    # Collect outputs
    output_columns = ['sector', 'route name', 'grade', 'rating']
    return (best_crag, [tuple(output_columns)] + list(filtered_df[output_columns].itertuples(index=False, name=None)))
