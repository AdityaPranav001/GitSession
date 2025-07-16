num1 = int(input("Enter the numerator:"))
num2 = int(input("Enter the denominator"))

try:
    value = num1/num2
    print(value)

except ZeroDivisionError:
    print("You litteraly tried to divide by zero, like who are you bro?")
