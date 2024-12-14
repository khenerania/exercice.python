nombre=int(input("donner un nombre:\n"))
if(nombre%3==0 and nombre%5==0):
    print("FizzBuzz\n")
else:
    if(nombre%3==0):
        print("Fizz\n")
    else:
        print("Buzz\n")