n=int(input("enter"))

def sum_n(n):
    if n==0:
        return 0
    return n + sum_n(n-1)

print(sum_n(n))



