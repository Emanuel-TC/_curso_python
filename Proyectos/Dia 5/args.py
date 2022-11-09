'''def suma(a,b):
     return a+b
print(suma(1,2,3)) '''

def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(1,2,3,5,6,7))

