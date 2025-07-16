balance=int(input("enter balance:"))
withdraw=int(input("enter withdrawl amount:"))


ld=withdraw%10
lsd=(withdraw//10)%10



if ld!=0 and lsd !=0:
    print("invalid")
elif balance<withdraw and withdraw<=0:
    print("invalid")
else:
    print("remaining balance=", balance-withdraw)


