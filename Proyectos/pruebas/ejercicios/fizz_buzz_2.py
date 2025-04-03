for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz, multiplo de 3 y 5")
    elif i % 3 == 0:
        print("Fizz, multiplo de 3")
    elif i % 5 == 0:
        print("Buzz, mutiplo de 5")
    else:
        print(f"{i}\n")
    