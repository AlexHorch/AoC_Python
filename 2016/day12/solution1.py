from puzzle_input import text

registers = {"a": 0, "b": 0, "c": 0, "d": 0}

idx = 0

val = lambda x: int(x) if x.isdigit() or x[1:].isdigit() else registers[x]
        

while (idx < len(text)):
    line = text[idx].split(" ")
    if "cpy" == line[0]:
        registers[line[2]] = val(line[1])
    elif "inc" == line[0]:
        registers[line[1]] += 1
    elif "dec" == line[0]:
        registers[line[1]] -= 1
    else:
        if val(line[1]) != 0:
            idx += val(line[2])
            continue
    idx += 1

print(registers["a"])