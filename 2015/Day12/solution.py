import json

with open("input.txt", "r") as file:
    puzzle_input = file.read().split("\n")

puzzle_json = json.loads(puzzle_input)


def value_of(x):
    if dict == type(x):
        return object_value(x)
    if list == type(x):
        return list_value(x)
    if int == type(x):
        return x
    else:
        return 0


def object_value(o):
    sum = 0
    for v in o.values():
        if v == "red":
            return 0
        sum += value_of(v)
    return sum


def list_value(l):
    return sum([value_of(e) for e in l])


def numeric_value(txt):
    sum = 0
    idx = 0
    while idx < len(txt):
        if txt[idx] in "-1234567890":
            start = idx
            while idx + 1 < len(txt) and txt[idx+1] in "1234567890":
                idx += 1
            sum += int(txt[start:idx+1])
        idx += 1
    return sum


print(numeric_value(puzzle_input))
print(value_of(puzzle_json))
