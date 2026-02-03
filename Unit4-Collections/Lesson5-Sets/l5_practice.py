# ============================================================
# PART 2: CODE WRITING
# ============================================================

print("\n" + "=" * 60)
print("PART 2: CODE WRITING")
print("=" * 60)


# ------------------------------------------------------------
# Exercise 1: Remove Duplicates
# ------------------------------------------------------------
print("\n--- Exercise 1: Remove Duplicates ---")

def get_unique_sorted(items):
    """
    Remove duplicates and return sorted list.
    
    Args:
        items: List that may contain duplicates
    
    Returns:
        list: Sorted list with duplicates removed
    
    Example:
        get_unique_sorted([3, 1, 2, 1, 3, 2])
        Returns: [1, 2, 3]
    """
    # TODO: Convert to set to remove duplicates
    
    # TODO: Sort and return as list
    pass  # Remove this when you add your code


# Test Exercise 1
# # Uncomment when ready to test:
# result = get_unique_sorted([3, 1, 2, 1, 3, 2, 5, 4, 5])
# print(f"Result: {result}")
# # Expected: [1, 2, 3, 4, 5]

# result2 = get_unique_sorted(["banana", "apple", "banana", "cherry"])
# print(f"Result 2: {result2}")
# # Expected: ['apple', 'banana', 'cherry']


# ------------------------------------------------------------
# Exercise 2: Find Common Items
# ------------------------------------------------------------
print("\n--- Exercise 2: Find Common Items ---")

def find_common_interests(person1_interests, person2_interests):
    """
    Find interests that both people share.
    
    Args:
        person1_interests: List of interests for person 1
        person2_interests: List of interests for person 2
    
    Returns:
        set: Interests they have in common
    
    Example:
        find_common_interests(
            ["gaming", "music", "coding"],
            ["music", "art", "coding", "reading"]
        )
        Returns: {"music", "coding"}
    """
    # TODO: Convert both lists to sets
    
    # TODO: Return the intersection
    pass  # Remove this when you add your code


# Test Exercise 2
# Uncomment when ready to test:
# alice = ["gaming", "music", "coding", "movies"]
# bob = ["music", "art", "coding", "reading"]
# common = find_common_interests(alice, bob)
# print(f"Common interests: {common}")
# # Expected: {"music", "coding"}


# ------------------------------------------------------------
# Exercise 3: Get Unique Tags from Posts
# ------------------------------------------------------------
print("\n--- Exercise 3: Unique Tags ---")

def get_all_unique_tags(posts):
    """
    Get all unique tags across all posts.
    
    Args:
        posts: List of post dictionaries, each with a "tags" key
               containing a list of tag strings
    
    Returns:
        set: All unique tags
    
    Example:
        posts = [
            {"title": "Post 1", "tags": ["python", "coding"]},
            {"title": "Post 2", "tags": ["python", "tutorial"]}
        ]
        Returns: {"python", "coding", "tutorial"}
    """
    # TODO: Create empty set for all tags
    all_tags = set()
    # TODO: Loop through posts and add tags to set
    # Hint: Use .update() to add multiple items at once
    for post in posts:
        all_tags.update(post.get("tags", []))
    # TODO: Return the set of all unique tags
    return all_tags


# Test Exercise 3
# Uncomment when ready to test:
posts = [
    {"title": "Intro to Python", "tags": ["python", "beginner", "tutorial"]},
    {"title": "Advanced Python", "tags": ["python", "advanced", "tips"]},
    {"title": "Web Dev Basics", "tags": ["html", "css", "beginner"]},
]
all_tags = get_all_unique_tags(posts)
print(f"All unique tags: {all_tags}")
print(f"Tag count: {len(all_tags)}")
# Expected: {"python", "beginner", "tutorial", "advanced", "tips", "html", "css"}
# Count: 7


# ------------------------------------------------------------
# Exercise 4: Compare Playlists
# ------------------------------------------------------------
print("\n--- Exercise 4: Compare Playlists ---")

def compare_playlists(playlist1, playlist2):
    """
    Compare two playlists and return analysis.
    
    Args:
        playlist1: List of song titles (first playlist)
        playlist2: List of song titles (second playlist)
    
    Returns:
        dict: Dictionary with keys:
              - "common": set of songs in both
              - "only_playlist1": set of songs only in first
              - "only_playlist2": set of songs only in second
              - "total_unique": total count of unique songs
    
    Example:
        compare_playlists(
            ["Song A", "Song B", "Song C"],
            ["Song B", "Song C", "Song D"]
        )
        Returns: {
            "common": {"Song B", "Song C"},
            "only_playlist1": {"Song A"},
            "only_playlist2": {"Song D"},
            "total_unique": 4
        }
    """
    # TODO: Convert both playlists to sets
    
    # TODO: Calculate common (intersection)
    
    # TODO: Calculate only in first (difference)
    
    # TODO: Calculate only in second (difference)
    
    # TODO: Calculate total unique (union length)
    
    # TODO: Return dictionary with all results
    pass  # Remove this when you add your code


# Test Exercise 4
# Uncomment when ready to test:
my_songs = ["Blinding Lights", "Bad Guy", "Levitating", "Stay"]
friend_songs = ["Bad Guy", "Stay", "Heat Waves", "As It Was"]

comparison = compare_playlists(my_songs, friend_songs)
if comparison:
    print(f"Songs we both have: {comparison['common']}")
    print(f"Only I have: {comparison['only_playlist1']}")
    print(f"Only friend has: {comparison['only_playlist2']}")
    print(f"Total unique songs: {comparison['total_unique']}")


# ------------------------------------------------------------
# Exercise 5: Permission Checker
# ------------------------------------------------------------
print("\n--- Exercise 5: Permission Checker ---")

def check_permissions(user_permissions, required_permissions):
    """
    Check if user has all required permissions.
    
    Args:
        user_permissions: List or set of permissions user has
        required_permissions: List or set of required permissions
    
    Returns:
        tuple: (has_access, missing_permissions)
               - has_access: True if user has ALL required permissions
               - missing_permissions: Set of permissions user is missing
    
    Example:
        check_permissions(
            ["read", "write"],
            ["read", "write", "delete"]
        )
        Returns: (False, {"delete"})
    """
    # TODO: Convert both to sets
    user_set = set(user_permissions)
    required_set = set(required_permissions)
    # TODO: Find missing permissions (required - user_has)
    missing = required_set - user_set
    # TODO: Check if user has access (missing is empty)
    # has_access = len(missing) == 0
    has_access = True if not missing else False
    # TODO: Return tuple of (has_access, missing)
    return has_access, missing


# Test Exercise 5
# Uncomment when ready to test:
# user = ["read", "write", "comment"]
# admin_required = ["read", "write", "delete", "manage"]
# 
# has_access, missing = check_permissions(user, admin_required)
# print(f"Has admin access: {has_access}")
# print(f"Missing permissions: {missing}")
# # Expected: False, {"delete", "manage"}
# 
# editor_required = ["read", "write"]
# has_access2, missing2 = check_permissions(user, editor_required)
# print(f"Has editor access: {has_access2}")
# print(f"Missing: {missing2}")
# # Expected: True, set()


