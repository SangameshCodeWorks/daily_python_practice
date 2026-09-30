# ==============================================================================
# Module: if_else_condition.py
# Topic: Two-Way Decision Making with 'if-else' Conditional Statements
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Two-Way Branching (if - else) with String Length Validation
# • What is it for:
#   Providing two mutually exclusive execution paths: one executed when the
#   condition evaluates to True, and an alternative fallback executed when False.
# • What it does:
#   - Starts with `number = "Raj"`.
#   - Measures string length using `len(number)`, which evaluates to 3.
#   - Tests conditional expression `len(number) > 2` (3 > 2 -> True).
#   - Because condition is True:
#       Executes the 'if' block: prints "valid name".
#       Bypasses and ignores the 'else' block.
#   - If the name had 2 or fewer characters, it would execute the 'else' block instead.
# • Where it is used:
#   Form validation (enforcing minimum length on names, passwords, usernames),
#   authentication success vs failure, toggle states (online/offline, active/inactive).
# ------------------------------------------------------------------------------
number = "Raj"
print("start")

if len(number) > 2:
    print("valid name")     # Executed because len("Raj") is 3, which is > 2
else:
    print("invalid name")   # Alternative branch (executed only if condition is False)
