#Using keyword arguments
def create_gamer(username, level, xp, rank, online):
    """Create a gamer profile."""
    return {
        "username": username,
        "level": level,
        "xp": xp,
        "rank": rank,
        "online": online
    }

player1 = create_gamer(username="BTStudent",
                       level=25,
                       rank="Gold",
                       xp=10000,
                       online=True)
print(player1)


def send_message(sender, recipient, message, urgent):
    """Send a message between users."""
    return f"{sender} → {recipient}: {message} (Urgent: {urgent})"


# SOLUTION: Call using keyword arguments (order doesn't matter!)
msg = send_message(
    sender="Alex",
    recipient="Jordan",
    message="Check Discord",
    urgent=True
)


# *args - Accept Any Number of Values

def sum_scores(*scores):
    """Sum ANY Number of scores"""
    total = 0
    for score in scores:
        total += score
    return total

result = sum_scores(10,20,30)
result2 = sum_scores(10,20,30,55,68)

