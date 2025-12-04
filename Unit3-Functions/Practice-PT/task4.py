"""
=============================================================================
UNIT 3 PRACTICE - Task 4: Build Custom Playlist
=============================================================================
Concepts: **kwargs, try/except, dictionary building, summing values

INSTRUCTIONS:
1. Complete the function below where it says # TODO
2. Run this file to test your solution
3. All 4 tests should pass to complete the practice!
=============================================================================
"""

def build_playlist(playlist_name, **songs):
    """
    Build a custom playlist from keyword arguments.
    
    Creates a playlist dictionary with the playlist name, a dictionary
    of songs with their play counts, and the total number of plays.
    Uses try/except to safely calculate the total.
    
    Args:
        playlist_name: The name of the playlist (required, string)
        **songs: Any number of song=play_count pairs
                 Example: song1=5, song2=10
    
    Returns:
        dict: A dictionary with keys:
              - "name": the playlist name
              - "songs": dictionary of {song: play_count}
              - "total_plays": sum of all play counts
    
    Examples:
        >>> build_playlist("Road Trip", song1=5, song2=10, song3=3)
        {"name": "Road Trip", "songs": {"song1": 5, "song2": 10, "song3": 3}, "total_plays": 18}
        
        >>> build_playlist("Chill Vibes", relaxing=20, ambient=15)
        {"name": "Chill Vibes", "songs": {"relaxing": 20, "ambient": 15}, "total_plays": 35}
        
        >>> build_playlist("Empty Playlist")
        {"name": "Empty Playlist", "songs": {}, "total_plays": 0}
    """
    # TODO: Write your code here (replace 'pass')
    # Hint 1: **songs is already a dictionary!
    # Hint 2: Use sum(songs.values()) to get total plays
    # Hint 3: Wrap the sum in try/except in case of bad values
    # Hint 4: Return a dictionary with "name", "songs", and "total_plays"
    pass


# =============================================================================
# TEST CODE - Run this file to test your solution
# =============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("🎵 TASK 4: build_playlist")
    print("=" * 50)
    
    # Test 1: Multiple songs
    result = build_playlist("Road Trip", song1=5, song2=10, song3=3)
    expected = {"name": "Road Trip", "songs": {"song1": 5, "song2": 10, "song3": 3}, "total_plays": 18}
    if result == expected:
        print("✅ Test 1 PASSED: build_playlist with multiple songs")
    else:
        print(f"❌ Test 1 FAILED:")
        print(f"   Expected: {expected}")
        print(f"   Got:      {result}")
    
    # Test 2: Different song names
    result = build_playlist("Chill Vibes", relaxing=20, ambient=15)
    expected = {"name": "Chill Vibes", "songs": {"relaxing": 20, "ambient": 15}, "total_plays": 35}
    if result == expected:
        print("✅ Test 2 PASSED: build_playlist('Chill Vibes', relaxing=20, ambient=15)")
    else:
        print(f"❌ Test 2 FAILED:")
        print(f"   Expected: {expected}")
        print(f"   Got:      {result}")
    
    # Test 3: Empty playlist (no songs)
    result = build_playlist("Empty Playlist")
    expected = {"name": "Empty Playlist", "songs": {}, "total_plays": 0}
    if result == expected:
        print("✅ Test 3 PASSED: build_playlist('Empty Playlist') handles empty")
    else:
        print(f"❌ Test 3 FAILED:")
        print(f"   Expected: {expected}")
        print(f"   Got:      {result}")
    
    # Test 4: Single song
    result = build_playlist("One Hit Wonder", hit_song=100)
    expected = {"name": "One Hit Wonder", "songs": {"hit_song": 100}, "total_plays": 100}
    if result == expected:
        print("✅ Test 4 PASSED: build_playlist('One Hit Wonder', hit_song=100)")
    else:
        print(f"❌ Test 4 FAILED:")
        print(f"   Expected: {expected}")
        print(f"   Got:      {result}")
    
    print("=" * 50)
    
    # Bonus: Show what **kwargs looks like inside the function
    print("\n📝 What **songs becomes inside the function:")
    print("   build_playlist('Test', a=1, b=2, c=3)")
    print("   → songs = {'a': 1, 'b': 2, 'c': 3}")
    print("   → songs.values() = dict_values([1, 2, 3])")
    print("   → sum(songs.values()) = 6")
