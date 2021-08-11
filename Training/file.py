file = open("/Users/amartyaghosh/Code/python/fruits.txt")

content = file.read()
print(content)

file.close()

#indent the code of file 

with open("/Users/amartyaghosh/Code/python/fruits.txt") as file1:
    content = file1.read()
    #here file is closed automatically 

print("The content of the file \n{}".format(content))