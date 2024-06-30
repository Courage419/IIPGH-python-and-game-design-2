# MAP AND FILTER FUNCTIONS

# MAP
# def experiment(func, arg1):
#     return func(arg1)

# def subFunc(x):
#     return x * 5

# print(experiment)
# print(experiment(subFunc, 2))

# lis1 = [1,2,3,4,5,6]

# def doubled(num):
#     return num * 2

# def filterFunc(num):
#     return num > 3

# result = list(filter(filterFunc, lis1))
# print(result)


# REGULAR FUCTIONS VS LAMBDA FUCTIONS
# def doubled(num):
#     return num * 2

# LAMBDA FUCTIONS

# doubled = lambda num: num * 2
# print(doubled(25))

lis1 = [1,2,3,4,5,6]
filter_result = list(filter(lambda num: num > 3, lis1))
print(filter_result)
map_result = list(map(lambda num: num*2, lis1))
print(map_result)

# NESTED STATEMENTS AND SCOPE