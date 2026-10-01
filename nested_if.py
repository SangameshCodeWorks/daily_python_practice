# ==============================================================================
# Module: nested_if.py
# Topic: Nested Conditional Statements & Hierarchical Decision Branching
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Multi-Stage Eligibility Verification Using Nested 'if' Statements
# • What is it for:
#   Evaluating dependent conditions where a secondary condition only needs to be
#   tested if a primary gatekeeping condition evaluates to True.
# • What it does:
#   - Outer Gatekeeper: Checks if `iscitizen == "Yes" or iscitizen == "yes"`.
#     - If False: Skips the inner check and jumps to outer `else` ("not the citizen of India").
#     - If True: Enters the inner block and requests `age`.
#   - Inner Decision: Checks whether `age >= 18`.
#     - If True: Prints "Voting Granted".
#     - If False: Prints "Not eligible to Vote".
# • Where it is used:
#   Voter eligibility verification, two-factor authentication gates, multi-stage KYC
#   verification, subscription tier feature access control.
# ------------------------------------------------------------------------------
iscitizen = (input("are you Citizen of India: (Yes/No) "))
if(iscitizen == "Yes" or iscitizen =="yes"):
    age = int(input("enter you age:"))
    if(age>=18):
        print("Voting Granted")         # Executed if Indian citizen AND age >= 18
    else:
        print("Not eligible to Vote")   # Executed if Indian citizen BUT age < 18
else:
    print("not the citizen of India")   # Executed if iscitizen is neither 'Yes' nor 'yes'
