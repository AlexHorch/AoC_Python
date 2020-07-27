from puzzle_input import text

instructions = text.split("\n")

it = 5

def to_code(values):
    return "".join(map(lambda i: {10:"A", 11:"B", 12:"C", 13:"D"}[i]  if i > 9 else str(i), values))

def mf(arr):
    global it
    it = arr[it]


def u(): return mf([0, 1, 2, 3, 1, 2, 3, 4, 5, 6])
def d(): return mf([0, 4, 5, 6, 7, 8, 9, 7, 8, 9])
def l(): return mf([0, 1, 1, 2, 4, 4, 5, 7, 7, 8])
def r(): return mf([0, 2, 3, 3, 5, 6, 6, 8, 9, 9])


def crack(label):
    global it
    it = 5
    buttons = []
    for line in instructions:
        fun = {"U": u, "L": l, "D": d, "R": r}
        for c in line:
            fun[c]()
        buttons.append(it)
    print(label, ":", to_code(buttons))


crack("1 - 9")


def u(): return mf([0, 1, 2, 1, 4, 5, 2, 3, 4, 9, 6, 7, 8, 11])
def d(): return mf([0, 3, 6, 7, 8, 5, 10, 11, 12, 9, 10, 13, 12, 13])
def l(): return mf([0, 1, 3, 4, 4, 6, 7, 8, 9, 9, 11, 12, 12, 13])
def r(): return mf([0, 1, 2, 2, 3, 5, 5, 6, 7, 8, 10, 10, 11, 13])


crack("1 - D")
