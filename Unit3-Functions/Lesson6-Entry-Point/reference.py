"""
Lesson 6: if __name__ == "__main__" - Quick Reference
"""

# __name__ changes based on how file is used:
#   Run directly → __name__ = "__main__"
#   Imported     → __name__ = "filename"


# ============================================================
# PATTERN
# ============================================================

def my_function():
    return "Hello!"

if __name__ == "__main__":
    # Only runs when file is executed directly
    # Skipped when imported
    print(my_function())


# ============================================================
# COMMON MISTAKES
# ============================================================

# ✅ CORRECT:
if __name__ == "__main__":
    pass

# ❌ WRONG:
# if __name__ == "main":        # Missing underscores
# if __name__ = "__main__":     # Single = (assignment)
# if _name_ == "__main__":      # Wrong variable
