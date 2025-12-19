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
    if not original_list:
        return "List is empty!"
    new_list = []
    for item in original_list:
        if item not in new_list:
            new_list.append(item)
    return new_list


if __name__ == "__main__":
    # Test 1: Given Example
    nums = [1,2,2,3,1,4,3]
    print(f"Original:{nums}")
    print(f"Removed_Duplicates:{remove_duplicates(nums)}")
    
    # Test 2: Empty List
    nums = []
    print(f"Original:{nums}")
    print(f"Removed_Duplicates:{remove_duplicates(nums)}")
    
    # Test 3: No Duplicates
    nums = [1,2,3]
    print(f"Original:{nums}")
    print(f"Removed_Duplicates:{remove_duplicates(nums)}")
    
    # Test 4: All Duplicates
    nums = [1,1,1]
    print(f"Original:{nums}")
    print(f"Removed_Duplicates:{remove_duplicates(nums)}")