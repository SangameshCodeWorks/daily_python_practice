# ==============================================================================
# Module: input_function.py
# Topic: Interactive Console Input with input() and Explicit Typecasting
# ==============================================================================

# Note: The built-in input() function always captures user keystrokes as a string (str).
# To perform arithmetic or logical checks, explicit typecasting is essential.

# ------------------------------------------------------------------------------
# 1. Basic String Input and Integer Conversion
# • What is it for: Reading text from the user and converting it to an integer.
# • What it does:
#   - age = input(...) captures user input as a string (type <class 'str'>).
#   - iage = int(age) converts string to integer, allowing numeric addition (iage + 5).
# • Where it is used: Collecting user age on sign-up forms, calculating retirement years.
# ------------------------------------------------------------------------------
'''print("start")
age=input("Enter your age: ")
print(type(age))
iage = int(age)
print(type(iage))
print(iage+5)
print("end")'''

# ------------------------------------------------------------------------------
# 2. Integer Input for Arithmetic Calculations
# • What is it for: Performing mathematical calculations directly on integer inputs.
# • What it does:
#   Collects expected salary and desired increment as integers, then computes total sum.
# • Where it is used: HR payroll calculators, expense estimation forms.
# ------------------------------------------------------------------------------
'''
salary = int(input("enter the salary expect:"))
inc  = int(input("how much you need increment:"))
print(salary+inc)
'''

# ------------------------------------------------------------------------------
# 3. Floating-Point Input
# • What is it for: Reading decimal values from the user.
# • What it does: Converts the string entered for height to a float and adds 2.1 to it.
# • Where it is used: Fitness apps (tracking BMI, height, weight), currency and financial calculators.
# ------------------------------------------------------------------------------
'''
height = float(input("enter ypur height:"))
print(height+2.1)
'''

# ------------------------------------------------------------------------------
# 4. Complex Number Input
# • What is it for: Reading mathematical complex notation (e.g. 3+4j) from the user.
# • What it does: Parses the entered string into a complex number object.
# • Where it is used: Scientific simulation tools, electrical engineering calculation scripts.
# ------------------------------------------------------------------------------
'''
com = complex(input("enter any complex number:"))
print(type(com))
print(com)
'''

# ------------------------------------------------------------------------------
# 5. Boolean Input Gotcha / Pitfall
# • What is it for: Demonstrating how bool() behaves on input strings.
# • What it does:
#   IMPORTANT GOTCHA: In Python, bool(string) checks whether the string is non-empty!
#   If the user types "False", bool("False") is still TRUE because the string is not empty ("")!
#   To properly parse a boolean string, one should compare: input().strip().lower() == 'true'.
# • Where it is used: Crucial gotcha for form checkboxes, survey yes/no questions, CLI confirmation prompts.
# ------------------------------------------------------------------------------
bo = bool(input(" are You Indian (true/false) :"))
print(bo)
