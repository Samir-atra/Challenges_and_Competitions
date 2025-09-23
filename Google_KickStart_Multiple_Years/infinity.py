# 1get R, A, B, draw a circle with it.
# 2multiply last radius by A, draw a circle with it.
# 3divide last radius by B, draw a circle with it.
# 4repeat 2&3 until the radius = zero

x = open("/home/samer/Documents/Programming/KickStart/InfinityArea/infinity_area_sample_ts1_input.txt","rt")
f = x.readline().split()

def draw_circle(thingy):
    R = thingy[0]
    A = thingy[1]
    B = thingy[2]
    radius = R
    circle = 3.14 * radius * radius
    print(circle)
    while radius !=0:
        radius = radius * A
        circle = 3.14 * radius * radius
        yield circle
        radius = radius // B
        circle = 3.14 * radius * radius
        yield circle



for i in range (len(f)):
    case = list(x.readline().split())
    l = []
    c = draw_circle(case)
    l.append(c)
sum = 0
for j in range (len(l)):
    sum = sum + l[j]
print (f"case #{i+1}: {sum}")




