# DICTIONARY COMPREHENSION
# lis = [num for num in range(1, 6)]
# print(lis)
# CHALLENGE
# CREATE DICTIONARY OF KEY, VALUE PAIRS AS NUM:NUM*2 IN THE RANGE OF 1 - 5
# dict1 = {num : num*2 for num in range(1 , 5)}
# print(dict1)
lis1 = ("name", "age", "hobby", "profession")
lis2 = ("Courage", 20, "coding", "student")

dictionary = {"name" :"Courage", "age": 20, "hobby": "coding", "profession": "student"}
classages = {"Courage" :32, "Jacinta": 20, "Selinam": 16, "Yusif": 12}

# dictionary = {key:value for (key, value) in dictionary.items() if/else condition.....}
# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.items())
# print(classages.keys())
# print(classages.values())
# print(classages.items())
# dict2 = {key:value for (key, value) in classages.items()}
# print(dict2)
# dict1 = {key:value for (key, value) in dictionary.items() if "e" in key}
# dict2 = {key:value for (key, value) in classages.items() if value > 5 and value < 15}
# print(dict1)
# print(dict2)
# zip1 = dict(zip(lis1, lis2))
# dict2 = {key:value for (key, value) in zip1.items()}
# print(zip1)
# print(dict2)


evenOdd = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# {"a": "odd", "b": "even", "c": "odd", "d": "even", "e": "odd"}
dict1 = {x: "even" if y%2 == 0 else "odd" for (x, y) in evenOdd.items()}
print(dict1)

# SET COMPREHENSION