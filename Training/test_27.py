def foo(temp):
    if(temp > 25):
        return ('Hot')
    elif(temp >= 15 and temp <= 25):
        return('Warm')
    else:
        return('Cold')

print(foo(10))
print(foo(15))
print(foo(26))