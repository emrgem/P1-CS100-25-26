"""
=============================================================================
UNIT 3 PRACTICE - Task 1: Calculate Remaining Time
=============================================================================
Concepts: Basic function, parameters, return, conditional logic

INSTRUCTIONS:
1. Complete the function below where it says # TODO
2. Run this file to test your solution
3. All 4 tests should pass before moving to Task 2
=============================================================================
"""

def calculate_remaining(total_seconds, played_seconds):
    """
    Calculate remaining play time for a song.
    
    Takes the total length of a song and how much has been played,
    then returns how many seconds are left. If the played time is
    greater than the total, return 0 (not a negative number).
    
    Args:
        total_seconds: Total length of the song in seconds (int)
        played_seconds: How many seconds have been played (int)
    
    Returns:
        int: Remaining seconds, minimum of 0
    
    Examples:
        >>> calculate_remaining(180, 60)
        120
        >>> calculate_remaining(200, 250)
        0
        >>> calculate_remaining(300, 300)
        0
    """
    # TODO: Write your code here (replace 'pass')
    # Hint: Calculate total - played, but don't return negative numbers
    remaining = total_seconds - played_seconds
    if remaining < 0:
        return 0
    return remaining


# =============================================================================
# TEST CODE - Run this file to test your solution
# =============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("🎵 TASK 1: calculate_remaining")
    print("=" * 50) 
    
    # Test 1: Normal remaining time
    result = calculate_remaining(180, 60)
    if result == 120:
        print("✅ Test 1 PASSED: calculate_remaining(180, 60) = 120")
    else:
        print(f"❌ Test 1 FAILED: Expected 120, got {result}")
    
    # Test 2: Song finished (equal values)
    result = calculate_remaining(200, 200)
    if result == 0:
        print("✅ Test 2 PASSED: calculate_remaining(200, 200) = 0")
    else:
        print(f"❌ Test 2 FAILED: Expected 0, got {result}")
    
    # Test 3: Played more than total (should return 0, not negative)
    result = calculate_remaining(150, 200)
    if result == 0:
        print("✅ Test 3 PASSED: calculate_remaining(150, 200) = 0 (not -50)")
    else:
        print(f"❌ Test 3 FAILED: Expected 0, got {result}")
    
    # Test 4: Nothing played yet
    result = calculate_remaining(300, 0)
    if result == 300:
        print("✅ Test 4 PASSED: calculate_remaining(300, 0) = 300")
    else:
        print(f"❌ Test 4 FAILED: Expected 300, got {result}")
    
    print("=" * 50)
