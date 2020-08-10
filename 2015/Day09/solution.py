with open("input.txt", "r") as file:
    text = file.read()


class City:
    def __init__(self, name):
        self.name = name
        self.destinations = {}

    def add_destination(self, destination, distance):
        self.destinations[destination] = distance

    def shortest(self, visited):
        if len(self.destinations) + 1 == len(visited):
            return 0
        return min([k.shortest(visited + [k.name]) + v for k, v in self.destinations.items() if k.name not in visited])

    def longest(self, visited):
        if len(self.destinations) + 1 == len(visited):
            return 0
        return max([k.longest(visited + [k.name]) + v for k, v in self.destinations.items() if k.name not in visited])


def prep(txt):
    cs = {}
    for line in txt.split("\n"):
        words = line.split(" ")
        a = words[0]
        b = words[2]
        d = int(words[4])
        if a not in cs.keys():
            cs[a] = City(a)
        if b not in cs.keys():
            cs[b] = City(b)
        cs[a].add_destination(cs[b], d)
        cs[b].add_destination(cs[a], d)
    return cs

def shortest(txt):
    cs = prep(txt)
    return min([c.shortest([c.name]) for c in cs.values()])

def longest(txt):
    cs = prep(txt)
    return max([c.longest([c.name]) for c in cs.values()])

print(shortest(text))
print(longest(text))