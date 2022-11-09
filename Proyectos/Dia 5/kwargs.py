'''def suma(**kwargs):
    #print(type(kwargs))
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total
print(suma(a=1, b=2, c=3, d=4)) '''

def prueba(num_uno,num_dos,*args,**kwargs):
    print(f"El primer valor es {num_uno}")
    print(f"El segundo valor es {num_dos}")
    for arg in args:
        print(f"arg = {arg}")
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

args =[1,2,3,4,5,6,7,8,9,10]
kwargs ={"a":1,"b":2,}

prueba(1,2,*args,**kwargs)
