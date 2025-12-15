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
    return list1 is list2

if __name__ == "__main__":
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    print(are_same_list(a, b))  # True - same object
    print(are_same_list(a, c))  # False - different objects
    print(a == c)               # True - same contents
    print(a is c)               # False - different objects