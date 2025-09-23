# N is the number of days of the competition
# M is the total number of participants
# get the daily score needed for last year to win the competition
# P last years ID
# Si,j is the step count of the ith person on the jth day of competition


import numpy as np

# f = open("/workspaces/70598009/Walktober/ts1_input.txt", "rt")
T = input().strip().split()
T = int(T[0])

walker_beedoo = "beedoo beedoo"


def score_creator(M, N):
    A = np.zeros((M, N))

    for player in range(M):
        walker = list(input().strip().split())
        for day in range(N):
            A[player][day] = walker[day]
    return A


def counter(M, N, P, A):
    DOut = 0
    John = A[P - 1]
    for day in range(len(John)):
        biggest = 0
        for walker in range(M):
            if John[day] >= A[walker][day]:
                continue
            elif John[day] < A[walker][day]:
                diff = A[walker][day] - John[day]
                # print(diff, "=", A[walker][day], "-", John[day])
                if diff > 0 and diff > biggest:
                    biggest = diff
                else:
                    continue
        # print("biggest = ", biggest)
        DOut += biggest

    return DOut


def main(T):
    for case in range(T):
        M, N, P = input(f"Case #{case+1}: ").strip().split()

        M = int(M)
        N = int(N)
        P = int(P)

        A = score_creator(M, N)
        add_steps = counter(M, N, P, A)

        print(int(add_steps))


main(T)


# WORKS
