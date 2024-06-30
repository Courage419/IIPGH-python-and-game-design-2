
# # PACKING AND UNPACKING TUPLES/LISTS/DICTIONARIES
# #PACKING
# lis1 = [1,2,4,3,4]
# *var1, var2 = lis1
# print(var1)
# print(var2)

# #UNPACKING
# lis1 = [1,2,3]
# lis2 = [4,5,6]
# lis3 = (*lis1, *lis2)
# print(lis3)

# dict1 = {'name':'Tylor', 'age': 150}
# dict2 = {'name':'Tylor', 'location': 'Accra'}
# dict3 = {**dict1, **dict2}
# print(dict3)

# FUCTION WITH ARGUMENTS AND KEYWORD ARGUMENTS
# POSITIONAL ARGUMENTS AND KEYWORD ARGUMENTS
# def explore(username, age = 10):
#     print(f'Name: {username} and Age: {age}')

# explore('Courage')
# def explore(age, username):
#     print(f'Name: {username} and Age: {age}')

# explore('Courage', 12)
# def explore(age= 10, username= 'Courage'):
#     print(f'Name: {username} and Age: {age}')

# explore(username='Courage', age= 12)

# def add(*args):
#   print(sum(args))

# add(10,3,1,3,4,5,7)

# def explore(*args, **kwargs):
#     print(args)
#     print(kwargs)

# explore('Courage', 12, hobby='coding', location = 'Accra')

##ASSIGNMENT1
# FUNCTION THAT CALCULATES YOUR BODY MASS INDEX(BMI)
# FUNCTION THAT MAKES CONVERSIONS FROM ONE UNIT TO ANOTHER(FROM-TO)
# EXAMPLE: 
#   conversion(100km -'m')
#   conversion(10c -'f')