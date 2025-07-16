credit=int(input("enter credit sscore:"))
income=int(input("enter income:"))
debt=int(input("enter current debts:"))



if income<=50000:
    if credit<=700:
        print("loan cant be approved due to low credit score")
    elif debt>=20000:
        print("loan cant be approved due to high debts")
    else:
        print("loan can be approved")
else:
    print("loan cant be approved")

