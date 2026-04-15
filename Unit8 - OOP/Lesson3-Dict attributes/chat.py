class GroupChat:
    """A group chat with members and their roles."""

    def __init__(self, chat_name):
        self.name = chat_name
        self.members = {}   # username (str) : role (str)

    # ---- Method 1: add_member (modifier) ----
    def add_member(self, username, role):
        """Add a member with their role."""
        self.members[username] = role

    # ---- Method 2: get_member_list (getter) ⭐ NJIT Q37 pattern ----
    def get_member_list(self):
        """Return list of 'username - (role)' strings."""
        result = []
        for username, role in self.members.items():
            result.append(f"{username} - ({role})")
        return result

    # ---- Method 3: is_member (getter) ----
    def is_member(self, username):
        """Return True if username is in the chat, False otherwise."""
        return username in self.members

    # ---- Method 4: remove_member (conditional modifier) ----
    def remove_member(self, username):
        """Guard clause: check before deleting to avoid KeyError."""
        if username in self.members:
            del self.members[username]
            return True
        return False

    # ---- Method 5: get_all_usernames (getter) ----
    def get_all_usernames(self):
        """Return a list of all usernames in the chat."""
        # Verbose version (what you'd write first):
        # result = []
        # for username in self.members:
        #     result.append(username)
        # return result

        # Pythonic one-liner:
        return list(self.members.keys())

    # ---- Method 6: get_role (getter) ----
    def get_role(self, username):
        """Return the user's role, or None if not a member."""
        if username in self.members:
            return self.members[username]
        return None

    # ---- Method 7: update_role (conditional modifier) ----
    def update_role(self, username, new_role):
        """Update a user's role. Return True if updated, False otherwise."""
        if username in self.members:
            self.members[username] = new_role
            return True
        return False

    # ---- Method 8: clear_members (modifier) ----
    def clear_members(self):
        """Remove all members from the group."""
        self.members.clear()


# =============================================================================
# TESTS
# =============================================================================

if __name__ == "__main__":
    squad = GroupChat("Study Squad")

    print("=== Testing add_member ===")
    squad.add_member("maria", "admin")
    squad.add_member("jake", "member")
    squad.add_member("sam", "guest")
    print(squad.members)
    print()

    print("=== Testing get_member_list() ===")
    print(squad.get_member_list())
    print()

    print("=== Testing is_member(username) ===")
    print(squad.is_member("maria"))
    print(squad.is_member("gemici"))
    print()

    print("=== Testing get_all_usernames() ===")
    print(f"All usernames: {squad.get_all_usernames()}")
    print()

    print("=== Testing get_role(username) ===")
    print(f"Role of maria: {squad.get_role('maria')}")
    print(f"Role of bob:   {squad.get_role('bob')}")
    print()

    print("=== Testing update_role(username, new_role) ===")
    print(f"Promote jake to admin: {squad.update_role('jake', 'admin')}")
    print(f"Promote nobody:        {squad.update_role('nobody', 'admin')}")
    print(f"Jake's new role: {squad.get_role('jake')}")
    print()

    print("=== Testing remove_member(username) ===")
    print(f"Remove jake:   {squad.remove_member('jake')}")
    print(f"Remove gemici: {squad.remove_member('gemici')}")
    print(f"Final members: {squad.members}")
    print()

    print("=== Testing clear_members() ===")
    squad.clear_members()
    print(f"After clear: {squad.members}")