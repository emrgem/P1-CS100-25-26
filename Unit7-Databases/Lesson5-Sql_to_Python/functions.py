import sqlite3
DB_FILE = "movies.db"
# ============================================================
# FUNCTION: add_movie(title, genre, rating, review)
# INSERT with ? placeholders
# ============================================================
def add_movie(title, genre, rating, review):
    """Insert a new movie into the database"""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO movies (title, genre, rating, review)
                       VALUES (?, ?, ?, ?)""",(title, genre, rating, review))
        
    print(f"✅ Added '{title}'")

# ============================================================
# FUNCTION: get_all_movies()
# SELECT all, return fetchall()
# ============================================================
def get_all_movies():
    """Get all movies sorted by rating (highest first).
    """
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT id, title, genre, rating FROM movies
                       ORDER BY rating DESC 
                       """)
        return cursor.fetchall() # list of tuples
    

# ============================================================
# FUNCTION: search_movies(keyword)
# SELECT with LIKE ? — build the pattern in Python
# ============================================================
def search_movies(keyword):
    """Search movies by title keyword"""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT id, title, genre, rating FROM movies
                       WHERE title LIKE ?""", (f"%{keyword}%",))
        return cursor.fetchall()        



# ============================================================
# YOUR TURN: Write these two functions
#
# FUNCTION: update_rating(movie_id, new_rating)
#   - UPDATE rating WHERE id = ?
#   - Print confirmation with rowcount
#
# FUNCTION: delete_movie(movie_id)
#   - DELETE FROM movies WHERE id = ?
#   - Print confirmation with rowcount
# ============================================================




# ============================================================
# TEST YOUR FUNCTIONS
# Call each function to verify it works
# ============================================================
if __name__ == "__main__":
    # add_movie("My Test Movie", "Comedy", 7.5, "Just a test!")
    
    # movies = get_all_movies()
    # print(f"\n🎞️All Movies ({len(movies)} total:) ")
    # # for m in movies: # all movies
    # for m in movies[:10]:
    #     print(f"    [{m[0]}] {m[1]} ({m[2]}) - {m[3]}/10") 
        
    results = search_movies("spider")
    print(f"\nSearch Results:")
    for m in results:
        print(f"    [{m[0]}] {m[1]} ({m[2]}) - {m[3]}/10")      
    pass
