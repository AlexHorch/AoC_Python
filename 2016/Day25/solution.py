from puzzle_input import row, column, first, factor, modulo

current = first


def next():
    global current
    current = (current * factor) % modulo

for i in range(18343669):
    next()

print(current)