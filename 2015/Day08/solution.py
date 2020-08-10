with open("input.txt", "r") as file:
    text = file.read().split("\n")


def mem_len(text):
    return len(eval(text))


def code_len(text):
    return len(text)


def rep_len(text):
    return len(repr(text)) + text.count('"')


def diff1(text):
    return sum([code_len(line) - mem_len(line) for line in text])


def diff2(text):
    return sum([rep_len(line) - code_len(line) for line in text])


print(diff1(text))
print(diff2(text))
