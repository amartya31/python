temps = [223,231,423,782] #temp stroed as whole 
temp1 = []
for temp in temps :
    temp1.append(temp / 10)

print(temp1)

#now to use the whole thing in a single line , list comprehension 

temp2 = [ temp / 10 for temp in temps ]
print(" The values are: {} ".format(temp2))