# Pyramid Pattern

# STEP-BY-STEP GUIDE:
# Row 0: 4 spaces, 1 star
# Row 1: 3 spaces, 3 stars
# Row 2: 2 spaces, 5 stars
# Row 3: 1 space, 7 stars
# Row 4: 0 spaces, 9 stars

rows = 5
# Step1:create an outer loop for the rows
for i in range(rows):
    #step2:print the spaces rows-i-1
    for j in range(rows-i-1):
        print(" ", end="")
    #step3:print the stars 2*i+1
    for k in range(2*i+1):
        print("*", end="")
    #step4:print a new line
    print()