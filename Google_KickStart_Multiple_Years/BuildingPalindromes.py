# if there is more than one character has an odd count in the selected string then it cannot be a palindrome
# pass to the function the string and question indices 
f = open("/workspaces/70598009/BuildingPalindromes/building_palindromes_sample_ts1_input.txt", "rt")
y = int(f.readline())             #T
z = (f.readline().split())        #N, Q
x = (f.readline())                #String
x = list(x)
del x[-1]
print(x)
C = 0                               #number of palindroms in a single string
for i in range(z[1]):
    s = (f.readline().split())       # question string limits
    if if_palindrome(s, x) == True:
        C += 1



def if_palindrome(s, x):
    Q = x[s[0]:s[1]]                    # list of the question characters
    L = []                              # list of unique characters
    c1 = 0                              #counter for unique characters
    c2 = 0                              #counter for odd characters
    n = len(s[0],s[1])                  # length of the question's string
    for i in range(s[0],s[1]):
        if count(s[i]) = n:
            print("1")
            break
        elif count(s[i])%2 ==1:
            center = s[i]
            c2 +=1
            c1 = c1 + count(s[i])
            if s[i] in L:
                continue
            else:
                L.append(s[i])
                continue
            elif c2 > 1:
                print("0")
                break
            continue
        else:
            c1 = c1 + count([i])
            continue
    return c1















