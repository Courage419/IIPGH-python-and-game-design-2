# QUIZ-4
# Q1
# Create set with set comprehesion where the set comprehension loops through
# two sets of iterables(in nested loops) giving us this format(containing tuples): {(n, m)}
# Example: Given these two iterables range(2)/ [0,1] and range(3, 5)/[3,4] use set comprehension to create
# this results: {(3, 0), (4, 0), (3, 1), (4, 1)}

# SOLUTION
# final_list = []
# final_set = {}
first_list = [1,2]
second_list = [5,6]


# for a in first_list:
#   for b in second_list:
#       final_list.append((a,b))

# print(final_list)

final_list = [(a,b) for a in first_list for b in second_list]
print(final_list)

final_set = {(a,b) for a in first_list for b in second_list}
print(final_set)

# Q2
# [5,6,7,2,4,1,2,3,8,4,5]
# Use list comprehension on the list above to return the same list of items and also use the same technique
# for set comprehension to return a set of that list.
# Compare the two results and explain to me the difference between the two types of comprehensions used

# SOLUTION
list_comprehension = [5,6,7,2,4,1,2,3,8,4,5]

using_list_comprehension = [num for num in list_comprehension ]

print(using_list_comprehension)
# The list comprehension allows you to write codes in shorter lines 
# By writing the code it displays a copy of the list given

using_set_comprehension = {num for num in list_comprehension}
print(using_set_comprehension)
# The set comprehension allow you to write codes in shorter lines too
# By writing this code, it returns a copy of the original one but does not repeat the numbers 
