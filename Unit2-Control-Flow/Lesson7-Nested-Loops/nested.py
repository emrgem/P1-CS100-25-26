#UNIT 2 - LESSON 7: NESTED LOOPS & PATTERN GENERATION
# PART 1: BASIC EXAMPLES - 1


# EXAMPLE-1- Basic Nested Loop Coordinates
# ======================================

# print("=" * 50)
# print("EXAMPLE 1: Basic Nested Loop Coordinates")
# print("=" * 50)

# for outer in range(3):
#     for inner in range(4):
#         print(f"({outer}, {inner})", end=" ")
#     print()  # New line after inner loop completes


# EXAMPLE-2- Rectangle of Stars
# ======================================


# print("\n" + "=" * 50)
# print("EXAMPLE 2: Right Triangle")
# print("=" * 50)

# rows = 5
# cols = 8
# for i in range(rows):
#     for j in range(cols):
#         print("*", end="")
#     print()


# EXAMPLE-3- Rectangle of Stars
# ======================================


# print("\n" + "=" * 50)
# print("EXAMPLE 3: Right Triangle")
# print("=" * 50)

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end="")
#     print()


# EXAMPLE-4- Number Triangle
# ======================================


# print("\n" + "=" * 50)
# print("EXAMPLE 4: Number Triangle")
# print("=" * 50)

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
    
    
# EXAMPLE-5- Multiplication Table (5x5)"
# ======================================

# print("\n" + "=" * 50)
# print("EXAMPLE 5: Multiplication Table (5x5)")
# print("=" * 50)

# for i in range(1, 6):
#     for j in range(1, 6):
#         product = i * j
#         print(f"{product:4}", end="")
#     print()

# n = 8
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         product = i * j
#         print(f"{product:4}", end="")
#     print()

