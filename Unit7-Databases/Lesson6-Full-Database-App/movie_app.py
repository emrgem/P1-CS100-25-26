"""
Unit 7, Lesson 6: Full Database App
=====================================
Build a complete menu-driven CRUD app with SQLite.
"""
import sqlite3
DB_FILE = "my_app.db"

# ============================================================
# init_db() — Create the table if it doesn't exist
# ============================================================
def init_db():
    """Create the movies table if it does not exist."""
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS movies (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           title TEXT NOT NULL,
                           genre TEXT NOT NULL,
                           rating REAL,
                           review TEXT
                       )
                       """)


# ============================================================
# display_movies() — Format and print a list of movie tuples
# Reusable helper for view_all and search
# ============================================================



# ============================================================
# add_movie() — Get input from user, INSERT into database
# ============================================================
def add_movie():
    """Get movie info from the user and save to the database"""
    title = input("Title:" )
    genre = input("Genre:" )
    rating = float(input("Rating(1-10):" ))
    review = input("Short Review:" )
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
                        INSERT INTO movies(title, genre, rating, review)
                        VALUES (?, ?, ?, ?)""", (title,genre,rating,review))

    print(f"✅Added '{title}'")
    # ============================================================
    # view_all_movies() — SELECT all, display formatted
    # ============================================================



# ============================================================
# search_movies() — Search by title keyword with LIKE
# ============================================================



# ============================================================
# update_rating() — Show all, pick an ID, UPDATE rating
# ============================================================



# ============================================================
# delete_movie() — Show all, pick an ID, DELETE row
# ============================================================



# ============================================================
# view_stats() — COUNT, AVG, GROUP BY genre
# ============================================================



# ============================================================
# main() — Menu loop that ties everything together
# ============================================================
def main():
    init_db()
    while True:
        print("\n🎬 Movie Database")
        print("1. Add Movie")
        print("2. View all movies")
        print("3. Search movies")
        print("4. Update a rating")
        print("5. Delete a movie")
        # print("6. View stats")
        print("7. Quit")
        choice = input("\nChoice: ")
        
        if choice == "1":
            add_movie()

# ============================================================
# Run the app
# ============================================================

if __name__ == "__main__":
    main()
