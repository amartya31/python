# Tuple is same as List 
#Tuple are not Mutable i.e. can not be appended 
#List are Mutable i.e. can be appended 

a = [1,2,3]
b = (1,2,3)
#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__',
#  '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', 
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__',
#  '__str__', '__subclasshook__', 'count', 'index']

print(a)
print(b)
a.append(4)
print(a)
print(b)
#b.append(4)
#File "/Users/amartyaghosh/Code/python/tuple_3_22.py", line 18, in <module>
#    b.append(4)
#AttributeError: 'tuple' object has no attribute 'append'