"""
Unit 4 - Lesson 1A Practice: Adding & Removing Lists
====================================================

Complete the functions below. Run this file to test your solutions!
All tests are provided - your job is to make them pass.
"""

# ==================== PROBLEM 1: CODE TRACING ====================

print("=" * 60)
print("PROBLEM 1: Code Tracing - insert() and extend()")
print("=" * 60)

print("""
Trace this code and predict the output:

    playlist = ["Song A", "Song C"]
    playlist.insert(1, "Song B")
    playlist.extend(["Song D", "Song E"])
    print(playlist)

Write your prediction below, then uncomment to check:
""")

# Your prediction:
# prediction = 

# Uncomment to check:
# playlist = ["Song A", "Song C"]
# playlist.insert(1, "Song B")
# playlist.extend(["Song D", "Song E"])
# print(f"Actual: {playlist}")
# print(f"Your prediction: {prediction}")

# ==================== PROBLEM 2: CODE TRACING ====================

print("\n" + "=" * 60)
print("PROBLEM 2: Code Tracing - remove() and pop()")
print("=" * 60)

print("""
Trace this code and predict the output:

    numbers = [10, 20, 30, 40, 50]
    numbers.remove(30)
    removed = numbers.pop(1)
    print(numbers)
    print(removed)

Write your predictions below, then uncomment to check:
""")

# Your predictions:
# numbers_prediction = 
# removed_prediction = 

# Uncomment to check:
# numbers = [10, 20, 30, 40, 50]
# numbers.remove(30)
# removed = numbers.pop(1)
# print(f"Actual numbers: {numbers}")
# print(f"Actual removed: {removed}")
# print(f"Your numbers prediction: {numbers_prediction}")
# print(f"Your removed prediction: {removed_prediction}")

# ==================== PROBLEM 3: CODE TRACING ====================

print("\n" + "=" * 60)
print("PROBLEM 3: Code Tracing - append() vs extend()")
print("=" * 60)

print("""
Trace these two similar codes and explain the difference:

Code A:
    list1 = [1, 2]
    list1.append([3, 4])
    print(list1)

Code B:
    list2 = [1, 2]
    list2.extend([3, 4])
    print(list2)

Write your predictions below, then uncomment to check:
""")

# Your predictions:
# list1_prediction = 
# list2_prediction = 

# Uncomment to check:
# list1 = [1, 2]
# list1.append([3, 4])
# list2 = [1, 2]
# list2.extend([3, 4])
# print(f"Code A result: {list1}")
# print(f"Code B result: {list2}")
# print(f"Your list1 prediction: {list1_prediction}")
# print(f"Your list2 prediction: {list2_prediction}")

# ==================== PROBLEM 4: CODE WRITING ====================

print("\n" + "=" * 60)
print("PROBLEM 4: Safe Remove Function")
print("=" * 60)

def safe_remove_all(playlist, song):
    """
    Remove ALL occurrences of a song from the playlist.
    
    Args:
        playlist: List of songs (will be modified)
        song: Song to remove (string)
    
    Returns:
        int: Number of times the song was removed
    
    Example:
        playlist = ["A", "B", "A", "C", "A"]
        count = safe_remove_all(playlist, "A")
        # playlist is now ["B", "C"]
        # count is 3
    """
    # TODO: Implement this function
    # Hint: Keep removing while the song is in the list
    # Count how many times you removed it
    pass


# ==================== PROBLEM 5: CODE WRITING ====================

print("\n" + "=" * 60)
print("PROBLEM 5: Insert Sorted")
print("=" * 60)

def insert_sorted(sorted_list, item):
    """
    Insert an item into an already sorted list, keeping it sorted.
    
    Args:
        sorted_list: List sorted in ascending order (will be modified)
        item: Item to insert (int or str)
    
    Example:
        numbers = [1, 3, 5, 7, 9]
        insert_sorted(numbers, 6)
        # numbers is now [1, 3, 5, 6, 7, 9]
    """
    # TODO: Implement this function
    # Hint: Find the correct position, then use insert()
    # Loop through and find where item should go
    pass


# ==================== TESTS ====================
