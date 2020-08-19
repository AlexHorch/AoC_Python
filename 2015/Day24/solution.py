with open("input.txt", "r") as file:
    packages = list(map(int, file.read().split("\n")))[::-1]


def permutations(prev, idx, packages, goal):
    if prev == goal:
        return ()
    for i in range(idx, len(packages)):
        n = packages[i]
        if prev + n <= goal:
            yield (n,) + permutations(prev + n, i, packages,  goal)


def combinations(packages):
    goal = sum(packages) // 3
    x = set([sorted(p) for p in permutations(0, 0, packages,  goal)])
    return x


for c in combinations([1, 2, 3, 4, 5]):
    print(list(c))
