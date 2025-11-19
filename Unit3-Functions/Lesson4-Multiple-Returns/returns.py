def search_data(query):
    if query == "": 
        return None    # No query provided
    if query == "empty": 
        return 0       # Found zero results
    if query == "error": 
        return False   # Search failed
    return len(query)  # Normal case - return count

#1 Return Type - None -> "No Value"
#Meaning: Absense of value, not set, not found
#Use for: Missing Data, search failures, optional parameters
result = None
print(result is None) #True - identity check
print(result == None) #True - equality check
print(not result)     #True - falsy check

#2 Return Type - False = Boolean False
#Meaning: Explicit false condition, validation failure, negative result
#Use for: Validation result, boolean operations, success/failure status
result = False
print(result is False) #True - identity check
print(not result)      #True - boolean negation
print(result == 0)     #True - falsy check

#3 Return Zero - A Valid Number
#Zero is VALID numeric value, not absense of value!
result = 0
print(result == 0)      #True - numeric equality
print(not result)       #True - (falsy in boolean context)
print(result is None)   #False - different objects
print(result is False)  #False - different types


#Multiple Returns - python packs multiple returns into a tuple!
def calculate_room(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter #Turns into a tuple (area,perimeter)

result = calculate_room(10, 5)
print(result)
print(type(result))

print(type((42))) #int
print(type((42,))) #tuple for single item
no_parentheses = 1,2,3
print(type(no_parentheses))

#unpacking tuple
area_result, perimeter_result = calculate_room(20, 6)
print(f"Area: {area_result}")
print(f"Perimeter: {perimeter_result}")

def analyze_grades(grades): 
    """Returns Avg, High, Low, Passed
        If no grades, return 0,0,0,False
    """
    if not grades:
        return 0,0,0,False
    average = sum(grades) / len(grades)
    highgest = max(grades)
    lowest = min(grades)
    passed = average >= 60 
    
    return average, highgest, lowest, passed

# Test case 1: Normal grades
print(analyze_grades([85, 92, 78, 90]))
# Should return: (86.25, 92, 78, True)

# Test case 2: Empty list  
print(analyze_grades([]))
# Should return: (0, 0, 0, False)

# Test case 3: All same
print(analyze_grades([80, 80, 80]))
# Should return: (80.0, 80, 80, True)