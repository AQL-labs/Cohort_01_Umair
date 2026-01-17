# This is for creating examples of set operations in Python

# Creating two sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("Set A:", A)
print("Set B:", B)

# Union of sets
union_set = A.union(B)
print("Union of A and B:", union_set)

# Intersection of sets
intersection_set = A.intersection(B)
print("Intersection of A and B:", intersection_set)

# Difference of sets
# A - B (Elements in A but not in B)
difference_set = A.difference(B)
print("Difference of A and B (A - B):", difference_set)

# Symmetric Difference of sets
# Elements in either A or B but not in both
symmetric_difference_set = A.symmetric_difference(B)
print("Symmetric Difference of A and B:", symmetric_difference_set)