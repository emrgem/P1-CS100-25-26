# ============================================
# LESSON 2A: List Comprehensions - Basics & Filtering
# ============================================

# KEY SYNTAX:
# -------------------------------------------------
# Basic:   [expression for item in list]
# Filter:  [expression for item in list if condition]
# -------------------------------------------------

# KEY TAKEAWAYS:
# • Replaces: empty list → loop → append
# • Filter (if at end) REMOVES items that fail the test
# • Result is always a NEW list (original unchanged)


# ============================================
# YOUR TURN (from slides)
# ============================================

# Convert this loop to a comprehension:
view_counts = [1500, 23000, 890, 45000]

# Loop version (convert this to one line!)
in_thousands = []
for views in view_counts:
    in_thousands.append(views / 1000)

# TODO: Write your comprehension here
in_thousands = [views for views in view_counts]
print("Your Turn:", in_thousands)
in_thousands = [views/1000 for views in view_counts]
print("Your Turn:", in_thousands)

# Expected: [1.5, 23.0, 0.89, 45.0]


# ============================================
# PRACTICE 1: Convert Loop to Comprehension
# ============================================

prices = [12.99, 8.50, 15.00, 22.99]

# Loop version:
with_tax = []
for price in prices:
    with_tax.append(price * 1.08)

# TODO: Write your comprehension here
# with_tax = 

# print("P1:", with_tax)


# ============================================
# PRACTICE 2: String Transformation
# ============================================

# Make all usernames lowercase
usernames = ["Gamer_Pro", "MUSIC_FAN", "CodeNinja", "StreamKing"]

# TODO: Write your comprehension here
# lowercase = 

# print("P2:", lowercase)
# Expected: ["gamer_pro", "music_fan", "codeninja", "streamking"]


# ============================================
# PRACTICE 3: Filtering
# ============================================

# Keep only scores that are 70 or above
scores = [85, 62, 91, 58, 77, 69, 94]

# TODO: Write your comprehension with a filter
# passing = 

# print("P3:", passing)
# Expected: [85, 91, 77, 94]


# ============================================
# PRACTICE 4: Filter Empty Strings
# ============================================

# Keep ONLY non-empty usernames
usernames = ["gamer123", "", "pro_coder", "x", "music_lover", ""]

# TODO: Write your comprehension here
# valid = 

# print("P4:", valid)
# Expected: ["gamer123", "pro_coder", "x", "music_lover"]


# ============================================
# PRACTICE 5: Filter AND Transform
# ============================================

# Get lengths of songs that are under 4 minutes (240 sec)
# Convert to minutes (integer division)
song_lengths = [180, 320, 210, 195, 280, 165]

# TODO: Filter for < 240, then convert to minutes
# short_minutes = 

# print("P5:", short_minutes)
# Expected: [3, 3, 3, 2]
