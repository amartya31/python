with open("/Users/amartyaghosh/Code/python/fruits.txt","a+") as file:
    file.write("{}".format("\nmango"))
    file.seek(0)
    contents = file.read()

print(contents)