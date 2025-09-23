# track with length L
# machine starts from 0 step 1
# run total N 
# D run unites and C direction
# get the number of laps???
# T test cases
# L length of track, N NO. run times
# distance in units, C or A for the direction 

T = input().strip().split()
T = int(T[0])

def track_detail(case):
    L, N = input(f"Case #{case+1}: ").strip().split()
    L = int(L[0])
    N = int(N[0])
    return L, N

def step_counter(case):
    L, N = track_detail(case)
    steps = 0
    laps = 0
    direction = ""
    init = 0
    for run in range(N):
        D, C = input().strip().split()
        D = int(D)
        if init == 0:
            if C == "C" or C == "A":
                direction = C
                steps += D
                if D / L >= 1:
                    laps +=1
                    init += 1
                    continue
                else:
                    init += 1
                    continue
        elif init != 0 and C == direction:
            steps += D
            if steps / L >= 1:
                x = int(steps / L)
                laps = x
                continue
            else:
                continue
        elif init != 0 and C != direction:
            steps == 0
            direction = C
            if D / L >= 1:
                x = int(steps / L)
                laps = x
                continue
            else:
                continue
    return laps


for case in range (T):
    print(int(step_counter(case)))

