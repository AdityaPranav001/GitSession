n=int(input("enter the no. disks"))

def tower_of_hanio(n , s, a, t):
    if n == 1:
        return print(f"move one disk from {s} to {t}")
    tower_of_hanio(n-1, s, t, a)
    print(f"move  disk {n} from {s} to {a}")
    tower_of_hanio(n-1, a, s, t)
    print(f"move  disk {n} from {a} to {s}")

tower_of_hanio(n ,'A', 'B', 'C')

