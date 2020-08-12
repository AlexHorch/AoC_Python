with open("input.txt", "r") as file:
    lines, mm = file.read().split("\n\n")


def add_exchange(exchanges, line):
    a, b = line.split(" => ")
    if a in exchanges:
        exchanges[a].append(b)
    else:
        exchanges[a] = [b]


def parse_exchanges(lines):
    subs = {}
    for line in lines.split("\n"):
        add_exchange(subs, line)
    return subs


def applications(mm, subs):
    x = []
    for k, v in subs.items():
        idx = 0
        while k in mm[idx:]:
            i = mm.index(k, idx)
            for s in v:
                x.append(mm[:i] + s + mm[i+len(k):])
            idx = i+1
    return set(x)


def symbols(mm):
    return len(list(filter(lambda x: ord("A") <= ord(x) <= ord("Z"), mm)))


def steps(mm):
    return symbols(mm) - mm.count("Rn") - mm.count("Ar") - 2 * mm.count("Y") - 1


print(steps(mm))
