def parse_input(text):
    return [[1 if c == '#' else 0 for c in line] for line in text.split("\n")]


with open("input.txt", "r") as file:
    field = parse_input(file.read())


def state(field, i, j):
    size = len(field)
    return 0 if -1 in [i, j] or len(field) in [i, j] else field[i][j]


def next_state(field, i, j):
    last = len(field)-1
    tot = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == y == 0:
                continue
            tot += state(field, i+x, j+y)
    return [0, 1][tot == 3 or (field[i][j] and tot == 2) or (i in [0, last] and j in [0, last])]


def step(field):
    size = len(field)
    field2 = []
    for i in range(size):
        field2.append([])
        for j in range(size):
            field2[i].append(next_state(field, i, j))
    return field2


p = field
for i in range(100):
    p = step(p)
print(sum(map(sum, p)))
