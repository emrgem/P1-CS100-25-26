"""Unit 7, Lesson 3: SELECT & WHERE"""
import sqlite3
DB_FILE = "movies.db"

# ============================================================
# HELPER: Run a query and print results
# Write this first — we'll use it for every query.
# ============================================================
def run_query(db, sql):
    """Run a query and print results."""
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print(f"({len(rows)} rows)\n")

# ============================================================
# QUERY 1: SELECT all movies
# ============================================================
run_query(DB_FILE, "SELECT * FROM movies")


# ============================================================
# QUERY 2-4: WHERE — Filter by genre, rating, year
# ============================================================
# title  rating of Action Movies
run_query(DB_FILE, "SELECT title, rating FROM movies WHERE genre = 'Action'")

# title genre rating of movies rating > 9
run_query(DB_FILE, "SELECT title, genre, rating FROM movies WHERE rating > 9")

# ============================================================
# QUERY 5-7: AND / OR — Combine conditions
# ============================================================
# Action movies rated above 8
run_query(DB_FILE,"""
          SELECT title, rating FROM movies
          WHERE genre = 'Action' AND rating > 8
          """)

#All movies Action or Sci-Fi
run_query(DB_FILE,"""
          SELECT * FROM movies
          WHERE genre = 'Action' OR genre = 'Sci-Fi'
          """)

# ============================================================
# QUERY 8-10: ORDER BY + LIMIT — Sort and cap results
# ============================================================
# top 5 highest rated movies
run_query(DB_FILE, """
          SELECT title, genre, rating FROM movies
          ORDER BY rating DESC LIMIT 5
          """)

# 10 newest movies
run_query(DB_FILE, """
          SELECT title, year, genre FROM movies
          ORDER BY year DESC LIMIT 10
          """)
# 10 newest movies, sorted by year by desc, then genre by asc
run_query(DB_FILE, """
          SELECT title, year, genre FROM movies
          ORDER BY year DESC, genre ASC LIMIT 10
          """)

# Top 5 Action Movies (title, rating)
run_query(DB_FILE, """
          SELECT title, rating FROM movies
          WHERE genre = 'Action'
          ORDER BY rating DESC LIMIT 5
          """)

# ============================================================
# QUERY 11-13: LIKE — Text search
# ============================================================
# Search movies that contains spider
run_query(DB_FILE, """
          SELECT title, year FROM movies
          WHERE title LIKE '%spider%'
          """)

# Title starts with "The" - First 10 movies, sorted by title
run_query(DB_FILE, """
            SELECT title, year FROM movies
            WHERE title LIKE 'The%'
            ORDER BY title LIMIT 10
          """)

# Genres containing 'i'
# DISTINCT removes the duplicates
run_query(DB_FILE, """
            SELECT DISTINCT genre FROM movies
            WHERE genre LIKE '%i%'
          """)
# ============================================================
# QUERY 14-17: Aggregates — COUNT, AVG, GROUP BY
# ============================================================
# Total Movies
run_query(DB_FILE, """
            SELECT COUNT(*) FROM movies
          """)
# Average Rating
run_query(DB_FILE, """
            SELECT ROUND(AVG(rating),1) FROM movies
          """)

# Movies per Genre
run_query(DB_FILE, """
            SELECT genre, COUNT(*) as total
            FROM movies
            GROUP BY genre
            ORDER BY total DESC
          """)

# Average rating by Genre
run_query(DB_FILE, """
            SELECT genre, ROUND(AVG(rating),1) as avg_rating
            FROM movies
            GROUP BY genre ORDER BY avg_rating DESC
          """)

# ============================================================
# QUERY 18: The "Impossible with CSV" query
# Top 3 genres by average rating with count
# ============================================================

run_query(DB_FILE, """
            SELECT genre, ROUND(AVG(rating),1) as avg_rating, COUNT(*) as total
            FROM movies
            GROUP BY genre
            ORDER BY avg_rating DESC
            LIMIT 3
          """)


# ============================================================
# CHALLENGES: Try these on your own!
#
# 1. All Horror movies rated above 7, sorted by rating (highest first)
# 2. The 5 oldest movies in the database
# 3. How many movies were made after 2020?
# 4. All movies with "love" in the title
# 5. Which genre has the most movies?
# ============================================================


