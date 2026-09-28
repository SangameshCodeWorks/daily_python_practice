# ==============================================================================
# Module: list_methods.py
# Topic: Built-in Python List Methods and Operations
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. append(item) Method
# • What is it for: Adding a single item to the very end of the list.
# • What it does: Modifies 'sangu' in-place by adding 110 after 108 -> [101, 102, 103, 104, 108, 110].
# • Where it is used: Appending incoming log entries, adding newly selected items to a shopping cart.
# ------------------------------------------------------------------------------
sangu = [101, 102, 103, 104, 108]
#var = type(sangu)
#print(var)
print(sangu)
sangu.append(110)
print(sangu)

# ------------------------------------------------------------------------------
# 2. insert(index, item) Method
# • What is it for: Inserting an item at a specific index, shifting existing items to the right.
# • What it does:
#   - insert(1, 51): Places 51 at index 1, shifting 102, 103... to the right.
#   - insert(-10, 100): When a negative index is beyond the list start, it prepends to index 0 -> [100, 10, ...].
# • Where it is used: Priority task insertion (adding high-priority job to front of queue).
# ------------------------------------------------------------------------------
sangu.insert(1, 51)
print(sangu)
print("----------------------------------------------")

l2 = [10, 20, 30, 50, 60]
l2.insert(-10, 100)
print(l2)
print("----------------------------------------------")

# ------------------------------------------------------------------------------
# 3. extend(iterable) Method
# • What is it for: Appending all elements from another list into the existing list in-place.
# • What it does: Modifies 'sangu' by appending each item from 'l2' without creating a new list.
# • Where it is used: Merging batch API responses into an existing data cache.
# ------------------------------------------------------------------------------
print("combining the two list using extend method, in existing the list")
sangu.extend(l2)
print(sangu)
print("-----------------------------------------------")

# ------------------------------------------------------------------------------
# 4. List Concatenation (+)
# • What is it for: Combining two lists into a brand new third list without altering originals.
# • What it does: Allocates new list 'list04' containing all elements of 'sangu' followed by 'l2'.
# • Where it is used: Immutable data pipelines, creating new combined datasets while preserving originals.
# ------------------------------------------------------------------------------
print("concatination of list it creates the new list called list04 to combine the sangu and l2")
list04 = sangu + l2
print(list04)
print("-----------------------------------------------")

# ------------------------------------------------------------------------------
# 5. pop() Method (Default & By Index)
# • What is it for: Removing and returning an item from the list.
# • What it does:
#   - pop(): Removes and returns the final element (24) -> leaves [21, 22, 23].
#   - pop(2): Removes and returns the item at index 2 (23) -> leaves [21, 22].
# • Where it is used: Implementing Stack (LIFO: Last-In-First-Out) and Queue (FIFO) data structures, undo actions.
# ------------------------------------------------------------------------------
print("removing the last element using pop method")
l5 = [21, 22, 23, 24]
rem_ele = l5.pop()
print(rem_ele)
print(l5) 
print("-----------------------------------------------")

print("removing the last element using pop method initializing the index number")
l5.pop(2)
print(l5)
print("-----------------------------------------------")

# ------------------------------------------------------------------------------
# 6. remove(value) Method
# • What is it for: Deleting the first occurrence of a specific value from the list.
# • What it does: Scans 'l7' for 98 and deletes the first instance found at index 1 -> leaves second 98 untouched.
# • Where it is used: Removing an unselected tag, canceling an order item by its product ID.
# ------------------------------------------------------------------------------
print("removing the first reoccring element  using remove method by giveing the direct element without index number")
l7 = [99, 98, 94, 95, 92, 93, 98, 100]
print("before:", l7)
l7.remove(98)
print("After:", l7)
print("-----------------------------------------------")

# ------------------------------------------------------------------------------
# 7. reverse() Method
# • What is it for: Reversing the elements of the list in-place.
# • What it does: Inverts order from [11, 22, 33, 44] to [44, 33, 22, 11] without allocating extra memory.
# • Where it is used: Displaying search results from newest to oldest, reverse chronological feeds.
# ------------------------------------------------------------------------------
#reverse
l8 = [11, 22, 33, 44]
l8.reverse()
print(l8)
print("-----------------------------------------------")

# ------------------------------------------------------------------------------
# 8. sort() Method
# • What is it for: Sorting items of the list in ascending order in-place.
# • What it does: Re-orders numbers from smallest to largest: [1, 2, 3, 4, 6, 7, 8, 9].
# • Where it is used: Ranking player scores, organizing prices from low to high in e-commerce.
# ------------------------------------------------------------------------------
#sort
l9 = [4, 6, 1, 9, 7, 3, 2, 8]
l9.sort()
print(l9)
print("-----------------------------------------------")

# ------------------------------------------------------------------------------
# 9. count(value) Method
# • What is it for: Counting how many times a given element appears in the list.
# • What it does: Counts occurrences of 11 in 'l10' -> returns 4.
# • Where it is used: Voting tallies, frequency analysis, counting failed login attempts.
# ------------------------------------------------------------------------------
#count
l10 = [33, 11, 45, 11, 32, 11, 33, 55, 45, 55, 11]
cou = l10.count(11)
print(cou)
print("-----------------------------------------------")

# ------------------------------------------------------------------------------
# 10. index(value) Method
# • What is it for: Finding the zero-based index of the first occurrence of a value.
# • What it does: Searches for 11 and returns index 1 (the first location where 11 appears).
# • Where it is used: Finding position of an item before replacing or inspecting it.
# ------------------------------------------------------------------------------
#index
l11 = [33, 11, 45, 11, 32, 11, 33, 55, 45, 55, 11]
ind = l11.index(11)
print(ind)
print("-----------------------------------------------")

# ------------------------------------------------------------------------------
# 11. Practical Problem: Sum of Smallest and Largest Number
# • What is it for: Finding the extreme values (min and max) after sorting.
# • What it does:
#   - Sorts [59, 12, 18, 14, 17] -> [12, 14, 17, 18, 59].
#   - Adds l[0] (smallest: 12) + l[-1] (largest: 59) -> 71.
# • Where it is used: Range analysis, outlier elimination, min-max normalization.
# ------------------------------------------------------------------------------
#sum of the smallest and the largest number in the list
l = [59, 12, 18, 14, 17]
l.sort()
sum = l[0] + l[-1]
print(l)
print(sum)

# ------------------------------------------------------------------------------
# 12. String split() vs list() Typecasting
# • What is it for: Demonstrating the difference between word tokenization and character explosion.
# • What it does:
#   - s1.split(): Splits on whitespace; because there are no spaces in "python", returns ['python'].
#   - list(s1): Iterates through string character-by-character -> ['p', 'y', 't', 'h', 'o', 'n'].
# • Where it is used:
#   - split(): Parsing sentences and space-delimited text.
#   - list(): Spell-checkers, anagram solvers, scrambling game letters.
# ------------------------------------------------------------------------------
s1 = "python"
s2 = s1.split()
print(s2)

s3 = list(s1)
print(s3)
