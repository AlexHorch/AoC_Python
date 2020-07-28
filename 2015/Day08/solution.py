from puzzle_input import text, examples, lit, act


def actual_len(text):
    l = len(text) - 2
    i = 1
    while i < len(text)-2:
        if text[i] == '\\' and i+1 < len(text):
            if text[i+1] in ["\"", "\\"]:
                l -= 1
                i += 1
            if text[i+1] == "x":
                l -= 3
                i += 3
        i += 1
    return l


x = text.split("\n")[1:-1]

total = 0

for i in range(len(x)):
    total += len(x[i])
    total -= actual_len(x[i])

print(total)
