import csv
import mysql.connector

# Database connection details
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "password"
DB_NAME = "cinescope"

# CSV file
CSV_FILE = "movies.csv"

def create_connection(db=None):
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=db
    )

def create_database():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    conn.commit()
    cursor.close()
    conn.close()

def create_table():
    conn = create_connection(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        year INT,
        genre VARCHAR(255),
        rating FLOAT,
        director VARCHAR(255),
        star1 VARCHAR(255),
        star2 VARCHAR(255),
        star3 VARCHAR(255)
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()

def import_csv():
    conn = create_connection(DB_NAME)
    cursor = conn.cursor()

    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute("""
                INSERT INTO movies 
                (title, year, genre, rating, director, star1, star2, star3)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                row["Series_Title"],
                int(row["Released_Year"]) if row["Released_Year"].isdigit() else None,
                row["Genre"],
                float(row["IMDB_Rating"]) if row["IMDB_Rating"] else None,
                row["Director"],
                row["Star1"],
                row["Star2"],
                row["Star3"]
            ))


    conn.commit()
    cursor.close()
    conn.close()
    print("Data imported successfully!")

if __name__ == "__main__":
    create_database()
    create_table()
    import_csv()
