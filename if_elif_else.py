# ==============================================================================
# Module: if_elif_else.py
# Topic: Multi-Way Decision Making with 'if-elif-else' Ladder & Grade Evaluation
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Multi-Way Decision Branching with 'range()' Boundaries (Initial Implementation)
# • What is it for:
#   Categorizing numerical scores into discrete grade buckets using Python's `range()`.
# • What it does:
#   - Takes integer score input `marks`.
#   - Sequentially tests each condition:
#     - `marks in range(90, 100)`: checks if score is in [90, 99].
#     - `marks in range(80, 90)`: checks if score is in [80, 89].
#     - `marks in range(60, 80)`: checks if score is in [60, 79].
#     - `marks in range(35, 60)`: checks if score is in [35, 59].
#   - Note: In Python, `range(start, stop)` is half-open (excludes `stop`), meaning
#     a score of 100 would miss the range(90, 100) and fall through to 'else'.
# • Where it is used:
#   Tiered scoring systems, tax brackets, discount tier assignments.
# ------------------------------------------------------------------------------
'''
marks = int(input())
if marks in range(90 ,100):
    print("grade: A")
elif marks in range(80,90):
    print("grade : B")
elif marks in range(60,80):
    print("grade : C")
elif marks in range(35,60):
    print("grade : D")
else:
    print("grade : E")
'''

# ------------------------------------------------------------------------------
# 2. Refined Grade Evaluation with Relational Boundaries & Range Checks
# • What is it for:
#   Handling inclusive upper boundaries (e.g. 100) and distinguishing failing grades
#   from completely invalid/out-of-bounds input scores.
# • What it does:
#   - Evaluates `marks > 90 and marks <= 100` to correctly include 100 for "grade: A".
#   - Checks middle tiers using `in range()` (80-89 -> 'B', 60-79 -> 'C', 35-59 -> 'D').
#   - Evaluates `marks >= 0 and marks < 35` to print encouragement "Better luck next Time!!".
#   - Catches negative marks or numbers > 100 with the fallback `else: print("invalid marks")`.
# • Where it is used:
#   Academic grading systems, employee performance evaluations, gamification point tiering.
# ------------------------------------------------------------------------------
marks = int(input())
if marks > 90 and marks <= 100:
    print("grade: A")                   # Executed when 91 <= marks <= 100
elif marks in range(80, 90):
    print("grade : B")                  # Executed when 80 <= marks < 90
elif marks in range(60, 80):
    print("grade : C")                  # Executed when 60 <= marks < 80
elif marks in range(35, 60):
    print("grade : D")                  # Executed when 35 <= marks < 60
elif marks >= 0 and marks < 35:
    print("Better luck next Time!!")    # Executed for failing scores (0 to 34)
else:
    print("invalid marks")              # Executed for out-of-range scores (< 0 or > 100)
