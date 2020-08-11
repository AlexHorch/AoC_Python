with open("input.txt", "r") as file:
    sizes = list(map(int, file.read().split("\n")))


def permutations(length):
    if length == 1:
        yield (0,)
        yield (1,)
    else:
        for value in [0, 1]:
            for permutation in permutations(length-1):
                yield (value,) + permutation

hit = [0 for n in range(21)]

for permutation in permutations(len(sizes)):
    tot = 0
    for i in range(len(permutation)):
        tot += permutation[i] * sizes[i]
    if tot == 150:
        hit[sum(permutation)] += 1

print(hit)
