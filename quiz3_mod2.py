# Quiz-3
# Using python file handling. Create a data.txt file with 'my name is <your name>' as it's content

x = open("data.txt", "a")
x.write("my name is courage ")
x.close()

x = open("data.txt")
print(x.read())