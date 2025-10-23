"""
Feature		Python
Create		[1, 2, 3]
Add		    .append(val)
Remove end	pop()
Insert		.insert(index, val)
Length  	len(list)
Slice	    [start:end]
Index		[0]
"""
# Creating lists
daily_likes = [500, 600, 750, 400]
usernames = ["@nasa", "@tswift", "@netflix"]
mixed_data = [500, "likes", "@user123", True]
# Accessing elements
first_day = daily_likes[0]      # 500
last_day = daily_likes[-1]      # 400 (negative indexing!)
third_day = daily_likes[2]      # 750
# Slicing (like JavaScript slice())
first_three = daily_likes[0:3]  # [500, 600, 750]
last_two = daily_likes[-2:]     # [750, 400]

# Code along - post analyzer
def analyze_post(likes_list):
    if likes_list:
        total = sum(likes_list)
        average = total / len(likes_list)
        best_day = max(likes_list)
        return (average, best_day)
    return "The list is empty!"


def format_usernames(handles):
    """Add @ prefix to all usernames."""
    formatted = []
    for handle in handles:
        formatted.append("@" + handle)
    return formatted

# Test
result = format_usernames(["nasa", "tswift", "netflix"])
print(result)  # ['@nasa', '@tswift', '@netflix']

def filter_trending_posts(likes_list):
    """Return posts with over 1000 likes."""
    trending = []
    for likes in likes_list:
        if likes > 1000:
            trending.append(likes)
    return trending

# Test
result = filter_trending_posts([500, 1200, 800, 1500, 600])
print(result)  # [1200, 1500]


def process_engagements(data):
    result = []
    for i in range(len(data)):
        if data[i] > 1000:
            result.append("Trending")
        elif i > 0 and data[i] > data[i-1]:
            result.append("Growing")
        else:
            result.append("Stable")
    return result

engagements = [500, 1200, 800, 1500, 600]
output = process_engagements(engagements)
print(output)

engagements = [500, 1200, 800, 1500, 600]

# i=0: 500 <= 1000, no previous → "Stable"
# i=1: 1200 > 1000 → "Trending"  
# i=2: 800 <= 1000, 800 < 1200 → "Stable"
# i=3: 1500 > 1000 → "Trending"
# i=4: 600 <= 1000, 600 < 1500 → "Stable"

result = ["Stable", "Trending", "Stable", "Trending", "Stable"]