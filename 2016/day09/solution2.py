from puzzle_input import text, short, very_short


def decompressed_length(text):
    length = 0
    weights = [1]*len(text)
    i = 0
    while i < len(text):
        if text[i] == "(":
            end = text[i:].find(")") + i
            (a, b) = map(int, text[i+1:end].split("x"))
            for j in range(a):
                weights[end + j + 1] *= b
            i = end + 1
        else:
            length += weights[i]
            i += 1
    return length


print(decompressed_length(text))
