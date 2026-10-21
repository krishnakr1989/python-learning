# A decorator function takes a function as an argument and 
# returns a new function that adds some behavior before and 
# after the original function is called.


def greet(fx):
    #print("Hi, !!!!")

    def wrapper():
        print("Hello from Child Before!")
        fx()
        print("Hello from Child After!")
    return wrapper

@greet
def sayHello():
    print("Hello from Parent!")

# def sayHello():
#     print("Hello from Parent!")

# greet(sayHello)()
sayHello()

