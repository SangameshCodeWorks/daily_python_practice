# ==============================================================================
# Module: Logical_operators2.py
# Topic: Non-Boolean Short-Circuiting Evaluation with Truthy and Falsy Values
# ==============================================================================

# Core Short-Circuit Rules in Python:
# • For 'X and Y':
#     If X is falsy, returns X immediately without evaluating Y.
#     If X is truthy, evaluates and returns Y.
# • For 'X or Y':
#     If X is truthy, returns X immediately without evaluating Y.
#     If X is falsy, evaluates and returns Y.
#
# Common Falsy Values: 0, 0.0, "", [], (), {}, set(), None, False
# All non-empty collections, non-zero numbers, and non-empty strings are Truthy.

# ------------------------------------------------------------------------------
# 1. Logical AND with Numeric Operands
# • What is it for: Demonstrating operand return values instead of pure booleans.
# • What it does:
#   - 5 and 4   : 5 is truthy -> returns second operand 4.
#   - 4 and 5   : 4 is truthy -> returns second operand 5.
#   - 0 and 0.4 : 0 is falsy -> short-circuits and returns 0.
# • Where it is used: Guard clauses and safe chained property checks.
# ------------------------------------------------------------------------------
print(5 and 4)      # Result: 4 (first is truthy -> returns 4)
print(4 and 5)      # Result: 5 (first is truthy -> returns 5)
print(0 and 0.4)    # Result: 0 (first is falsy -> short-circuits at 0)

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Logical AND with Heterogeneous Truthy & Falsy Values
# • What is it for: Evaluating combinations of collections, None, strings, and booleans.
# • What it does:
#   - 5 and []          : 5 is truthy -> returns []
#   - [0] and 0.2       : [0] has length 1 (truthy) -> returns 0.2
#   - True and "False"  : True is truthy -> returns string "False"
#   - "True" and "False": Non-empty string "True" is truthy -> returns "False"
#   - None and {}       : None is falsy -> returns None
#   - "" and 0          : Empty string is falsy -> returns ""
# • Where it is used: Safe traversal of optional nested structures without crashing.
# ------------------------------------------------------------------------------
# AND truthy value and falsy value
print(5 and [])             # Result: [] (5 is truthy, returns [])
print([0] and 0.2)          # Result: 0.2 ([0] is non-empty list, returns 0.2)
print(True and "False")     # Result: 'False' (True is truthy, returns 'False')
print("True" and "False")   # Result: 'False' ("True" is truthy, returns 'False')
print(None and {})          # Result: None (None is falsy, short-circuits at None)
print("" and 0)             # Result: '' (empty string is falsy, short-circuits at '')

print("------------------------------------------------")

# ------------------------------------------------------------------------------
# 3. Logical OR with Truthy & Falsy Values (Default Fallback Pattern)
# • What is it for:
#   Selecting the first truthy value or falling back to a default value.
# • What it does:
#   - 5 or []           : 5 is truthy -> short-circuits and returns 5
#   - [0] or 0.2        : [0] is truthy -> returns [0]
#   - True or "False"   : True is truthy -> returns True
#   - {0: None} or "False": Non-empty dict is truthy -> returns {0: None}
#   - None or {}        : None is falsy -> returns {}
#   - "" or 0           : "" is falsy -> returns 0
# • Where it is used:
#   Providing default fallback values: `user_name = input_name or 'Guest'`.
# ------------------------------------------------------------------------------
# OR truthy value and falsy value
print(5 or [])              # Result: 5 (5 is truthy, returns 5 immediately)
print([0] or 0.2)           # Result: [0] ([0] is non-empty, returns [0])
print(True or "False")      # Result: True (True is truthy, returns True)
print({0: None} or "False") # Result: {0: None} (dict has a key, returns dict)
print(None or {})           # Result: {} (None is falsy, returns empty dict {})
print("" or 0)              # Result: 0 (empty string is falsy, returns 0)

print("------------------------------------------------")
