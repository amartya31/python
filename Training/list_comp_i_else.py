temps = [223,231,-123,423,782] #temp stroed as whole 
temp1 = [ temp / 10 for temp in temps ]
print(" The values are: {} ".format(temp1))

temp2 = [ temp / 10 for temp in temps if temp > 0 ]
print(" The values are: {} ".format(temp2))

temp3 = [ temp / 10  if temp > 0 else 0 for temp in temps] #note the for side 
print(" The values are: {} ".format(temp3))