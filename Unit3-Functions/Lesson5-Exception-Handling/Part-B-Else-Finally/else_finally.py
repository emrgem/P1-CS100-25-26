# else: Runs ONLY if the try block succeeded (no exceptions)
# try:
#     # Try something risky
#     score = int(input("Enter score: "))
# except ValueError:
#     # Runs if it FAILED
#     print("Invalid score!")
# else:
#     # Runs if it SUCCEEDED
#     print(f"✅ Score recorded: {score}")


def parse_command(message):
    """Parse a Discord command like: !ban PlayerName 7days"""
    try:
        parts = message.split()
        command = parts[0]
        target = parts[1]
        duration = parts[2]
    except IndexError:
        print("❌Invalid command format-missing parts!")
        return None
    else:
        print("✅Command parsed successfully!")
        if command.startswith("!"):
            print(f"⚡Executing: {command}")
        return command, target, duration
    finally: #Runs no matter what
        print("Finally block runs regardless!")
        
result = parse_command("!ban PlayerName 7day")
print(result)
result2 = parse_command("!ban")
print(result2)

"""
1-return is reached
2-Python stores the return value
3-Python jumps to the finally block
4-finally executes
5-After finally finishes → Python gives back the stored return value

Finally is designed for:
***Closing files
***Closing database connections
***Releasing memory
***Cleaning up even if return happens
"""