def meanOfNumbers(val):
    if type(val) == dict:
        mean = sum(val.values()) / len(val)
    elif type(val) == str:
        mean = len(val)
    else:
        mean = sum(val)/ len(val)
    return mean

val = [1,2,3,4]
print('The mean is ',meanOfNumbers(val))
val = {'a':1,'b':2,'c':3}
print('The mean of dict is = ',meanOfNumbers(val))
print('The mean of dict is = ',meanOfNumbers("HELLO"))
