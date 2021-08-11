import time
import os

while True :
    if os.path.exists("/Users/amartyaghosh/Code/python/fruits.txt") == True:
        with open("/Users/amartyaghosh/Code/python/fruits.txt") as file :
            print(file.read())
    else:
        print("File doesn't exist")
    time.sleep(10)
    break