text = open("input.txt", "r").read().split("\n")


def cs(id):
    counts = [0] * 26
    for c in id:
        counts[ord(c) - ord("a")] += 1
    return any(map(lambda x: x == 2, counts)), any(map(lambda x: x == 3, counts))

twos = 0
threes = 0
for line in text:
    x,y = cs(line)
    twos += x
    threes += y

print(twos * threes)

def comp(l, o):
    count = 0
    for i in range(len(l)):
        if not l[i] == o[i]:
            count += 1
    return count


for i in range(len(text)):
    l = text[i]
    for o in text[i+1:]:
        if comp(l,o) == 1:
            print(l,o)
