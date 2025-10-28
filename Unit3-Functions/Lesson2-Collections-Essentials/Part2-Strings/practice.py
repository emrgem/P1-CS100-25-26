# Python Strings Practice Solutions
# ---------------------------------
# This file contains all 9 problems with detailed explanations and solutions.

# ---------------------------
# Question 1
# ---------------------------
# Code Tracing
school = "bergen tech"
# First, convert to uppercase, then replace 'TECH' with 'CTE'
result = school.upper().replace("TECH", "CTE")
print("Q1 Output:", result)  # Expected: BERGEN CTE


# ---------------------------
# Question 2
# ---------------------------
# Code Tracing
username = "  CodeMaster99  "
# Strip spaces and convert to lowercase
clean = username.strip().lower()
length = len(clean)
print("Q2 Output:", length)  # Expected: 12


# ---------------------------
# Question 3
# ---------------------------
# Code Writing
def create_username(first_name, last_name):
    """Combine first and last names with underscore, lowercase."""
    return f"{first_name}_{last_name}".lower()

# Examples
print("Q3 Output:", create_username("John", "Smith"))  # Expected: john_smith
print("Q3 Output:", create_username("MARY", "Jones"))  # Expected: mary_jones


# ---------------------------
# Question 4
# ---------------------------
# Code Tracing
email = "student@bergen.edu"
parts = email.split("@")        # ['student', 'bergen.edu']
domain = parts[1]               # 'bergen.edu'
first_part = domain[0:6]        # 'bergen'
print("Q4 Output:", first_part)  # Expected: bergen


# ---------------------------
# Question 5
# ---------------------------
# Code Tracing with conditionals
course = "Web Development"
if "web" in course.lower():
    result = course.replace(" ", "-")
else:
    result = course
print("Q5 Output:", result)  # Expected: Web-Development


# ---------------------------
# Question 6
# ---------------------------
# Code Writing
def check_email(email):
    """Return True if '@' in email and ends with .com (case-insensitive)."""
    email_lower = email.lower()
    return "@" in email_lower and email_lower.endswith(".com")

# Examples
print("Q6 Output:", check_email("test@gmail.com"))   # Expected: True
print("Q6 Output:", check_email("test@school.edu"))  # Expected: False


# ---------------------------
# Question 7
# ---------------------------
# Code Tracing (loop and counting vowels)
text = "Python Programming"
first_word = text.split()[0]  # 'Python'
vowel_count = 0
for char in first_word.lower():
    if char in "aeiou":
        vowel_count += 1
print("Q7 Output:", vowel_count)  # Expected: 1


# ---------------------------
# Question 8
# ---------------------------
# Code Tracing (boolean logic)
password = "Pass123"
length_ok = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
valid = length_ok and has_digit
print("Q8 Output:", valid)  # Expected: False


# ---------------------------
# Question 9
# ---------------------------
# Code Writing
def create_slug(title):
    """Convert title to lowercase, trim spaces, and replace spaces with hyphens."""
    return title.strip().lower().replace(" ", "-")

# Examples
print("Q9 Output:", create_slug("My First Blog Post"))   # Expected: my-first-blog-post
print("Q9 Output:", create_slug("  Python Tutorial  "))  # Expected: python-tutorial
