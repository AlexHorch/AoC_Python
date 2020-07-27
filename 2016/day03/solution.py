from puzzle_input import text
import re


numbers = [[int(t) for t in re.split(r' +', line.strip())] for line in text]


def possible(a, b, c):
    return a+b > c and b+c > a and a+c > b


horizontal_count = 0

for l in numbers:
    if possible(*l):
        horizontal_count += 1


vertical_count = 0

for i in range(len(numbers)//3):
    for j in range(3):
        if possible(*[numbers[i*3+n][j] for n in range(3)]): vertical_count += 1

print("horizontal:", horizontal_count)
print("vertical:", vertical_count)
