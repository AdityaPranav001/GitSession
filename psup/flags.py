keep_running= True
while keep_running:
    user_input=input("do u wnt to cntinue? yes or no").lower()

if user_input == "no":
    keep_running= False

    print("loop has ended:")

else:
    print("loop again")