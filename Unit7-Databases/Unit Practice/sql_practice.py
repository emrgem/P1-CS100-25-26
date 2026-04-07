"""
Unit 7: SQL Practice — songs.db
================================
155 songs across 9 genres with streaming data.

Table: songs
Columns: id, title, artist, genre, streams_millions, year

Instructions:
1. Make sure songs.db is in the same folder
2. Write each query below the comment
3. Run the file to check your answers: python sql_practice.py
"""

import sqlite3

DB_FILE = "songs.db"

def run(sql):
    """Run a query and print results."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print(f"({len(rows)} rows)\n")


# ============================================================
# LEVEL 1: Basic SELECT
# ============================================================

# 1. Show all songs (every column)
run("SELECT * FROM songs")

# 2. Show just the title and artist for all songs

run("SELECT title, artist FROM songs")
# 3. How many total songs are in the database?

 
# ============================================================
# LEVEL 2: WHERE Filters
# ============================================================

# 4. All Pop songs


# 5. All songs with more than 2000 million streams


# 6. All songs released before 2000


# 7. All songs by Taylor Swift


# ============================================================
# LEVEL 3: AND / OR
# ============================================================

# 8. Pop songs with more than 2000 million streams


# 9. Songs by Drake OR Kendrick Lamar


# 10. Rock songs from the 1990s (year >= 1990 AND year <= 1999)


# ============================================================
# LEVEL 4: ORDER BY + LIMIT
# ============================================================

# 11. Top 10 most streamed songs (highest first)


# 12. 5 oldest songs in the database


# 13. Top 5 Hip-Hop songs by streams


# ============================================================
# LEVEL 5: LIKE (Text Search)
# ============================================================

# 14. All songs with "love" in the title


# 15. All artists that start with "The"


# 16. All songs with "baby" anywhere in the title (case doesn't matter)


# ============================================================
# LEVEL 6: Aggregates
# ============================================================

# 17. Average streams across all songs (rounded to 0 decimals)


# 18. The most streamed song (MAX)


# 19. The oldest year in the database (MIN)


# ============================================================
# LEVEL 7: GROUP BY
# ============================================================

# 20. How many songs in each genre? (sorted by count, highest first)


# 21. Average streams per genre (rounded, sorted highest first)


# 22. How many songs does each artist have? (only show artists with 3+ songs)
#     Hint: use HAVING COUNT(*) >= 3 after GROUP BY


# ============================================================
# LEVEL 8: Combine Everything
# ============================================================

# 23. Top 3 genres by total streams (SUM, not AVG)


# 24. For each decade (2000s, 2010s, 2020s), how many songs?
#     Hint: you can do math in GROUP BY:
#     GROUP BY (year / 10) * 10


# 25. Which artist has the highest single-song stream count?
#     Show the artist, title, and streams.




