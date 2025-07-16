initial_deposit=float(input("enter initial deposit amount:"))
interest=0.5
years=int(input("enter the total no. of year"))

balance=initial_deposit

print("initial balance=", balance)
for i in range(years):
    balance+=initial_deposit*interest
print("new balance=", balance)



