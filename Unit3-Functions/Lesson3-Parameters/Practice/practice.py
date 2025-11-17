# Question 2: Create Card Function
def create_card(name, level=1, active=False):
    # Write your code here
    pass

# Test Question 2
# print(create_card("Fireball"))  # Should return: {'name': 'Fireball', 'level': 1, 'active': False}
# print(create_card("Shield", level=3, active=True))  # Should return: {'name': 'Shield', 'level': 3, 'active': True}



# Question 4: Build Profile Function
# def build_profile(username, **stats):
#     profile = {"username":username}
#     # if no stats were provided
#     if not stats:
#         return profile
#     # if stats exists, build a profile
#     for key, value in stats.items():
#         profile[key] = value
#     return profile


# Way 2
def build_profile(username, **stats):
    profile = {"username":username}
    profile.update(stats)
    return profile

# Way 3
def build_profile(username, **stats):
    return {"username":username,**stats}


# Test Question 4
# print(build_profile("gamer42", score=850, rank="Gold"))  # Should return: {'username': 'gamer42', 'score': 850, 'rank': 'Gold'}
# print(build_profile("player1"))  # Should return: {'username': 'player1'}

# Question 6:

def make_notification(user, *messages, urgent=False):
    # Write your code here
    pass

# Test Question 6
# print(make_notification("admin", "Server down!", urgent=True))  # Should return: "URGENT: admin - Server down!"
# print(make_notification("user", "Welcome", "Check inbox"))  # Should return: "user - Welcome, Check inbox"


# Question 8: Log Action Function
def log_action(actor, *actions, timestamp=None, **context):
    # Write your code here
    pass

# Test Question 8
# print(log_action("bot", "login", "scan", source="API", ip="1.2.3.4"))  # Should return: "bot: login, scan | source=API, ip=1.2.3.4"

