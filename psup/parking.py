while True:
    hours= int (input("enter the no. of hours parked:"))
    if hours>0:
        break
    print("invalid input. please enter a valid number of hours:")

if hours<=2:
    fee=0
else:
    fee=(hours-2)*5

print(f"total parking fee:", fee)


