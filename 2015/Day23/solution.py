import re

with open("input.txt", "r") as file:
    program = file.read().split("\n")


def getState(pointer=0, a=0, b=0):
    return [pointer, {"a": a, "b": b}]


def compute(program, state):
    i = state[0]
    regs = state[1].copy()
    while i < len(program):
        inst = re.split(" |, ", program[i])
        if inst[0] == "inc":
            regs[inst[1]] += 1
            i += 1
        elif inst[0] == "hlf":
            regs[inst[1]] //= 2
            i += 1
        elif inst[0] == "tpl":
            regs[inst[1]] *= 3
            i += 1
        elif inst[0] == "jmp":
            i += int(inst[1])
        elif inst[0] == "jie":
            j = regs[inst[1]] % 2 == 0
            i += int(inst[2])*j + 1 * (not j)
        elif inst[0] == "jio":
            j = regs[inst[1]] == 1
            i += int(inst[2]) * j + 1 * (not j)
    return [i, regs]


print(compute(program, getState()))
print(compute(program, getState(a=1)))
