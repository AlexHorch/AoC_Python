from puzzle_input import maze_small, maze_medium, maze_actual


class Portal:
    def __init__(self, a, b):
        self.coordinates = [a, b]


class Field:
    def __init__(self):
        self.neighbours = []
        self.distance = -1

    def append(self, neighbor):
        self.neighbours.append(neighbor)

    def spread(self):
        if self.distance > -1:
            for neighbour in self.neighbours:
                if neighbour.distance > self.distance + 1 or neighbour.distance == -1:
                    neighbour.distance = self.distance + 1


def find_size(text, n):
    return find_size(text, n+1) if text[n][n] in "#." else n-2


text = maze_small.split("\n")
size = find_size(text, 2)

fields = {}


def total_distances():
    global fields
    return sum(map(lambda f: f.distance, fields.values()))


start = ""
end = ""


for i in range(len(text)):
    for j in range(len(text[i])):
        c = text[i][j]
        if c == ".":
            fields[f"{i},{j}"] = Field()
        elif c != "#":
            (x, y) = find_partner(i, j)
            d = text[x][y]


fields["2,9"].distance = 0

for x, y in fields.items():
    (a, b) = map(int, x.split(","))
    for s in [f"{a+1},{b}", f"{a-1},{b}", f"{a},{b+1}", f"{a},{b-1}"]:
        if s in fields:
            y.append(fields[s])

print(total_distances())

p = 0
s = total_distances()

while p != s:
    p = s
    for f in fields.values():
        f.spread()
    s = s = total_distances()

print(total_distances())
print(fields["16,13"].distance)
