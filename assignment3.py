
# ASSIGNMENT-3
# Using file handling, create a program that take inputs and stores in a data.txt and output it's content on a new line each.
name = open("assignment3.txt", "w")
name.write(input("What is your name?: "))
name.write(input("How old are you?: "))
name.write(input("Email address: "))
name.write(input("Contact: "))
name.write(input("Location: "))
name.close()


name = open("assignment3.txt", "r")

print(name.read())










