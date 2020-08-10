import re

scan = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0,
        "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

with open("input.txt", "r") as file:
    aunts = file.read().split("\n")

"""Sue 1: goldfish: 6, trees: 9, akitas: 0"""


def parse_aunt(line):
    global scan
    parts = re.split(': |, ', line)
    line.split(" ")
    if all(map(lambda pair: scan[parts[pair[0]]] == int(parts[pair[1]]), [[1, 2], [3, 4], [5, 6]])):
        print(parts[0])


for i in range(len(aunts)):
    parse_aunt(aunts[i])
