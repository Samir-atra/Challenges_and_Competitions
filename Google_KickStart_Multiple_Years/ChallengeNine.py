#first number is the loop length, and then put a loop that type a digit and find
#modulo of three if zero then we have what we are looking for.
#now start by creating a function that type the test digits and find modulo.

def number(T, num):    #function with the number as an input.
    for i in range (9):
        if int(str(num)+str(i))%9 == 0:
            break
    for i in range (9):
        if int(str(i)+str(num))%9 == 0:
            break
    if int(str(num)+str(i)) > int(str(i)+str(num)):
        x = int(str(i)+str(num))
    else:
        x = int(str(num)+str(i))
    return x



f = open("/workspaces/70598009/ChallengeNine/ts1_input.txt", "rt")
T = int(f.readline())
for l in range (T):
    num = int(f.readline())

    y = number(T, num)
    print(f"Case #{l+1}: {y}")


