from puzzle_input import row, column, first, factor, modulo

current = first

diagonal = row + column - 1
n = sum(range(diagonal+1)) + column-1

def next():
    global current
    current = (current * factor) % modulo

for i in range(n):
    next()

print(current)