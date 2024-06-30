# FILE I/O
# INPUT(WRITE, APPEND)
# using write(w)
# write_file_Handle = open("try.txt", "w")
# write_file_Handle.write("This is a new file ")
# write_file_Handle.write("this is another text")
# write_file_Handle.close()

# write_file_Handle = open("try.txt", "r")
# print(write_file_Handle.read())

# # using append(a)
# append_file_Handling = open("try.txt", "a")
# append_file_Handling.write("\njust adding this one")
# append_file_Handling.close()

# append_file_Handling = open("try.txt", "r")
# print(append_file_Handling.read())

# # using create(x)
# create_file_Handling = open("try2.txt", "x")
# create_file_Handling.write("Creating a new file from here")
# create_file_Handling.close()

# create_file_Handling = open("try2.txt", "r")
# print(create_file_Handling.read())

# # using delete (remove)
# import os
# os.remove("try2.txt")

# using new lines (readlines())
newlines_file_Handling = open("try.txt", "w")
newlines_file_Handling.writelines(["ONE", "TWI","THREE"])
newlines_file_Handling.close()

newlines_file_Handling = open("try.txt", "r")
for x in newlines_file_Handling:
    print(x)


# OUTPUT(READ)
# TEXT(PDF,DOC,DOCXT,TXT)






# QUIZ
# Using python file handling, create a data.txt file with 'my name is <your name>' as it's content