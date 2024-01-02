lista = list(range(1,101))
for i in lista:
    if (i%3==0) and (i%5==0):
        print(i)
        print("fizzbuzz")
    elif i%3==0:
        print(i)
        print("fizz")
    elif i%5==0:
        print(i)
        print("buzz")
    else:
        pass
