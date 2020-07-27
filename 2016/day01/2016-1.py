x = 0
y = -1


def right():
    global x
    global y
    if (x == 0):
        if (y == 1):
            x = -1
            y = 0
        else:
            x = 1
            y = 0
    elif (x == 1):
        x = 0
        y = 1
    else:
        x = 0
        y = -1


def left():
    global x
    global y
    if (x == 0):
        if (y == 1):
            x = 1
            y = 0
        else:
            x = -1
            y = 0
    elif (x == 1):
        x = 0
        y = -1
    else:
        x = 0
        y = 1


a = 0
b = 0

route = input().split(", ")
visited = [[0, 0]]
for r in route:
    steps = int(r[1:])
    right() if r[0] == "R" else left()
    for i in range(steps):
        a += x
        b += y
        visited.append([a, b])

for i in range(len(visited)):
    point = visited[i]
    twice = point in visited[i+1:]
    if twice:
        print(abs(point[0]) + abs(point[1]))
        break

# L2, L5, L5, R5, L2, L4, R1, R1, L4, R2, R1, L1, L4, R1, L4, L4, R5, R3, R1, L1, R1, L5, L1, R5, L4, R2, L5, L3, L3, R3, L3, R4, R4, L2, L5, R1, R2, L2, L1, R3, R4, L193, R3, L5, R45, L1, R4, R79, L5, L5, R5, R1, L4, R3, R3, L4, R185, L5, L3, L1, R5, L2, R1, R3, R2, L3, L4, L2, R2, L3, L2, L2, L3, L5, R3, R4, L5, R1, R2, L2, R4, R3, L4, L3, L1, R3, R2, R1, R1, L3, R4, L5, R2, R1, R3, L3, L2, L2, R2, R1, R2, R3, L3, L3, R4, L4, R4, R4, R4, L3, L1, L2, R5, R2, R2, R2, L4, L3, L4, R4, L5, L4, R2, L4, L4, R4, R1, R5, L2, L4, L5, L3, L2, L4, L4, R3, L3, L4, R1, L2, R3, L2, R1, R2, R5, L4, L2, L1, L3, R2, R3, L2, L1, L5, L2, L1, R4