from puzzle_input import text
compressed = text
uncompressed = ""


idx = 0
while idx < len(compressed):
    if compressed[idx] != "(":
        uncompressed += compressed[idx]
        idx += 1
    else:
        end = compressed[idx:].index(")") + idx
        (length, times) = map(int, compressed[idx+1:end].split("x"))
        uncompressed += compressed[end+1: end+length+1] * times
        idx = end+length+1

print(len(uncompressed))