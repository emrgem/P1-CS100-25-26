"""
Unit 7, Lesson 5: Python + SQLite
===================================
"""
import sqlite3
DB_FILE = "movies.db"

# ============================================================
# BASIC PATTERN: connect → cursor → execute → fetch
# SELECT 5 movies and print them
# ============================================================
print("=== Basic Pattern: 5 Movies ===")
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT title, genre, rating FROM movies LIMIT 5")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    print()


# ============================================================
# fetchone(): Get a single value
# How many total movies?
# ============================================================
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM movies")
    result = cursor.fetchone()
    print(f"Total Movies: {result[0]}")
    
# ============================================================
# fetchone(): Get a single value
# Look up one movie by id.
# ============================================================
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT title, genre, rating FROM movies WHERE id = 10")
    movie = cursor.fetchone()
    if movie:
        print(f"{movie[0]} ({movie[1]} - {movie[2]}/10)")
    else:
        print("Movie not found!")

# ============================================================
# PARAMETERIZED QUERIES: ? placeholders
# Search by genre using user input (safe!)
# ============================================================
genre = input("Enter a genre:")
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT title, rating FROM movies
                   WHERE genre = ?
                   ORDER BY rating DESC LIMIT 5
                   """, (genre,))
    rows = cursor.fetchall()
    print(f"\nTop 5 {genre} Movies:")
    for row in rows:
        print(f"    {row[0]} - {row[1]}/10")



