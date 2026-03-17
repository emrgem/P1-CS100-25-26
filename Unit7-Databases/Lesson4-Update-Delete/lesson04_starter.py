"""
Unit 7, Lesson 4: UPDATE & DELETE
==================================
Learn to change and remove data in your database.

Instructions:
1. Follow along as we write each section together
2. Run this file after each step: python lesson04.py
3. We work on a COPY of movies.db so we can safely break things
"""

import sqlite3
import shutil

# Make a fresh copy every time we run (safe to experiment!)
shutil.copy("movies.db", "movies_practice.db")
DB_FILE = "movies_practice.db"


# ============================================================
# HELPER: Run a query and print results
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
# UPDATE: Change one column
# Change The Dark Knight's rating to 9.5
# Show before and after
# ============================================================
print("====Before Update=====")
run_query(DB_FILE, "SELECT title, rating FROM movies WHERE title = 'The Dark Knight'")
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("""
                   UPDATE movies SET rating = 9.5 WHERE title = 'The Dark Knight'
                   """)


print("====After Update=====")
run_query(DB_FILE, "SELECT title, rating FROM movies WHERE title = 'The Dark Knight'")


# ============================================================
# UPDATE: Change multiple columns at once
# Change The Matrix's genre and rating
# ============================================================
run_query(DB_FILE, "SELECT title, genre, rating FROM movies WHERE title = 'The Matrix'")
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("""
                   UPDATE movies
                   SET genre = 'Sci-Fi Action', rating = 9.0
                   WHERE title = 'The Matrix' 
                   """)
run_query(DB_FILE, "SELECT title, genre, rating FROM movies WHERE title = 'The Matrix'")


# ============================================================
# THE GOLDEN RULE: UPDATE without WHERE
# ⚠️ Watch what happens when you forget WHERE
# (comment this out after running once!)
# ============================================================
# with sqlite3.connect(DB_FILE) as conn:
#     cursor = conn.cursor()
#     cursor.execute("""
#                    UPDATE movies SET rating = 0
#                    """)
#     print(f"Rows Affected: {cursor.rowcount}")
# run_query(DB_FILE, "SELECT title, rating FROM movies LIMIT 10")

# ============================================================
# DELETE: Remove a row by title
# Delete a movie, check the count before and after
# ============================================================
print("=== Before Delete ===")
run_query(DB_FILE, "SELECT COUNT(*) FROM movies")

with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE title = 'Pinocchio'")
    print(f"🗑 Deleted ({cursor.rowcount} row)\n")

print("=== After Delete ===")
run_query(DB_FILE, "SELECT COUNT(*) FROM movies")



# ============================================================
# DELETE: Remove rows by condition
# Delete all movies rated below 5.5
# ============================================================
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE rating < 7")
    print(f"🗑 Deleted ({cursor.rowcount} low rated movies)\n")

run_query(DB_FILE, "SELECT COUNT(*) FROM movies")


# Make a fresh copy every time we run (safe to experiment!)
shutil.copy("movies.db", "movies_practice.db")
DB_FILE = "movies_practice.db"

# ============================================================
# DELETE by ID: The safest way
# Find a movie's id first, then delete by id
# ============================================================
with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE rating < 7")
    print(f"🗑 Deleted ({cursor.rowcount} low rated movies)\n")



# ============================================================
# CHALLENGES: Try these on your own!
#
# 1. Change the genre of "Jaws" from "Horror" to "Thriller"
# 2. Give all Animation movies a rating boost of +0.2
# 3. Delete all movies from before 1970
# 4. Find all movies with a NULL review, then delete them
# 5. How many movies are left? (SELECT COUNT)
# ============================================================


