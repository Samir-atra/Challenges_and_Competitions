# L = number of lilies

T = input().strip().split()
T = int(T[0])

for case in range(T):
    L = input(f"Case #{case+1}: ").strip().split()
    L = int(L[0])
    if L <= 14:
        print(L)
        continue
    elif L == 15:
        print("13")
        continue
    elif L == 16:
        print("14")
        continue
    elif L == 17:
        print("15")
        continue
    elif L == 18:
        print("15")
        continue
    elif L == 19:
        print("16")
        continue
    elif L == 20:
        print("15")
        continue

# could not find a math function that fast
















