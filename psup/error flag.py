error_flag = False

try:
    result=10/0
except ZeroDivisionError:
    error_flag = True


if error_flag:
    print("an error occured handleing it")