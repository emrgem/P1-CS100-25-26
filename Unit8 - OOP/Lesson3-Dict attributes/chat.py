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
    
    # Method4: remove_member()
    def remove_member(self, username):
        """Guard Clause: check before deleting to avoid KeyError"""
        if username in self.members:
            del self.members[username]
            return True
        return False
    
    # Method5: get_all_usernames()
    # Returns a list of all usernames
    def get_all_usernames(self):
        # result = []
        # for username in self.members:
        #     result.append(username)
        # return result
        return list(self.members.keys())
    
        
    # Method6: update_role() - 
    # updates user's role, returns True if updated, False otherwise
    def update_role(self, username, new_role):
        if username in self.members:
            self.members[username] = new_role
            return True
        return False

    # Method7: clear_members() - Removes all members from the group
    def clear_members(self):
        self.members.clear()
        

# Test code
if __name__ == "__main__":
    squad = Groupchat("Study Squad")
    print("===Testing add_member===")
    squad.add_member("maria", "admin") 
    squad.add_member("jake", "member") 
    squad.add_member("sam", "guest")
    print(squad.members) 
    print()

    print("===Testing get_member_list()====")
    print(squad.get_member_list())
    print()

    print("===Testing is_member(username)====")
    print(squad.is_member("maria"))
    print(squad.is_member("gemici"))
    print()

    print("===Testing remove_member(username)===")
    print(f"Remove jake: {squad.remove_member('jake')}")
    print(f"Remove gemici: {squad.remove_member('gemici')}")
    print(f"Final Members: {squad.members}")
    print()

    print("===Testing get_all_usernames()===")
    print(f"All usernames: {squad.get_all_usernames()}")
    print()


    print("===Testing get_role(username)===")
    print(f"Role of maria: {squad.get_role('maria')}")
    print(f"Role of bob:   {squad.get_role('bob')}")
    print()

    print("===Testing clear_members===")
    squad.clear_members()
    print(f"After clear: {squad.members}")
