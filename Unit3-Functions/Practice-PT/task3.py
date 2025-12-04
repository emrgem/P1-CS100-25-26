"""
=============================================================================
UNIT 3 PRACTICE - Task 3: Playlist Statistics
=============================================================================
Concepts: *args, multiple return values, tuple unpacking, handling empty input

INSTRUCTIONS:
1. Complete the function below where it says # TODO
2. Run this file to test your solution
3. All 4 tests should pass before moving to Task 4
=============================================================================
"""

def playlist_stats(*durations):
    """
    Calculate statistics for a playlist of songs.
    
    Accepts any number of song durations and returns the total time,
    number of songs, and average duration. If no durations are provided,
    returns zeros to avoid division errors.
    
    Args:
        *durations: Any number of song durations in seconds (integers)
    
    Returns:
        tuple: A tuple of (total_time, song_count, average_duration)
               - total_time: sum of all durations (int)
               - song_count: number of songs (int)
               - average_duration: average length (float)
    
    Examples:
        >>> playlist_stats(180, 210, 240, 195)
        (825, 4, 206.25)
        
        >>> playlist_stats(300, 300)
        (600, 2, 300.0)
        
        >>> playlist_stats()
        (0, 0, 0.0)
    """
    # TODO: Write your code here (replace 'pass')
    # Hint 1: Check if durations is empty FIRST (if not durations:)
    # Hint 2: Use sum() and len() for calculations
    # Hint 3: Return three values separated by commas
    pass


# =============================================================================
# TEST CODE - Run this file to test your solution
# =============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("🎵 TASK 3: playlist_stats")
    print("=" * 50)
    
    # Test 1: Multiple durations
    result = playlist_stats(180, 210, 240, 195)
    expected = (825, 4, 206.25)
    if result == expected:
        print("✅ Test 1 PASSED: playlist_stats(180, 210, 240, 195)")
    else:
        print(f"❌ Test 1 FAILED: Expected {expected}, got {result}")
    
    # Test 2: Two durations
    result = playlist_stats(300, 300)
    expected = (600, 2, 300.0)
    if result == expected:
        print("✅ Test 2 PASSED: playlist_stats(300, 300)")
    else:
        print(f"❌ Test 2 FAILED: Expected {expected}, got {result}")
    
    # Test 3: Single duration
    result = playlist_stats(240)
    expected = (240, 1, 240.0)
    if result == expected:
        print("✅ Test 3 PASSED: playlist_stats(240)")
    else:
        print(f"❌ Test 3 FAILED: Expected {expected}, got {result}")
    
    # Test 4: Empty (no durations) - should NOT crash!
    result = playlist_stats()
    expected = (0, 0, 0.0)
    if result == expected:
        print("✅ Test 4 PASSED: playlist_stats() handles empty")
    else:
        print(f"❌ Test 4 FAILED: Expected {expected}, got {result}")
    
    print("=" * 50)
    
    # Bonus: Show how to unpack the results (only if function works)
    print("\n📝 Example of tuple unpacking:")
    print("   total, count, avg = playlist_stats(180, 200, 220)")
    print("   # This gives you three separate variables!")
