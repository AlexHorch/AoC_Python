from puzzle_input import text, decoded


def ind(x, l, indices):
    i = l.index(x)
    while(i in indices):
        i += l[i+1:].index(x)+1
    return i


def generateCheck(os):
    top5 = sorted(os, reverse=True)[:5]

    indices = []
    for o in top5:
        indices.append(ind(o, os, indices))

    return "".join(map(lambda i: str(chr(i+97)), indices))


def occurences(text):
    os = [0]*26
    for c in text:
        os[ord(c)-97] += 1
    return os


def extract(line):
    parts = line.split("-")
    text = "".join(parts[:-1])
    last = parts[-1]
    check = last[-6:-1]
    dep = int(line[-10:-7])
    return (parts[:-1], text, check, dep)


def department(line):
    (parts, text, check, dep) = extract(line)

    os = occurences(text)

    return dep if check == generateCheck(os) else 0


def shift(c, dep):
    return chr(((ord(c)-ord('a')+dep) % 26)+ord('a'))


def decipher(line):
    (parts, text, check, dep) = extract(line)
    return " ".join(["".join(map(lambda c: shift(c, dep), part)) for part in parts])


total = 0

for line in text:
    dep = department(line)
    if dep > 0:
        print(decipher(line), dep)
        total += dep

print(total)


for l in decoded:
    if "north" in l:
        print(l)
