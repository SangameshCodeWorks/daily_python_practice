# ==============================================================================
# Module: print_function.py
# Topic: Advanced Formatting with print() Arguments (sep and end)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. The 'sep' (Separator) Parameter
# • What is it for:
#   Controls the character(s) placed between multiple values/arguments inside print().
# • What it does:
#   By default, sep=" " (a single space). You can override it with custom symbols
#   such as arrows ("->"), newlines ("\n"), empty strings (""), or custom delimiters.
# • Where it is used:
#   Generating CSV/TSV formatted lines, building file paths (e.g., sep="/"),
#   creating visual arrows in breadcrumb navigation, and joining output without extra string formatting.
# ------------------------------------------------------------------------------
#sep - separator helps to separate the values in the output
print(10, 20, 30, 40)                   # Default space separator: 10 20 30 40

print(10, 20, 30, 40, sep="->")         # Custom arrow separator: 10->20->30->40
print(10)                               # Single value: sep is not applied
print(20, 30, sep="\n")                 # Newline separator: prints each number on a new line
print(40, 50, sep="")                   # Empty string separator: concatenates with no spaces (4050)
print(60, 70, sep=" ")                  # Explicit single space separator (default behavior)

print("................................................")

# ------------------------------------------------------------------------------
# 2. The 'end' Parameter
# • What is it for:
#   Controls what character(s) are printed at the very end of the print statement.
# • What it does:
#   By default, end="\n" (newline), which moves the cursor to the next line.
#   Specifying a custom 'end' prevents the line break or adds trailing text.
# • Where it is used:
#   Command-line progress bars (e.g., printing dots '...' on the same line),
#   inline user prompts, building tabular console reports, and custom endings.
# ------------------------------------------------------------------------------
#end it tell what should be print in the end of the output

print(10, 20, 30, 40)                   # Ends with default '\n'
print(50, 60)                           # Starts on a new line, ends with '\n'
print(30, 60, 10, 70, 40, 60, end=" the END \n") # Appends custom ending string instead of just '\n'

print("................................................")

# ------------------------------------------------------------------------------
# 3. Combining 'sep' and 'end' in Complex Layouts
# • What is it for:
#   Gives complete fine-grained control over both intra-item separation and line termination.
# • What it does:
#   - end=" " keeps the next print call on the same console line separated by a space.
#   - sep="\n" splits the arguments across lines.
#   - sep="" and end="" fuses items tightly together with the subsequent print call.
# • Where it is used:
#   CLI dashbaords, formatted receipts, text games, matrix printing, and streaming tokens in AI chatbots.
# ------------------------------------------------------------------------------
print(10, 20, end=" ")                  # Prints 10 20 followed by space, no newline
print(30, 40, sep="\n")                 # Prints 30 on same line, then 40 on next line
print(50, 60, sep="", end="")           # Prints 5060 without spaces or trailing newline
print(70)                               # Appends 70 right next to 5060, then adds newline
