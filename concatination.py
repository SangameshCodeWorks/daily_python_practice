# ==============================================================================
# Module: concatination.py
# Topic: String Concatenation and Modern String Formatting (f-strings & .format())
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. String Concatenation using the '+' Operator
# • What is it for:
#   Joining multiple string fragments together into a single combined string.
# • What it does:
#   Adds strings firstname, space (" "), middlename, space (" "), and lastname
#   together into one cohesive string variable 'fullname'.
# • Where it is used:
#   Building display names, constructing URLs, assembling greetings, creating file names.
# ------------------------------------------------------------------------------
#concatination
firstname = "Rajendara"
middlename = "Raja"
lastname = "Cholan"

fullname = firstname + " " + middlename + " " + lastname
print(fullname)

# ------------------------------------------------------------------------------
# 2. Formatted String Literals (f-Strings) with User Input
# • What is it for:
#   Embedding variables directly inside a string template using {expression}.
# • What it does:
#   Collects student data (name as string, age as int, marks as float) and inserts
#   them cleanly into the formatted text string.
# • Where it is used:
#   Displaying student report cards, user profile summaries, confirmation receipts.
# ------------------------------------------------------------------------------
'''studentname = str(input("enter the Student full name :"))
sage = int(input("enter the student age : "))
smarks = float(input("enter the marks of student :"))
print(f"Student name is :{studentname} and age is {sage} and marks secured is {smarks}")
'''

# ------------------------------------------------------------------------------
# 3. Dynamic User Input and Multi-Type Data Collection
# • What is it for:
#   Reading varied data types (string, integer, float, boolean/evaluated literal) from the terminal.
# • What it does:
#   - str(input(...)): Reads text for player name and country.
#   - int(input(...)): Parses input string into an integer for age.
#   - float(input(...)): Parses input string into a decimal number for height.
#   - eval(input(...)): Dynamically evaluates Python literal (e.g. True/False boolean).
# • Where it is used:
#   Interactive CLI applications, onboarding questionnaires, sports statistics intake.
# ------------------------------------------------------------------------------
player = str(input("player name :"))
countryname = str(input("country name :"))
page = int(input("player age :"))
playerheight = float(input("player height :"))
islegend = eval(input("is legend :"))

# ------------------------------------------------------------------------------
# 4. Comparison: f-Strings vs str.format()
# • What is it for:
#   Two primary ways to inject dynamic variables into template strings.
# • What it does:
#   - f"{player}...": Evaluates expressions inline; fast, readable, modern (Python 3.6+).
#   - "{}...".format(...): Uses positional placeholder braces {} filled by arguments; backward-compatible.
# • Where it is used:
#   Generating personalized email alerts, dynamic database queries/logs, reports, UI displays.
# ------------------------------------------------------------------------------
print(f"{player} plays {countryname} age is {page} and height {playerheight} is a {islegend}")
print("{} plays {} age is {} and height {} is a {}".format(player, countryname, page, playerheight, islegend))
