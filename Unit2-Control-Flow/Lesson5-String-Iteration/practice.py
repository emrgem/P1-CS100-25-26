text = "Hello World"
vowel_count = 0
# for char in text:
#     if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#         vowel_count += 1
#     elif char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
#         vowel_count += 1
# print(f"Vowels in '{text}': {vowel_count}")
vowels = "aeiouAEIOU"
for char in text:
    if char in vowels:
        vowel_count += 1
print(f"Vowels in '{text}': {vowel_count}")