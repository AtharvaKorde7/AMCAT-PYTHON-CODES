def outerFunction():
    print("This is the outer function")

    def innerFunction():
        print("This is the inner function")

    innerFunction()

outerFunction()