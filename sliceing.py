# ==============================================================================
# Module: sliceing.py
# Topic: Sequence Slicing Syntax (start:stop:step) on Lists and Strings
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Slicing Mechanics on Lists
# Slicing syntax formula: sequence[start : stop : step]
#   - start: index where slice begins (inclusive). Defaults to 0 (or end if step is negative).
#   - stop:  index where slice ends (exclusive, up to stop - 1).
#   - step:  increment amount. Positive moves forward, negative moves backward.
# ------------------------------------------------------------------------------
#slicing on list

l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# • What is it for: Extracting a continuous sub-range of elements.
# • What it does: Starts at index 4 (50) up to index 7 (exclusive, so up to index 6: 70) with step 1 -> [50, 60, 70].
# • Where it is used: Paginating list data, grabbing a batch of records.
print(l1[4:7:1])

# • What is it for: Extracting elements at regular intervals (skipping items).
# • What it does: From index 1 to 9 with step 3 -> picks index 1 (20), 4 (50), 7 (80) -> [20, 50, 80].
# • Where it is used: Sub-sampling data, selecting every Nth sensor reading or frame.
print(l1[1:9:3])

# • What is it for: Grabbing the first N elements from the start.
# • What it does: Omits 'start' (defaults to 0) up to index 6 exclusive -> [10, 20, 30, 40, 50, 60].
# • Where it is used: Getting "Top N" items (e.g. top 5 highest scores or leaderboard leaders).
print(l1[:6:])

# • What is it for: Extracting everything from a starting index to the end of the list.
# • What it does: Starts at index 5 (60) and proceeds until the final element -> [60, 70, 80, 90].
# • Where it is used: Discarding metadata headers or first few processed items to get the rest.
print(l1[5::])

# • What is it for: Stepping backwards through a sequence.
# • What it does: Starts at index 7 (80), steps backwards by -3 down to index 0 exclusive -> picks indices 7 (80), 4 (50), 1 (20) -> [80, 50, 20].
# • Where it is used: Reverse traversal without modifying the original list.
print(l1[7:0:-3])

# • What is it for: Creating a reversed copy of the list.
# • What it does: Omits start and stop with step -1, reversing the entire sequence -> [90, 80, 70, 60, 50, 40, 30, 20, 10].
# • Where it is used: Checking palindromes, chronological reversal (newest to oldest), undo stacks.
print(l1[::-1])

print("-----------------------------------------------")

# ------------------------------------------------------------------------------
# 2. Slicing on Strings
# • What is it for: Extracting substrings from a string without mutating the original string.
# • What it does: Takes "22BBTECo23" and extracts characters from index 5 up to index 7 exclusive
#   (index 5 is 'E', index 6 is 'C') -> "EC".
# • Where it is used: Parsing standardized ID numbers, extracting department codes from roll numbers,
#   reading area codes from phone numbers.
# ------------------------------------------------------------------------------
#sliceing on Strings

l2 = "22BBTECo23"
print(l2[5:7])
