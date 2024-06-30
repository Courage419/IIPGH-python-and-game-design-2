
# ASSIGMENT-1

# Convert this regular functions into lambda functions:
# def addFunc(a, b):
#     return a + b

# def addFunc(a, b):
#     if(a > b):
#         return a
#     else:
#         return b


# explore the reduce function

                                # SOLUTIONS
addFunc = lambda a, b: a + b
print(addFunc)


addFunc = lambda a, b: a if a > b else b
print(addFunc)