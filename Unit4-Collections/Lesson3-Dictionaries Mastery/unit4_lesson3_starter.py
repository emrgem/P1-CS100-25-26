"""
Unit 4 - Lesson 3: Dictionaries Mastery
Your Turn Practice - Follow Along in Class!

Run each section as we go through the slides.
"""

# ============================================================
print("=" * 50)
print("YOUR TURN 1: Safe Access")
print("=" * 50)
# ============================================================

user = {
    "username": "StreamKing",
    "followers": 1500,
    "verified": True
}

a = user.get("username")
b = user.get("email")
c = user.get("email", "not provided")
d = user.get("followers", 0)

# PREDICT: What are a, b, c, and d?
# Write your predictions here:
# a = ???
# b = ???
# c = ???
# d = ???

# Uncomment below to check your answers:
# print(f"a = {a}")
# print(f"b = {b}")
# print(f"c = {c}")
# print(f"d = {d}")


# ============================================================
print("\n" + "=" * 50)
print("YOUR TURN 2: Iteration")
print("=" * 50)
# ============================================================

prices = {"basic": 9.99, "plus": 14.99, "premium": 19.99}

# PREDICT: What prints? How many lines?
# Write your prediction here:
# Line 1: ???
# Line 2: ???

# Uncomment below to check your answer:
# for plan, cost in prices.items():
#     if cost > 10:
#         print(f"{plan}: ${cost}")


# ============================================================
print("\n" + "=" * 50)
print("YOUR TURN 3: Dict Comprehension")
print("=" * 50)
# ============================================================

temps_c = {"Mon": 20, "Tue": 25, "Wed": 30}

# YOUR TASK: Convert to Fahrenheit using a dict comprehension
# Formula: F = C * 9/5 + 32
# Expected: {"Mon": 68.0, "Tue": 77.0, "Wed": 86.0}

# TODO: Write your comprehension here
temps_f = {day:temp * 9/5 + 32 for day,temp in temps_c.items()}

# Uncomment below to check your answer:
print(f"temps_f = {temps_f}")


# ============================================================
print("\n" + "=" * 50)
print("YOUR TURN 4: Filter Comprehension")
print("=" * 50)
# ============================================================

scores = {"Alice": 85, "Bob": 62, "Charlie": 91, "Diana": 58}

passing = {name: score for name, score in scores.items() 
           if score >= 70}

# PREDICT: What are the TWO lines of output?
# Line 1 (passing): ???
# Line 2 (len): ???

# Uncomment below to check your answers:
# print(passing)
# print(len(passing))


# ============================================================
print("\n" + "=" * 50)
print("YOUR TURN 5: Modify vs Return")
print("=" * 50)
# ============================================================

original = {"a": 1, "b": 2}

result = original.get("c", 99)
original.update({"c": 3})
doubled = {k: v * 2 for k, v in original.items()}

# PREDICT: What does original contain at the end?
# original = ???

# Uncomment below to check your answer:
# print(f"original = {original}")
