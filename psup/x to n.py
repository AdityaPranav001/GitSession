x=int(input("enter base"))
n=int(input("enter power"))


def power_x(n):
    if n==0:
        return 1
    return x * power_x(n-1)

print(power_x(n))
