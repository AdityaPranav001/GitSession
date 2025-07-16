try:
    numbers = [10,20,30]
    index = int(input("Enter an index:"))
    print("Number at index", numbers[index])

except IndexError:
    print("Invalid Index! Please enter a valid index.")

except ValueError:
    print("Invalid Index! Please enter a number")

else:
    print("There is no error")
