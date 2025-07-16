n=-1
while n<0:
    n=int(input("enter a non negative integer"))

factorial =1

for i in range (1, n+1):
    factorial*=i

print("the factorial of ",n ,"is =", factorial)




