# Input Validation 1 - Username Validation
while True:
    username = input("Enter a username (3-15 chars):")
    if len(username) < 3:
        print("Too short! Min 3 characters!")
        continue
    if len(username) > 15:
        print("Too long! Max 15 characters!")
        continue
    # check if username has any space
    has_space = False
    for char in username:
        if char == ' ':
            has_space = True
            break
    if has_space:
        print("No spaces allowed!")
        continue
    # username validation passed
    print(f"Username '{username}' accepted!\n")
    break
    