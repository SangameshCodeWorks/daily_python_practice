# ==============================================================================
# Module: Match_case.py
# Topic: Structural Pattern Matching with 'match-case' Statements (Python 3.10+)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Day of the Week Mapping Using 'match-case' Pattern Matching
# • What is it for:
#   Replacing long `if-elif-else` chains with clean, readable structural pattern
#   matching introduced in Python 3.10 (equivalent to switch-case in other languages).
# • What it does:
#   - Captures `day` as an integer (0 through 6).
#   - Matches `day` against specific literal patterns (`case 0:` through `case 6:`).
#   - Executes only the matched branch without requiring explicit `break` statements.
#   - The wildcard pattern `case _:` acts as the default / catch-all case when none of
#     the defined patterns match.
# • Where it is used:
#   State machine transitions, command dispatchers, HTTP status code routing,
#   weekday/calendar mapping, menu option handlers.
# ------------------------------------------------------------------------------
day = int(input())
match day:
    case 0:
        print("sunday")                     # Match for day 0: Sunday
    case 1:
        print("Monday")                     # Match for day 1: Monday
    case 2:
        print("Tuesday")                    # Match for day 2: Tuesday
    case 3:
        print("Wednesday")                  # Match for day 3: Wednesday
    case 4:
        print("Thrusday")                   # Match for day 4: Thursday
    case 5:
        print("Friday")                     # Match for day 5: Friday
    case 6:
        print("Satruday")                   # Match for day 6: Saturday
    case _:
        print("Input should be under 0-6")  # Wildcard / Default branch for any other value
