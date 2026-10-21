def helloMain(fx):   #=> decorator function
    print("Hi, !!!!")

    def helloMain2():   #=> wrapper function
        print("Hello from Child Before!")
        fx()
        print("Hello from Child After!")
    return helloMain2

@helloMain
def sayHello():
    print("Hello from Parent!")

#helloMain(sayHello)

# if __name__ == "main":
#     sayHello()