#syntax:
'''
initialize variable
while condition(test variable):
    code block
    increment/decrement variable
'''

# Example: Count to 5
print("=== Count to 5 ===")
count = 1


while count <= 5:
    print(count)
    count += 1
    
# YOUR TURN: Countdown Timer
num = 5


while num > 0:
    print(num)
    num -= 1
   
print("Blastoff!")

# Sum numbers 1 to 10
num = 1
total = 0

# while num <= 10:
#     total += num #(total = total + num)
#     num += 1

# print(f"Sum of numbers 1-10: {total}")

while num <= 10:
    total += num
    if num < 10:
        print(num, end="+")
    else:
        print(num, end="=")
    num += 1
print(total)
print()

# Sum of digits
# take a user input as int, and sum the digits of it
# number = input("Enter a number:") #1234
sum = 0
# for char in number:
#     print(f"{char} {type(char)}")
#     sum += int(char)
# print(f"Total {sum}")

# i=0
# while i<len(number):
#     sum += int(number[i])
#     i += 1
# print(f"Total {sum}")


# # Algorithm - sum of digits(as ints)
# n = int(input("Enter a number:"))
# number = n
# sum = 0
# while number > 0:
#     digit = number % 10 #Get the last digit
#     sum += digit # Add to sum
#     number = number // 10 # Remove the last digit
    
# print(f"The sum of digits {n}: {sum}")
    


# Algorithm - count digits (as ints)
number = 54321
n = number
count = 0

while number > 0:
    count += 1
    number = number // 10 # Remove the last digit
print(f"The number {n} has {count} digits!")
