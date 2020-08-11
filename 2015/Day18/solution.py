def parse_input(text):
    return [[1 if c == '#' else 0 for c in line] for line in text.split("\n")]


with open("input.txt", "r") as file:
    field = parse_input(file.read())


def state(field, i, j):
    return 0 if -1 in [i, j] or len(field) in [i, j] else field[i][j]


def next_state(field, i, j):
    tot = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == y == 0:
                continue
            tot += state(field, i, j)
    return [0, 1][tot == 3 or (field[i][j] and tot == 2)]


def step(field):
    size = len(field)
    field2 = []
    for i in range(size):
        field2.append([0]*size)
    for i in range(size):
        for j in range(size):
            field2[i][j] = next_state(field, i, j)
    return field2
