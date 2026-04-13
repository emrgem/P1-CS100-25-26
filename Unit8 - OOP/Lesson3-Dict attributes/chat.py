class Groupchat:
    """A group chat with members and their roles"""
    def __init__(self, chat_name):
        self.name = chat_name
        self.members = {} # username (str) : role (str)   
    # Method1: add_member(modifier)
    def add_member(self, username, role):
        """Add a member with their role"""
        self.members[username] = role
    
    # Method2: get_member_list()
    def get_member_list(self):
        """Return list of 'username' (role) strings"""
        result = []
        for username, role in self.members.items():
            result.append(f"{username} - ({role})")
        return result
    
    # Method3: is_member()
    def is_member(self, username):
        """Return True if username is in the chat, False otherwise."""
        return username in self.members
# Test code
squad = Groupchat("Study Squad")
print("===Testing add_member===")
squad.add_member("maria", "admin") 
squad.add_member("jake", "member") 
squad.add_member("sam", "guest")
print(squad.members) 

print("===Testing get_member_list()====")
print(squad.get_member_list())

print("===Testing is_member(username)====")
print(squad.is_member("maria"))
print(squad.is_member("gemici"))