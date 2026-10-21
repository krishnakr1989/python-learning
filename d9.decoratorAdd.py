def decorator(fx):
    def wrapper(*args, **kwargs):
        print("Hello from Child Before!")
        fx(*args, **kwargs)
        print("Hello from Child After!")
    return wrapper

@decorator
def add(x,y):
    print(x+y)

add(10,20)