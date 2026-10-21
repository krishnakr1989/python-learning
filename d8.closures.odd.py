#Closures are important because they let an inner function retain access to values 
# from an outer function even after the outer function has finished executing.

def calculate():
    n=-1
    def inner():
        nonlocal n
        n+=2
        return n
    return inner

odd=calculate()
print(odd())
print(odd())
print(odd())