
import random
# GENERATIORS AND GENERATOR EXPRESSION

gen_list = [1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
customers = [{"username":"Courage", "age":34,}, {"username":"Yusif", "age":31,}, {"username":"Jacinta", "age": 12}, {"username":"Selinam", "age":3}..............]
# FOR LOOP (DATA LOADED IN MEMORY FIRST BEFORE IT IS RETURNED)
# for i in gen_list:
#     print(i)

# GENERATOR (DATA IS RETURNED ONE AFTER THE OTHER)
# yield

# def normal_function():
#     for i in gen_list:
#         return i
    
#     
# while True:
#     print("a")

# for i in gen_list:
#     print(i)    

# def gen_function():
#     for i in gen_list:
#         yield i

# def gen_function():
#     while True:
#         yield random.randint(1,5)

# for v in gen_function():
#     print(v)


# GENERATOR EXPRESSION
gen_exs_list = [ i for i in range(1,5)]

gen = (i for i in 'dffdsfdsf')

for v in gen:
    print(v)