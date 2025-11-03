"""
Python Dictionaries - Student Starter Code
Unit 3, Lesson 2
"""

# =============================================================================
# PART 1: Creating and Accessing Dictionaries
# =============================================================================

# TODO: Create a user dictionary with username, followers, and verified keys


# TODO: Access the followers value


# TODO: Add a new key "posts" with value 120


# TODO: Delete the "verified" key



# =============================================================================
# PART 2: Dictionary Methods
# =============================================================================

# TODO: Use .get() to safely access a key that might not exist


# TODO: Loop through all keys in the dictionary


# TODO: Loop through all values in the dictionary


# TODO: Loop through all key-value pairs using .items()



# =============================================================================
# PART 3: Dictionaries in Functions
# =============================================================================

def get_display_name(user):
    """Return the display name from a user dictionary."""
    # TODO: Return user["name"] if it exists, otherwise return "Anonymous"
    pass


def update_score(player, points):
    """Add points to a player's score."""
    # TODO: Add the points to player["score"]
    pass


# =============================================================================
# CHALLENGE: Engagement Calculator
# =============================================================================

def analyze_post(post):
    """
    Calculate total and average engagement for a post.
    
    Parameters:
        post (dict): Dictionary with "likes", "comments", and "shares" keys
    
    Returns:
        dict: Dictionary with "total" and "average" keys
    """
    # TODO: Calculate total engagement (likes + comments + shares)
    
    # TODO: Calculate average engagement (total / 3)
    
    # TODO: Return a dictionary with total and average (rounded to 2 decimals)
    pass


# Test your function
if __name__ == "__main__":
    post = {"likes": 100, "comments": 20, "shares": 10}
    result = analyze_post(post)
    print(result)
    # Expected output: {"total": 130, "average": 43.33}
