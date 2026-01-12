# unit4_lesson4_tuples_practice.py
"""
Unit 4 - Lesson 4: Tuples Practice
===================================
print("=" * 60)
print("UNIT 4 LESSON 4: TUPLES PRACTICE")
print("=" * 60)"""

# ============================================================
# PART 2: CODE WRITING
# ============================================================

print("\n" + "=" * 60)
print("PART 2: CODE WRITING")
print("=" * 60)


# ------------------------------------------------------------
# Exercise 1: Create and Unpack
# ------------------------------------------------------------
print("\n--- Exercise 1: Create and Unpack ---")

def create_rgb_color(red, green, blue):
    """
    Create an RGB color tuple and return formatted info.
    
    Args:
        red: Red value (0-255)
        green: Green value (0-255)
        blue: Blue value (0-255)
    
    Returns:
        tuple: (rgb_tuple, hex_string)
               - rgb_tuple is (red, green, blue)
               - hex_string is "#RRGGBB" format
    
    Example:
        create_rgb_color(88, 101, 242)
        Returns: ((88, 101, 242), "#5865f2")
    """
    # TODO: Create the RGB tuple
    rgb_tuple = (red, green, blue)
    # TODO: Create hex string using f-string formatting
    # Hint: Use :02x for 2-digit hex with lowercase letters
    hex_string = f"#{red:02x}{green:02x}{blue:02x}"
    # TODO: Return both as a tuple
    return rgb_tuple, hex_string

# Test Exercise 1
# Uncomment when ready to test:
result = create_rgb_color(88, 101, 242)
if result:
    rgb, hex_str = result
    print(f"RGB: {rgb}")
    print(f"Hex: {hex_str}")
    # Expected: RGB: (88, 101, 242), Hex: #5865f2


# ------------------------------------------------------------
# Exercise 2: Player Stats Function
# ------------------------------------------------------------
print("\n--- Exercise 2: Player Stats ---")

def calculate_player_stats(scores):
    """
    Calculate and return multiple stats for a player's scores.
    
    Args:
        scores: List of integer scores
    
    Returns:
        tuple: (total, average, best, worst)
               Returns (0, 0, 0, 0) if scores is empty
    
    Example:
        calculate_player_stats([100, 85, 92, 78, 95])
        Returns: (450, 90.0, 100, 78)
    """
    # TODO: Handle empty list case
    
    # TODO: Calculate total (sum of all scores)
    
    # TODO: Calculate average (total / count)
    
    # TODO: Find best (highest) score
    
    # TODO: Find worst (lowest) score
    
    # TODO: Return all four values as a tuple
    pass  # Remove this when you add your code


# Test Exercise 2
# Uncomment when ready to test:
# scores = [100, 85, 92, 78, 95]
# stats = calculate_player_stats(scores)
# if stats:
#     total, avg, best, worst = stats
#     print(f"Total: {total}")
#     print(f"Average: {avg}")
#     print(f"Best: {best}")
#     print(f"Worst: {worst}")
#     # Expected: Total: 450, Average: 90.0, Best: 100, Worst: 78
# 
# # Test empty list
# empty_stats = calculate_player_stats([])
# print(f"Empty: {empty_stats}")
# # Expected: (0, 0, 0, 0)


# ------------------------------------------------------------
# Exercise 3: Coordinate Grid
# ------------------------------------------------------------
print("\n--- Exercise 3: Coordinate Grid ---")

def create_game_grid():
    """
    Create a game grid using tuples as dictionary keys.
    
    Returns:
        dict: Grid with coordinate tuples as keys
              - (0, 0) -> "spawn"
              - (5, 5) -> "checkpoint"  
              - (10, 0) -> "treasure"
              - (10, 10) -> "boss"
    """
    # TODO: Create and return the grid dictionary
    # Use tuples (x, y) as keys
    pass  # Remove this when you add your code


def check_location(grid, x, y):
    """
    Check what's at a location in the grid.
    
    Args:
        grid: The game grid dictionary
        x: X coordinate
        y: Y coordinate
    
    Returns:
        str: What's at that location, or "empty" if nothing
    """
    # TODO: Create coordinate tuple from x and y
    
    # TODO: Use .get() to safely check the grid
    # Return "empty" if coordinate not found
    pass  # Remove this when you add your code


# Test Exercise 3
# Uncomment when ready to test:
# grid = create_game_grid()
# if grid:
#     print(f"At (0, 0): {check_location(grid, 0, 0)}")      # spawn
#     print(f"At (10, 10): {check_location(grid, 10, 10)}")  # boss
#     print(f"At (3, 3): {check_location(grid, 3, 3)}")      # empty


# ------------------------------------------------------------
# Exercise 4: Song Metadata Processor
# ------------------------------------------------------------
print("\n--- Exercise 4: Song Metadata ---")

def process_song(song_dict):
    """
    Process a song dictionary that contains a metadata tuple.
    
    Args:
        song_dict: Dictionary with keys:
                   - "title": str
                   - "artist": str  
                   - "metadata": tuple of (year, duration_seconds, bpm)
    
    Returns:
        tuple: (formatted_string, duration_string)
               - formatted_string: "Title by Artist (Year)"
               - duration_string: "M:SS" format
    
    Example:
        song = {
            "title": "Blinding Lights",
            "artist": "The Weeknd",
            "metadata": (2020, 200, 171)
        }
        process_song(song)
        Returns: ("Blinding Lights by The Weeknd (2020)", "3:20")
    """
    # TODO: Extract title and artist from dict
    
    # TODO: Unpack the metadata tuple into year, duration, bpm
    
    # TODO: Create formatted string: "Title by Artist (Year)"
    
    # TODO: Convert duration to "M:SS" format
    # Hint: minutes = duration // 60, seconds = duration % 60
    # Use f"{seconds:02d}" for zero-padded seconds
    
    # TODO: Return both strings as a tuple
    pass  # Remove this when you add your code


# Test Exercise 4
# Uncomment when ready to test:
# song = {
#     "title": "Blinding Lights",
#     "artist": "The Weeknd",
#     "metadata": (2020, 200, 171)
# }
# result = process_song(song)
# if result:
#     info, duration = result
#     print(f"Info: {info}")
#     print(f"Duration: {duration}")
#     # Expected: "Blinding Lights by The Weeknd (2020)", "3:20"


# ------------------------------------------------------------
# Exercise 5: Playlist Analyzer
# ------------------------------------------------------------
print("\n--- Exercise 5: Playlist Analyzer ---")

def analyze_playlist(songs):
    """
    Analyze a playlist of songs with metadata tuples.
    
    Args:
        songs: List of song dictionaries, each with:
               - "title": str
               - "artist": str
               - "metadata": (year, duration_seconds, bpm)
    
    Returns:
        tuple: (total_duration, avg_bpm, oldest_year, newest_year)
               Returns (0, 0, 0, 0) if playlist is empty
    
    Example:
        songs = [
            {"title": "Song A", "artist": "Artist 1", "metadata": (2020, 180, 120)},
            {"title": "Song B", "artist": "Artist 2", "metadata": (2019, 200, 140)},
        ]
        analyze_playlist(songs)
        Returns: (380, 130.0, 2019, 2020)
    """
    # TODO: Handle empty playlist
    
    # TODO: Initialize counters for total_duration, total_bpm
    
    # TODO: Track oldest and newest years
    # Hint: Start oldest at a large number, newest at 0
    
    # TODO: Loop through songs and unpack each metadata tuple
    
    # TODO: Calculate average BPM
    
    # TODO: Return all four values
    pass  # Remove this when you add your code


# Test Exercise 5
# Uncomment when ready to test:
# playlist = [
#     {"title": "Blinding Lights", "artist": "The Weeknd", "metadata": (2020, 200, 171)},
#     {"title": "Bad Guy", "artist": "Billie Eilish", "metadata": (2019, 194, 135)},
#     {"title": "Levitating", "artist": "Dua Lipa", "metadata": (2020, 203, 103)},
# ]
# 
# stats = analyze_playlist(playlist)
# if stats:
#     total, avg_bpm, oldest, newest = stats
#     print(f"Total Duration: {total}s ({total // 60}m {total % 60}s)")
#     print(f"Average BPM: {avg_bpm:.1f}")
#     print(f"Year Range: {oldest} - {newest}")
#     # Expected: Total: 597s, Avg BPM: 136.3, Years: 2019 - 2020

