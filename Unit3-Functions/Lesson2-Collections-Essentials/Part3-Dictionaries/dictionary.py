"""
Python Dictionaries - Student Starter Code
Unit 3, Lesson 2 Part3
"""

# =============================================================================
# PART 1: Creating and Accessing Dictionaries
# =============================================================================

# Creating a dictionary
user = {
    "username": "nasa",
    "followers": 50000,
    "verified": True
}

# Accessing values
count = user["followers"]  # 50000

# Adding a new key-value pair
user["posts"] = 120

# Deleting a key
del user["verified"]

# Dictionary after modifications:
# {"username": "nasa", "followers": 50000, "posts": 120}


# =============================================================================
# PART 2: Dictionary Methods
# =============================================================================

# .get() method - safe access (avoids KeyError)
bio = user.get("bio", "No bio available")  # Returns default if key doesn't exist

# .keys() - get all keys
for key in user.keys():
    print(key)

# .values() - get all values
for value in user.values():
    print(value)

# .items() - get all key-value pairs
for key, value in user.items():
    print(f"{key}: {value}")

# Checking if a key exists
if "username" in user:
    print(user["username"])

# Copy a dictionary
user_copy = user.copy()


# =============================================================================
# PART 3: Dictionaries in Functions
# =============================================================================

# EXAMPLE 1: Passing dictionaries to functions
def get_display_name(user):
    """Return the display name from a user dictionary."""
    return user.get("name", "Anonymous")

# EXAMPLE 2: Modifying dictionaries in functions
def update_score(player, points):
    """Add points to a player's score."""
    player["score"] += points  # Modifies original dictionary

# EXAMPLE 3: Returning dictionaries from functions
def create_product(name, price):
    """Create and return a product dictionary."""
    return {
        "name": name,
        "price": price,
        "in_stock": True
    }


# =============================================================================
# LOOPING PATTERNS
# =============================================================================

# Pattern 1: Loop through keys only
for key in user:
    print(key)

# Pattern 2: Loop through keys and values
for key, value in user.items():
    print(f"{key}: {value}")

# Pattern 3: Loop through values only
for value in user.values():
    print(value)

