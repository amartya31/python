def foo(*args):
    print(type(args))
    return (args)

def foo1(**kargs):
    print(type(kargs))
    return(kargs)

print(foo(1,2,3))

print(foo1(a = 1,b = 2,c = 3))