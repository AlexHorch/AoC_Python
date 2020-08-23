jumps = [int(line) for line in open("input.txt", "r").read().split("\n")]
f = 0
fs = {0}
found = False
while not found:
    for jump in jumps:
        f += jump
        if not found and f in fs:
            print(f)
            found = True
        fs.add(f)
print(len(fs) == len(set(fs)))
print(f)
