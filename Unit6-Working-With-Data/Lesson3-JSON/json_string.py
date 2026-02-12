# =============================================================================
# 🔤 PRACTICE: JSON Strings
# =============================================================================
# Practice with json.loads() and json.dumps()

import json
# Parse this JSON string from an "API response"
api_response = '{"status": "success", "revenue": 45000, "customers": 127}'

# YOUR CODE HERE:
# 1. Parse the string into a Python dictionary
data = json.loads(api_response) # converts to dictionary
# print(type(data)) 

import requests
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url) # if successful we get 200 status code
print(response) 
response_data = response.json() #converts json str to dict
print(f"{type(response_data)}")

# 2. Print the revenue
print(f"Revenue: ${data.get('revenue', 0):,}")

# 3. Convert back to a formatted JSON string
formatted_json = json.dumps(data, indent=4)
print("Formatted String")
print(formatted_json)


# =============================================================================
# 🏢 PRACTICE: Nested Data
# =============================================================================
# Work with nested JSON structures

company = {
    "name": "TechCorp",
    "founded": 2018,
    "location": {
        "city": "San Francisco",
        "state": "CA",
        "zip": "94105"
    },
    "departments": ["Sales", "IT", "Marketing", "Finance"]
}

# YOUR CODE HERE:
# 1. Print the city
print(f"City: {company['location']['city']}")
print(f"Department: {company['departments'][1]}")

# 2. Print the first department


# 3. Save this to "company_info.json"

