
def main():
    x = int(input("# of case = "))
    for i in range (x):
        y = int(input("# of cells = "))
        c = 0
        for j in range (y+1):
            if j == 0:
                c += 1
            elif j % 4 == 0:
                c += 1
            else:
                continue
        print(f"Case #{i+1}:",c)

main()


