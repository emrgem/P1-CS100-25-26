#Unit 7, Lesson 2: CREATE & INSERT — Starter File
import sqlite3
DB_FILE = "my_movies.db"
# ============================================================
# STEP 1: CREATE TABLE
# This creates the movies table if it doesn't already exist.
# You DON'T need to change anything here — just read it.
# ============================================================
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS movies (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    rating REAL,
                    year INTEGER,
                    review TEXT  
                   )
                   """)


# ============================================================
# STEP 2: INSERT — Code-Along Movies (do these with teacher)
# Follow along as we add 3 movies together.
# ============================================================
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO movies (title, genre, rating, year, review)
        VALUES ('The Dark Knight', 'Action', 9.0, 2008, 'Batman vs Joker masterpiece')
    """)



# ============================================================
# STEP 3: YOUR TURN — Add 5 movies YOU like
# Replace the placeholders below with real movies.
#
# Rules:
#   - Pick movies you've actually seen
#   - Genres: Action, Comedy, Drama, Sci-Fi, Animation,
#             Horror, Thriller, Romance, Fantasy, Documentary
#   - Rating: 1.0 to 10.0
#   - Review: one short sentence
#
# Remember:
#   - Text values use SINGLE QUOTES: 'like this'
#   - Numbers have NO quotes: 8.5 not '8.5'
#   - Apostrophes in titles: use two single quotes: 'Schindler''s List'
# ============================================================
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()


    # Movie 4
    cursor.execute("""
        INSERT INTO movies (title, genre, rating, year, review)
        VALUES ('Spider-Man: Into the Spider-Verse', 'Animation', 8.4, 2018, 'Miles Morales becomes Spider-Man across dimensions')
    """)


    # Movie 5
    cursor.execute("""
        INSERT INTO movies (title, genre, rating, year, review)
        VALUES ('Inception', 'Sci-Fi', 8.8, 2010, 'A thief who enters dreams takes on one last impossible job')
    """)


    # Movie 6
    cursor.execute("""
        INSERT INTO movies (title, genre, rating, year, review)
        VALUES ('Knives Out', 'Comedy', 7.9, 2019, 'A detective investigates a wealthy family after a death')
    """)


    # Movie 7
    cursor.execute("""
        INSERT INTO movies (title, genre, rating, year, review)
        VALUES ('Whiplash', 'Drama', 8.5, 2014, 'A jazz drummer is pushed to his limits by a ruthless teacher')
    """)


    # Movie 8 — note the apostrophe handled with double single quotes
    cursor.execute("""
        INSERT INTO movies (title, genre, rating, year, review)
        VALUES ('Schindler''s List', 'Drama', 9.0, 1993, 'A businessman saves lives during the Holocaust')
    """)


    print("✅ 5 movies inserted")


# ============================================================
# STEP 4: VERIFY — See all your movies
# This SELECT shows everything in the table.
# ============================================================

