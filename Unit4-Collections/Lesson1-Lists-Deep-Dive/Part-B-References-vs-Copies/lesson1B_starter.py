"""
Unit 4 - Lesson 1B: References vs Copies
Practice Problems Starter File
"""
# ============================================================
# PROBLEM 3: Write safe_add() function
# ============================================================

def safe_add(original_list, item):
    """
    Create a new list with item added to the end.
    DO NOT modify the original list!
    
    Args:
        original_list: The list to add to (don't modify this!)
        item: The item to add
    
    Returns:
        A new list with item added to the end
    
    Example:
        nums = [1, 2, 3]
        result = safe_add(nums, 4)
        # nums is still [1, 2, 3]
        # result is [1, 2, 3, 4]
    """
    # TODO: Your code here
    new_list = original_list.copy() #original_list[:]
    new_list.append(item)
    return new_list


# ============================================================
# PROBLEM 4: Write are_same_list() function
# ============================================================

def are_same_list(list1, list2):
    """
    Return True if list1 and list2 point to the SAME list object.
    Return False if they are different list objects (even if contents match).
    
    Args:
        list1: First list
        list2: Second list
    
    Returns:
        True if they reference the same object, False otherwise
    
    Example:
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        
        are_same_list(a, b)  # True (same object)
        are_same_list(a, c)  # False (different objects)
    """
    # TODO: Your code here
    pass


# ============================================================
# PROBLEM 5: Write remove_duplicates() function (Challenge!)
# ============================================================

def remove_duplicates(original_list):
    """
    Return a new list with duplicates removed.
    DO NOT modify the original list!
    Order should be preserved (first occurrence kept).
    
    Args:
        original_list: The list to remove duplicates from (don't modify!)
    
    Returns:
        A new list with duplicates removed
    
    Example:
        nums = [1, 2, 2, 3, 1, 4, 3]
        result = remove_duplicates(nums)
        # nums is still [1, 2, 2, 3, 1, 4, 3]
        # result is [1, 2, 3, 4]
    """
    # TODO: Your code here
    pass


# ============================================================
# TESTS -
# ============================================================

def run_tests():
    """Run all tests and display results."""
    print("=" * 60)
    print("LESSON 1B PRACTICE - TEST RESULTS")
    print("=" * 60)
    
    total_tests = 0
    passed_tests = 0
    
    # Test Problem 3
    print("\n💻 PROBLEM 3: safe_add()")
    try:
        # Test 3.1: Basic functionality
        nums = [1, 2, 3]
        result = safe_add(nums, 4)
        if nums == [1, 2, 3] and result == [1, 2, 3, 4]:
            print("  ✅ PASS: Test 3.1 (basic add)")
            passed_tests += 1
        else:
            print(f"  ❌ FAIL: Test 3.1")
            print(f"     Original should be [1, 2, 3], got {nums}")
            print(f"     Result should be [1, 2, 3, 4], got {result}")
        total_tests += 1
        
        # Test 3.2: Empty list
        empty = []
        result = safe_add(empty, "first")
        if empty == [] and result == ["first"]:
            print("  ✅ PASS: Test 3.2 (empty list)")
            passed_tests += 1
        else:
            print(f"  ❌ FAIL: Test 3.2")
            print(f"     Original should be [], got {empty}")
            print(f"     Result should be ['first'], got {result}")
        total_tests += 1
        
        # Test 3.3: Independence check
        original = [1, 2]
        copy = safe_add(original, 3)
        copy.append(4)
        if original == [1, 2]:
            print("  ✅ PASS: Test 3.3 (lists are independent)")
            passed_tests += 1
        else:
            print(f"  ❌ FAIL: Test 3.3")
            print(f"     Original was modified! Should be [1, 2], got {original}")
        total_tests += 1
        
    except Exception as e:
        print(f"  ❌ ERROR: {e}")
        total_tests += 3

# ============================================================
# RUN THE TESTS
# ============================================================

if __name__ == "__main__":
    run_tests()
