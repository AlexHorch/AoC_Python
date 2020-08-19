with open("input.txt", "r") as file:
    packages = list(map(int, file.read().split("\n")))[::-1]


def permutations(prev, idx, packages, goal):
    if prev == goal:
        yield ()
    for i in range(idx, len(packages)):
        n = packages[i]
        if prev + n <= goal:
            for p in permutations(prev + n, i+1, packages,  goal):
                yield (n,) + p


def combinations(packages):
    goal = sum(packages) // 4
    x = set([p for p in permutations(0, 0, packages,  goal)])
    return x


count = 28
qe = 10000000000000000

for c in combinations(packages):
    if len(c) <= count:
        count = len(c)
        q = 1
        for x in c:
            q *= x
        if q <= qe:
            qe = q

print(count, qe)
