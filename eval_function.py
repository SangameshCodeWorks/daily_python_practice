# ==============================================================================
# Module: eval_function.py
# Topic: Dynamic Expression Evaluation with Python's Built-in eval()
# ==============================================================================

# Variables available in the local execution scope
a = 10
b = 20
l = [11, 22, 33]

# ------------------------------------------------------------------------------
# 1. Evaluating Dynamic Arithmetic and Function Calls
# • What is it for:
#   Parsing and executing a Python code expression passed dynamically as a string.
# • What it does:
#   Parses the string "a+b+(len(l))", looks up 'a' (10), 'b' (20), and len(l) (3),
#   evaluates the sum (10 + 20 + 3), and returns 33.
# • Where it is used:
#   Building command-line calculators, custom formula parsers in spreadsheet apps,
#   rule evaluation engines. (Caution: Never run eval() on untrusted user input due to code injection risks!).
# ------------------------------------------------------------------------------
result = eval("a+b+(len(l))")
print(result)

# ------------------------------------------------------------------------------
# 2. Parsing Complex Python Literals (Data Structures)
# • What is it for:
#   Instantiating native Python objects directly from text strings.
# • What it does:
#   Evaluates "{22,33,66}" as a Python set literal.
#   Returns an actual set object {33, 66, 22} of type <class 'set'>.
# • Where it is used:
#   Deserializing Python literal strings, reading custom structured configuration files.
# ------------------------------------------------------------------------------
result1 = eval("{22,33,66}")
print(type(result1))
print(result1)

# ------------------------------------------------------------------------------
# 3. Parsing Boolean / Primitive Literals
# • What is it for:
#   Converting boolean string representations ("True"/"False") into native boolean objects.
# • What it does:
#   Evaluates the string "False" as the Python keyword False of type <class 'bool'>.
# • Where it is used:
#   Interpreting flag values from text configuration files or environment variables.
# ------------------------------------------------------------------------------
result2 = eval("False")
print(type(result2))
print(result2)
