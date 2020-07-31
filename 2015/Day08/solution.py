from puzzle_input import text, examples, lit, act


def actual_len(text):
    copy = text[:]
    idx = copy.find(r"\x")
    while idx > 0:        
        copy = copy[:idx] + copy[idx+4:]
        idx = copy.find(r"\x")
    idx = copy.find(r"\\")
    while idx > 0:
        copy = copy[:idx] + copy[idx+2:]
        idx = copy.find(r"\\")
    idx = copy.find(r"\"")
    while idx > 0:
        copy = copy[:idx] + copy[idx+2:]
        idx = copy.find(r"\"")
    return len(copy)


x = """
"d\\gkbqo\\fwukyxab\"u"
""".split("\n")[1:-1]

total = 0

for i in range(len(x)):
    total += len(x[i])
    total -= actual_len(x[i])

print(total)
