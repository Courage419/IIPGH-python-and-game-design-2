# QUIZ-2
# USE LIST COMPREHENSION FOR THE FOLLOWING CONVERSIONS:

#1- convert [1, 2, 3, 4, 5] to [2, 4, 6, 8, 10]
original_list = [1, 2, 3, 4, 5]
converted_list = [x * 2 for x in original_list]
print(converted_list)

#2- convert [0, 1, 2,  3, 4, 5,] to [1, 2, 3, 4, 5, 6]
original_list = [0, 1, 2, 3, 4, 5]
converted_list = [x + 1 for x in original_list]
print(converted_list)

#3- convert [3, 4, 5, 6, 7, 8, 9, 10] to [7, 8, 9, 10]
original_list = [3, 4, 5, 6, 7, 8, 9, 10]
converted_list = [x for x in original_list if x >= 7]
print(converted_list)
