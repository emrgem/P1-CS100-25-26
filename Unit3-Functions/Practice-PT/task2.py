"""
=============================================================================
UNIT 3 PRACTICE - Task 2: Create Song Entry
=============================================================================
Concepts: Default parameters, keyword arguments, dictionaries

INSTRUCTIONS:
1. Complete the function below where it says # TODO
2. Run this file to test your solution
3. All 4 tests should pass before moving to Task 3
=============================================================================
"""

def create_song(title, artist="Unknown Artist", duration=180):
    """
    Create a song entry dictionary.
    
    Takes song information and returns it as a dictionary. The artist
    and duration have default values that are used if not specified.
    
    Args:
        title: The song title (required, string)
        artist: The artist name (default "Unknown Artist", string)
        duration: Song length in seconds (default 180, int)
    
    Returns:
        dict: A dictionary with keys "title", "artist", and "duration"
    
    Examples:
        >>> create_song("Imagine")
        {"title": "Imagine", "artist": "Unknown Artist", "duration": 180}
        
        >>> create_song("Yesterday", artist="The Beatles")
        {"title": "Yesterday", "artist": "The Beatles", "duration": 180}
        
        >>> create_song("Bohemian Rhapsody", artist="Queen", duration=354)
        {"title": "Bohemian Rhapsody", "artist": "Queen", "duration": 354}
    """
    # TODO: Write your code here (replace 'pass')
    # Hint: Create a dictionary with the three keys and return it
    pass


# =============================================================================
# TEST CODE - Run this file to test your solution
# =============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("🎵 TASK 2: create_song")
    print("=" * 50)
    
    # Test 1: Title only (should use both defaults)
    result = create_song("Imagine")
    expected = {"title": "Imagine", "artist": "Unknown Artist", "duration": 180}
    if result == expected:
        print("✅ Test 1 PASSED: create_song('Imagine') uses defaults")
    else:
        print(f"❌ Test 1 FAILED: Expected {expected}")
        print(f"   Got: {result}")
    
    # Test 2: Override artist with keyword argument
    result = create_song("Yesterday", artist="The Beatles")
    expected = {"title": "Yesterday", "artist": "The Beatles", "duration": 180}
    if result == expected:
        print("✅ Test 2 PASSED: create_song('Yesterday', artist='The Beatles')")
    else:
        print(f"❌ Test 2 FAILED: Expected {expected}")
        print(f"   Got: {result}")
    
    # Test 3: Override duration with keyword argument
    result = create_song("Long Song", duration=600)
    expected = {"title": "Long Song", "artist": "Unknown Artist", "duration": 600}
    if result == expected:
        print("✅ Test 3 PASSED: create_song('Long Song', duration=600)")
    else:
        print(f"❌ Test 3 FAILED: Expected {expected}")
        print(f"   Got: {result}")
    
    # Test 4: Override both with keyword arguments
    result = create_song("Bohemian Rhapsody", artist="Queen", duration=354)
    expected = {"title": "Bohemian Rhapsody", "artist": "Queen", "duration": 354}
    if result == expected:
        print("✅ Test 4 PASSED: create_song with all keyword args")
    else:
        print(f"❌ Test 4 FAILED: Expected {expected}")
        print(f"   Got: {result}")
    
    print("=" * 50)
