# ==============================================================================
# Module: Conditional_statement.py
# Topic: Control Flow & Decision Making with the Simple 'if' Statement
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Simple 'if' Statement with Numeric Input Evaluation (Commented Demonstration)
# • What is it for:
#   Executing a specific code block conditionally only when a test condition is True.
# • What it does:
#   - Accepts an integer from user input.
#   - Evaluates whether 'num > 0'.
#   - If True: executes the indented block and prints the positive number.
#   - If False: skips the indented block and continues linear execution to 'end'.
# • Where it is used:
#   Input validation, checking positive quantities, filtering valid transaction amounts.
# ------------------------------------------------------------------------------
# Simple if statement pattern
'''
num = int(input())
print("Start")
if num > 0:
    print("positive number : ", num)
print("end")
'''

print("------------------------------------")

# ------------------------------------------------------------------------------
# 2. String Method Condition in 'if' Statement
# • What is it for:
#   Controlling program execution based on string properties and boolean method returns.
# • What it does:
#   - Evaluates `player.startswith("Pr")`.
#   - Since "Pradeep Narwal" starts with prefix "Pr", the expression returns True.
#   - Executes the guarded block: prints "the requirement are met".
#   - "start" and "end" delineate the unconditional entry and exit points.
# • Where it is used:
#   Validating prefixes (e.g. phone numbers starting with "+91", URL schemes "https://",
#   file extension filters, user identity checks).
# ------------------------------------------------------------------------------
player = "Pradeep Narwal"
print("start")
if player.startswith("Pr"):
    print("the requirement are met")
print("end")
