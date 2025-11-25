# The raise syntax
# Basic syntax
"""
raise ExceptionType("Your message!")   
Examples:
raise ValueError("Quantity myst be at least 1)
raise TypeError("Expected a player object, got a potato!")
raise PermissionError("You are not a mod, nice try though!") 
"""
# Just returning
def open_loot_box(player, qty):
    if qty <= 0:
        return None
    #rest of the code
    
# Raising exception
def open_loot_box(player, qty):
    if qty <= 0:
        raise ValueError("Bad qty!")
    #rest of the code
    
VALID_PROTEINS = ['chicken', 'steak', "barbacoa", "carnitas"]
VALID_RICE = ["white", "brown", "none"]
VALID_BEANS = ["black", "pinto", "none"]
MAX_FREE_EXTRAS = 3

def build_bowl(protein, rice, extras):
    """Build a Chipotle bowl with validation.

    Raises:
    ValueError:if protein is invalid
    TypeError:if extras is not a list
    """
    #1check if extras is not a list
    if not isinstance(extras, list):
        raise TypeError("Extras must be a list!")
    #2Validate protein
    if protein.lower() not in VALID_PROTEINS:
        raise ValueError(f"'{protein}' isn't valid! Choose from: {VALID_PROTEINS} ")
    #3 return the bowl
    return {
        "protein": protein.lower(),
        "rice": rice,
        "extras": extras,
        "price": 10.50
    }
    
# Test the function
try:
    # bowl = build_bowl("chicken", "brown", "corn")
    bowl = build_bowl("chicken", "brown", ["corn"])
    print(f"Created : {bowl}")
except Exception as e:
    print(f"Error: {e}")