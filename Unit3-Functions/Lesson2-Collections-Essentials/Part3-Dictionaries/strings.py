# PRACTICE 1: Format Course Code


# Step 1: Just get the input
code = "  webdev101  "
print(f"Original code: '{code}'")


# Step 2: Remove spaces with .strip()
code_clean = code.strip()
print(f"After strip:   '{code_clean}'")


# Step 3: Convert to uppercase with .upper()
code_upper = code_clean.upper()
print(f"After upper:   '{code_upper}'")


# Step 4: Or do it all at once (method chaining)
print("\nMethod chaining (one line):")
result = "  webdev101  ".strip().upper()
print(f"Result: '{result}'")


# Step 5: Put it in a function
print("\nAs a function:")


def format_course_code(code):
    """Format a course code: remove spaces, make uppercase."""
    return code.strip().upper()


# Test it
print(format_course_code("  webdev101  "))  # WEBDEV101
print(format_course_code("  Python202  "))  # PYTHON202
print(format_course_code("Java303"))        # JAVA303



# PRACTICE 2: Count Hashtags
print("\n" + "=" * 70)
print("PRACTICE 2: Count Hashtags")
print("=" * 70)


# Step 1: Start with a post
post = "Great game! #BergenTech #GoGamrz"
print(f"Post: {post}")


# Step 2: Split into words
words = post.split()
print(f"Words: {words}")


# Step 3: Check the first word
first_word = words[0]
print(f"First word: '{first_word}'")
print(f"Starts with #? {first_word.startswith('#')}")


# Step 4: Check all words one by one
print("\nChecking each word:")
for word in words:
    starts_with_hash = word.startswith("#")
    print(f"  '{word}' starts with #? {starts_with_hash}")


# Step 5: Count the hashtags
print("\nCounting hashtags:")
count = 0
for word in words:
    if word.startswith("#"):
        print(f"  Found hashtag: {word}, count = {count + 1}")
        count = count + 1
print(f"Total hashtags: {count}")


# Step 6: Put it in a function
print("\nAs a function:")


def count_hashtags(post):
    """Count how many hashtags are in the post."""
    words = post.split()
    count = 0
   
    for word in words:
        if word.startswith("#"):
            count = count + 1
   
    return count


# Test it
print(count_hashtags("Great game today! #BergenTech #GoGamrz #Pride"))
print(count_hashtags("Meeting tomorrow in room 205"))
print(count_hashtags("#Robotics team wins #StateChampionship! #STEM #BergenTech"))


