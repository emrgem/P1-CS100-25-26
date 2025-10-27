# solutions_part1_lists.py

# Practice 1 Solution: Format Usernames
def format_usernames(handles):
    """Add @ prefix to all usernames."""
    formatted = []
    for handle in handles:
        formatted.append("@" + handle)
    return formatted

# Test Practice 1
print("Practice 1 Test:")
result1 = format_usernames(["nasa", "tswift", "netflix"])
print(result1)  # ['@nasa', '@tswift', '@netflix']
print()

# Practice 2 Solution: Filter Trending Posts
def filter_trending_posts(likes_list):
    """Return posts with over 1000 likes."""
    trending = []
    for likes in likes_list:
        if likes > 1000:
            trending.append(likes)
    return trending

# Test Practice 2
print("Practice 2 Test:")
result2 = filter_trending_posts([500, 1200, 800, 1500, 600])
print(result2)  # [1200, 1500]
print()

# Practice 3 Solution: Engagement Stats
def engagement_stats(engagements):
    """Calculate comprehensive engagement statistics."""
    if not engagements:
        return {"average": 0, "max": 0, "min": 0, "trending_days": 0}
    
    average = sum(engagements) / len(engagements)
    maximum = max(engagements)
    minimum = min(engagements)
    
    trending_days = 0
    for engagement in engagements:
        if engagement > 1000:
            trending_days += 1
    
    return {
        "average": average,
        "max": maximum,
        "min": minimum,
        "trending_days": trending_days
    }

# Test Practice 3
print("Practice 3 Test:")
weekly = [1200, 800, 1500, 900, 1100]
result3 = engagement_stats(weekly)
print(result3)  # {'average': 1100.0, 'max': 1500, 'min': 800, 'trending_days': 3}
print()

# Code Tracing 1 Solution
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

print("Code Tracing 1:")
engagements = [500, 1200, 800, 1500, 600]
output1 = process_engagements(engagements)
print(output1)  # ['Stable', 'Trending', 'Stable', 'Trending', 'Stable']
print(len([r for r in output1 if r == "Trending"]))  # 2
print()

# Code Tracing 2 Solution
def analyze_growth(daily_likes):
    if not daily_likes:
        return []
    
    growth_pattern = []
    for i in range(1, len(daily_likes)):
        if daily_likes[i] > daily_likes[i-1]:
            growth_pattern.append("Up")
        elif daily_likes[i] < daily_likes[i-1]:
            growth_pattern.append("Down")
        else:
            growth_pattern.append("Same")
    return growth_pattern

print("Code Tracing 2:")
data = [100, 150, 150, 120, 200]
result4 = analyze_growth(data)
print(result4)  # ['Up', 'Same', 'Down', 'Up']
print(result4.count("Up"))  # 2
print()

# Code Tracing 3 Solution
def process_data(values):
    result = []
    temp = values[:]  # Create a copy
    
    while temp:
        if temp[0] % 2 == 0:
            result.append(temp.pop(0) * 2)
        else:
            result.append(temp.pop(0) // 2)
    
    return result

print("Code Tracing 3:")
data = [10, 5, 8, 3]
output2 = process_data(data)
print(output2)  # [20, 2, 16, 1]
print(data)     # [10, 5, 8, 3] (original unchanged)
print()

# Challenge Solution: Post Analyzer Pro
def calculate_engagement(likes, shares, comments):
    return likes + shares + comments

def get_engagement_tier(total_engagement):
    if total_engagement < 500:
        return "Low"
    elif total_engagement <= 2000:
        return "Medium"
    else:
        return "High"

def analyze_posts(post_data):
    tiers = []
    for post in post_data:
        likes, shares, comments = post
        total = calculate_engagement(likes, shares, comments)
        tier = get_engagement_tier(total)
        tiers.append(tier)
    return tiers

print("Challenge Solution:")
posts = [[500, 50, 100], [1000, 200, 300], [100, 10, 20]]
result5 = analyze_posts(posts)
print(result5)  # ['Medium', 'High', 'Low']
print()

# Additional Test Cases
print("Additional Test Cases:")
print("Empty list test:", engagement_stats([]))
print("Single element test:", engagement_stats([1500]))
print("All trending test:", engagement_stats([1200, 1500, 1800]))
print("No trending test:", engagement_stats([500, 800, 900]))