def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)
print(factorial(5))





def printFun(test):
    if (test<1):
        return
    else:
        print(test, end="")
        printFun(test-1)
        print(test, end="")
        return
    
test = 3
printFun(test)




