import time
import os
import pandas 


if os.path.exists("/Users/amartyaghosh/Code/python/fruits.txt") == True:
    with open("/Users/amartyaghosh/Code/python/temps.csv") as file :
        data = pandas.read_csv("/Users/amartyaghosh/Code/python/temps.csv")
        print(file.read())
        print("NOW PANDA OUTPUT ")
        print(data)
        print("NOW PANDA MEAN OUTPUT ")
        print(data.mean() )
else:
    print("File doesn't exist")
#time.sleep(10)
#break