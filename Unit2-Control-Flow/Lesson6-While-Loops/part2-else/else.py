# while ... else
'''
The else clause runs when:
The loop completes normally
WITHOUT hitting a break
'''
#Basic Example 1
count = 1
while count <= 3:
    print(count)
    count += 1
else:
    print("Loop Completed!")
    
#Basic Example 2
count = 1
while count <= 5:
    print(count)
    if count == 3:
        break
    count += 1
else:
    print("This won't print!")

