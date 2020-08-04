old = "hepxcrrq"


def abc(c):
    return chr(ord(c)+1)


def next(pw, idx):
    if idx < 0:
        raise Exception("something went wrong")
    c = pw[idx]
    if c == "z":
        return next(pw[:idx]+"a"+pw[idx+1:], idx-1)
    return pw[:idx]+abc(c)+pw[idx+1:]

alphabet = "abcdefghijklmnopqrstuvwxyz"
combinations = [alphabet[i:i+3] for i in range(len(alphabet)-2)]
pairs = [alphabet[i]*2 for i in range(len(alphabet))]

print(combinations)
print(pairs)

def valid(pw):
    if "i" in pw or "l" in pw or "o" in pw:
        return False    
    if any(map(lambda c: c in pw, combinations)):
        for p1 in pairs:
            if p1 in pw:
                idx = pw.index(p1)
                for p2 in pairs:
                    if p2 in pw[idx+2:]:
                        return True
    return False

pw = old    
while not valid(pw):
    pw = next(pw, 7)
print(pw)

pw = next(pw, 7)
while not valid(pw):
    pw = next(pw, 7)
print(pw)