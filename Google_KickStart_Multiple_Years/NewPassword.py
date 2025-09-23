f = open("/home/samer/Documents/Programming/KickStart/NewPassword/new_password_sample_ts1_input.txt","rt")
T = int(f.readline())
def main():
    p = []
    for i in range(T):
        c = f.readline()
        p = f.readline()
        l = check(p, c, islower())
        if l == False:
            p.append("a")
        u = check(p, c, isupper)
        if u == False:
            p.append("A")
        d = check(p, c, isdigit)
        if d == False:
            p.append("1")
        s = character(p, c)
        if s == False:
            p.append("@")
        if len(p) < 7:
            p.append("a"*7-len(p))

def check(p, c, case):
    for i in range(c):
        z = p[i].case()
        if z == False:
            break
        return False 

def character(p, c):
    ch = ["#","@","*","&"]
    for i in range(len(c)):
        for j in range(len(ch)):
            if p[i] == ch[j]:
                break
                return True
            else:
                continue
    return False
            
main()    