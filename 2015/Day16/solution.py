import re

scan = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0,
        "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

with open("input.txt", "r") as file:
    aunts = file.read().split("\n")

"""Sue 1: goldfish: 6, trees: 9, akitas: 0"""


def parse_aunt(line):
    global scan
    parts = re.split(': |, ', line)
    if all(map(lambda pair: scan[parts[pair[0]]] == int(parts[pair[1]]), [[1, 2], [3, 4], [5, 6]])):
        print(parts[0])


def parse_aunt_correct(line):
    global scan
    parts = re.split(': |, ', line)
    if "cats" in parts:
        if not scan["cats"] < int(parts[parts.index("cats")+1]):
            return
    if "trees" in parts:
        if not scan["trees"] < int(parts[parts.index("trees")+1]):
            return
    if "pomeranians" in parts:
        if not scan["pomeranians"] > int(parts[parts.index("pomeranians")+1]):
            return
    if "goldfish" in parts:
        if not scan["goldfish"] > int(parts[parts.index("goldfish")+1]):
            return
    for i in [1,3,5]:
        if parts[i] not in ["cats", "trees", "pomeranians", "goldfish"]:
            if not scan[parts[i]] == int(parts[i+1]):
                return
    print(parts[0])


for i in range(len(aunts)):
    parse_aunt(aunts[i])
    parse_aunt_correct(aunts[i])
