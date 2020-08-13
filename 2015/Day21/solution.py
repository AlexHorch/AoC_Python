def parseEquipment(line):
    return list(map(int, line.split(" ")))


weapons = list(map(parseEquipment, open(
    "weapons.txt", "r").read().split("\n")))
armors = list(map(parseEquipment, open("armors.txt", "r").read().split("\n")))
rings = list(map(parseEquipment, open("rings.txt", "r").read().split("\n")))

boss = [103, 9, 2]


def permutations(length):
    if length == 1:
        yield (0,)
        yield (1,)
    else:
        for value in [0, 1]:
            for permutation in permutations(length-1):
                yield (value,) + permutation


rcs = []

for p in permutations(6):
    if sum(p) < 3:
        rcs.append([0, 0, 0])
        for i in range(len(p)):
            rcs[-1][0] += p[i] * rings[i][0]
            rcs[-1][1] += p[i] * rings[i][1]
            rcs[-1][2] += p[i] * rings[i][2]

acs = [[0, 0, 0]]
for i in range(5):
    acs.append([armors[i][0], 0, armors[i][1]])

wcs = []
for i in range(5):
    wcs.append([weapons[i][0], weapons[i][1], 0])

stats = []
for r in rcs:
    for a in acs:
        for w in wcs:
            stats.append([r[0]+a[0]+w[0], r[1]+a[1]+w[1], r[2]+a[2]+w[2]])

base = [100]


def victory(player, boss):
    php = player[0]
    bhp = boss[0]
    pt = True
    while php > 0 and bhp > 0:
        if pt:
            bhp -= max(0, player[1] - boss[2])
        else:
            php -= max(0, boss[1] - player[2])
        pt = not pt
    return php > bhp


min_cost = 1000

for s in stats:
    if victory(base + s[1:], boss):
        min_cost = min(min_cost, s[0])

print(min_cost)

max_cost = 0

for s in stats:
    if not victory(base + s[1:], boss):
        max_cost = max(max_cost, s[0])

print(max_cost)
