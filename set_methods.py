# ==============================================================================
# Module: set_methods.py
# Topic: Set Methods (Mutations, Mathematical Venn Diagram Operations, Subsets)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. add() Method
# • What is it for: Adding a single hashable element into a set.
# • What it does: Inserts 32, 41, and 5 into set 's3' in arbitrary order.
# • Where it is used: Tracking seen IDs in algorithms (graph BFS/DFS visited sets).
# ------------------------------------------------------------------------------
#add method in sets
s3 = set()
s3.add(32)
s3.add(41)
s3.add(5)
print(s3)
print("----------------------------------------")

# ------------------------------------------------------------------------------
# 2. update() Method
# • What is it for: Adding multiple elements from an iterable (list, tuple, set) into the existing set.
# • What it does: Merges all items from s2 ({11, 22, 33}) into s3 in-place.
# • Where it is used: Batch adding newly imported category tags to an existing collection.
# ------------------------------------------------------------------------------
#updateing the existing set by using the update Method
s2 = {11, 22, 33}
s3.update(s2)
print(s3)

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 3. pop() Method
# • What is it for: Removing and returning an arbitrary element from the set.
# • What it does: Since sets are unordered, pop() removes whatever element is first in the hash table.
# • Where it is used: Pulling tasks out of an unordered worker pool until empty.
# ------------------------------------------------------------------------------
#pop method
s4 = {23, 24, 25, 26}
ele = s4.pop()
print(s4)
print(ele)

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 4. remove() vs discard() Methods
# • What is it for: Deleting a specific element from the set.
# • What it does:
#   - remove(8): Removes 8. If the item does not exist (like 18), raises KeyError!
#   - discard(50): Removes 50 if present; if absent, does nothing without raising any error!
# • Where it is used:
#   - remove(): When absence of the element indicates an unexpected bug/error state.
#   - discard(): Safe deletion when an element might or might not already be present.
# ------------------------------------------------------------------------------
#remove Method
s5 = {7, 8, 9, 5}
s5.remove(8)
#s5.remove(18)  # Would raise KeyError because 18 is not in s5
print(s5)

#discard Method
s5.discard(50)  # Safe: 50 is not in s5, but no error is raised
print(s5)

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 5. clear() Method
# • What is it for: Removing all elements from the set, leaving it empty.
# • What it does: Empties 's5' completely, turning it into set().
# • Where it is used: Resetting session filters, flushing cached identifiers.
# ------------------------------------------------------------------------------
#clear method, delete all the elements from the set and it will make it empty
s5.clear()
print(s5)

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 6. issubset() and issuperset() Methods
# • What is it for: Testing subset and superset containment relationships.
# • What it does:
#   - s6.issubset(s7): Returns True if EVERY element of s6 is also inside s7.
#   - s7.issuperset(s6): Returns True if s7 contains all elements of s6.
# • Where it is used: Role-based access control (checking if a user's permissions satisfy required permissions).
# ------------------------------------------------------------------------------
#issubset method
s6 = {9, 10, 11}
s7 = {21, 10, 22, 9, 11}
bv1 = s6.issubset(s7)
print(bv1)

#issuperset method
bv2 = s7.issuperset(s6)
print(bv2)

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 7. isdisjoint() Method
# • What is it for: Checking whether two sets have zero elements in common.
# • What it does: Compares s8 and s9; since 66 is present in both, they are NOT disjoint -> returns False.
# • Where it is used: Checking for conflicting schedule bookings or mutually exclusive user roles.
# ------------------------------------------------------------------------------
#isdis joint if same elements in diffrent set when comparing by suing disjoint i will show false
s8 = {88, 77, 66}
s9 = {66, 55, 44}
bv3 = s8.isdisjoint(s9)
print(bv3) 

print("----------------------------------------")

# ------------------------------------------------------------------------------
# 8. Mathematical Venn Diagram Operations: union, intersection, difference, symmetric_difference
# • What is it for: Performing set theory operations across two sets.
# • What it does:
#   - union(): Combines all unique items from s10 and s11 -> {12, 13, 14, 15, 16}.
#   - intersection(): Returns only items common to both -> {14}.
#   - difference(): Returns items in s10 that are NOT in s11 -> {12, 13}.
#   - symmetric_difference(): Returns items in either s10 or s11, but not both -> {12, 13, 15, 16}.
# • Where it is used:
#   - union: Consolidating mutual customer lists.
#   - intersection: Finding mutual friends / shared interests.
#   - difference: Finding churned users or missing dependencies.
#   - symmetric_difference: Finding discrepancies between two synchronized databases.
# ------------------------------------------------------------------------------
#union method it combine all  elements of both set except duplicates it taken only once
s10 = {12, 13, 14}
s11 = {14, 15, 16}
us = s10.union(s11)
print(us)

#intersection returns only duplicate value
inter = s10.intersection(s11)
print(inter)

#diffrence
ds = s10.difference(s11)
print(ds)

#symetric diffrence gives uncomman elements of both set
sd = s10.symmetric_difference(s11)
print(sd)
print("----------------------------------------")
