# String Indexing
# ==================
word = "Python"
#       012345 (positive indexing)
word[0] #P (first character)
word[1] #y second character
word[5] #n last character
word[-1] #n last character
len(word) #length of the string
word[len(word)-1] #n last character

#String Slicing
# ==================
word[0:3] #Pyt (characters 0,1,2)
word[:3] #Pyt (characters 0,1,2)
word[2:5] #tho (characters 2,3,4)

word[2:6] #thon (characters 2,3,4,5)
word[2:len(word)] #thon (characters 2,3,4,5)
word[2:] #thon (characters 2,3,4,5)

word[-3:] #hon (characters -3,-2,-1 or 3,4,5)

# Part1-String Iteration Patterns
# Direct Character Iteration
word = 'hello'

for char in word:
    print(char)

# Index based Iteration
for i in range(len(word)):
    print(f"Character {i}: {word[i]}")
    
# Character Classification
# char = 'A'
char = input("Press a key:")
# Check character types using ASCII ranges
if 'A' <= char <= 'Z':
    print(f"'{char}' is an uppercase") 
    
if 'a' <= char <= 'z':
    print(f"'{char}' is a lowercase") 
    
if '0' <= char <= '9':
    print(f"'{char}' is a digit") 
    
if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
    print(f"'{char}' is a letter")