# unit4_lesson5_sets_data.py
# Data sets for the Sets lesson - all examples from slides

# ===== DATA FROM SLIDES =====

######1 DUPLICATES
# Slide: Problem 1 - Duplicates
favorites_list = ["Blinding Lights", "Bad Guy", "Blinding Lights"]
print(f"List :{favorites_list}")
print(f"List Length :{len(favorites_list)}")

# Slide: Set solution
favorites_set = {"Blinding Lights", "Bad Guy", "Blinding Lights"}
print(f"Set:{favorites_set}")
print(f"Set Length:{len(favorites_set)}")

# Slide: Creating sets with curly braces
genres = {"Rock", "Pop", "Jazz"}

# Slide: Creating sets from list
numbers_list = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers_list)
print(unique_numbers)

# Slide: Empty set examples
empty_dict = {}  # This is a dict, not a set!
empty_set = set()  # Correct empty set

# Slide: Quick check data
quick_check_data = {5, 3, 5, 1, 3, 5, 2, 1}


######2 FASTER Membership check
# Slide: Membership check
colors = {"red", "green", "blue"}
print("red" in colors)
print("yellow" in colors)

#Looping a Set
for color in colors:
    print(color)

#NO indexing
# print(colors[0]) - TyperError

# Slide: Adding items example
tags = {"python", "coding"}  # We'll add "tutorial" during lesson

tags.add("tutorial")
print(tags)

# Duplicates silently ignored, no error
tags.add("python")
print(tags)

# Remove item
tags.remove("coding")
print(tags)

# Remove item - can KeyError
# tags.remove("notexist")


#Safe Remove - discard()
tags.discard("safe_remove")


# Slide: Set operations data
gamers = {"Alice", "Bob", "Charlie", "Diana"}
coders = {"Bob", "Diana", "Eve", "Frank"}

#### 3 SET OPERATIONS######
# & Intersection (Items in both sets)
both = gamers & coders
print(both)

# | Union (All uniqe items from both)
everyone = gamers | coders
print(everyone)

# - Difference (Items in first but NOT second)
gamers_only = gamers - coders
print(gamers_only)


# Slide: Another quick check
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Slide: Remove duplicates pattern
scores = [85, 92, 78, 85, 90, 78]

# Slide: We do together - Playlists
my_songs = {"Song A", "Song B", "Song C"}
friend_songs = {"Song B", "Song C", "Song D"}

# Slide: Large set for fast lookup demo
# (We'll create this during the lesson to avoid memory issues)
# large_set = set(range(1000000))