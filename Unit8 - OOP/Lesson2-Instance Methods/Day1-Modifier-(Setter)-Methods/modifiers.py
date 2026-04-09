"""=============================================
 UNIT 8 - LESSON 2 - DAY 1: MODIFIER METHODS
================================================
TODAY'S GOAL:
  Add three methods to the Profile class that CHANGE its data:
    1. add_post(self, text)         — appends to self.posts
    2. gain_follower(self)          — adds 1 to self.followers
    3. follow(self, other_username) — appends to self.following
=============================================== """

class Profile:
    def __init__(self, username, display_name, bio):
        self.username = username
        self.display_name = display_name
        self.bio = bio
        self.followers = 0
        self.posts = []
        self.following = []
    # ---------------------------
    # TODO 1: Write add_post(self, text)
    # It should append `text` to self.posts
    # ---------------------------

    def add_post(self, text):
        self.posts.append(text)


    # ---------------------------
    # TODO 2: Write gain_follower(self)
    # It should add 1 to self.followers
    # ---------------------------

    def gain_follower(self):
        self.followers += 1


    # ---------------------------
    # TODO 3: Write follow(self, other_username)
    # It should append other_username to self.following
    # ---------------------------

    def follow(self, other_username):
        self.following.append(other_username)


# ==================================
# -------------TESTS ---------------
# ==================================

print("Creating Maria's Profile...")
maria = Profile("code_queen", "Maria", "Python Enthusiast!")
print(f"Username: {maria.username}")
print(f"Followers: {maria.followers}")
print(f"Posts: {maria.posts}")
print()

# Testing add_post method
print("Testing add_post method...")
maria.add_post("Hello BT!")
maria.add_post("Learning OOP today!")
print(f"Posts: {maria.posts}")
print()

# Testing gain_follower method
print("Testing gain_follower method...")
maria.gain_follower()
maria.gain_follower()
maria.gain_follower()
print(f"Followers: {maria.followers}")
print()


# Testing follow method
print("Testing follow method...")
maria.follow("python_guru")
maria.follow("real_python")
print(f"Following: {maria.following}")





