#Q1 - Solution 1
def format_phone_number(phone):
    """Format a phone number to (XXX) XXX-XXXX format."""
    # Remove all formatting characters
    clean = phone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    
    # # Check if exactly 10 digits
    # if len(clean) != 10:
    #     return "Invalid phone number"
    
    # # Check if all characters are digits
    # if not clean.isdigit():
    #     return "Invalid phone number"
    
    # Check if exactly 10 digits or all characters are digits
    if len(clean) != 10 or not clean.isdigit():
        return "Invalid phone number"
    
    # Format: (XXX) XXX-XXXX
    area = clean[0:3]      # First 3 digits
    prefix = clean[3:6]     # Next 3 digits
    line = clean[6:10]      # Last 4 digits
    
    return f"({area}) {prefix}-{line}" 

#Q1 - Alternative Solution
def format_phone_number(phone):
    # Step 1: Clean the input by removing spaces, hyphens, and parentheses
    cleaned = ""
    for ch in phone:
        if ch.isdigit():
            cleaned += ch

    # Step 2: Check if the cleaned string has exactly 10 digits
    if len(cleaned) != 10:
        return "Invalid phone number"

    # Step 3: Format as (XXX) XXX-XXXX
    area = cleaned[:3]
    middle = cleaned[3:6]
    last = cleaned[6:]
    return f"({area}) {middle}-{last}"
