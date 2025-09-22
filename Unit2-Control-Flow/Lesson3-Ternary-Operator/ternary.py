# JS Ternary
'''
let status = age >= 18 ? "adult" : "minor"
let message = score >= 90 ? "Excellent" : "Keep Trying"
'''
# Python Ternary
age = 15
status = "adult" if age >= 18 else "minor"
score = 75
message = "Excellent" if score >= 90 else "Keep Trying!" 

# Examples
password = "mypass1"
strength = "strong" if len(password) >= 8 else "weak"
print(f"Password:{password}\nStrength:{strength}")

#Combining Ternary + Chaining
category = ("Child" if 0 <= age <= 12 else 
            "Teen"  if 13 <= age <= 17 else
            "Adult" if 18 <= age <= 64 else
            "Senior"
            )

score = 89
grade = ("A" if 90 <= score <= 100 else
               "B" if 80 <= score < 90 else
               "C" if 70 <= score < 80 else
               "D" if 60 <= score < 70 else
               "F")