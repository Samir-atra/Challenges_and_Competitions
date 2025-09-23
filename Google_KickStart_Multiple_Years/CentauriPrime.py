'''
# first create a function with a list as an input (the list will be the kingdom's name).
# then for each input, check it's last element, and according to the ruler's conditions assign the kingdom to
# the suitable ruler.
# print the output in the form needed.({name} is ruled by Bob) for example
import sys

def kingdom(name):    #now go for the list element where index = len-1
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
    Ys = ["y", "Y"]
    if name[-1] in Ys:
        return f"Case #{1}: {name} is ruled by nobody."
    elif name[-1] in vowels:
        return f"Case #{1}: {name} is ruled by Alice."
    elif name[-1] in consonants:
        print (f"Case #{1}: {name} is ruled by Bob.")



f = open("/workspaces/70598009/ts2_input.txt", "rt")
y = int(f.readline())
x = f.read().splitlines()
for names in x:
    for i in range (y):
        kingdom(names)
        continue
    continue

#x = kingdom("asasy")

x = int(input())
for i in range(x):
    y = input()
    kingdom(y)
    continue

if __name__ == '__main__':
  kingdom()

x = sys.stdin.readline()
for i in range(int(x)):
    y = sys.stdin.readline().strip()
    kingdom(y)
    continue
'''
# first create a function with a list as an input (the list will be the kingdom's name).
# then for each input, check it's last element, and according to the ruler's conditions assign the kingdom to
# the suitable ruler.
# print the output in the form needed.({name} is ruled by Bob) for example


def kingdom(name):    #now go for the list element where index = len-1
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]
    Ys = ["y", "Y"]
    if name[-1] in Ys:
        print(f"{name} is ruled by nobody")
    elif name[-1] in vowels:
        print(f"{name} is ruled by Alice")
    elif name[-1] in consonants:
        print(f"{name} is ruled by Bob")



f = open("/workspaces/70598009/ts2_input.txt", "rt")
x = f.read().splitlines()
for names in x:
    kingdom(names)
    continue







