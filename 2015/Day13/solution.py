from puzzle import small, actual


def size(lines):
    i = 1
    while i * i - i != len(lines):
        i += i
    return i


def getGuests(lines):
    s = size(lines)
    guests = {}
    for i in range(s):
        guest = {}
        for j in range(s - 1):
            arrangement = lines[i * (s - 1) + j].split(" ")
            guest[arrangement[10][:-1]
                  ] = int(arrangement[3]) * (1 if arrangement[2] == "gain" else -1)
        guests[lines[i * (s - 1)].split(" ")[0]] = guest
    return guests


def happy(guests, a, b):
    return guests[a][b] + guests[b][a]


def arrange_guests(guests, seated):
    if len(seated) == len(guests):
        return 0 # you sit at the table
        #return happy(guests, seated[0], seated[-1]) # you don't sit at the table
    values = []
    if len(seated):
        last = guests[seated[-1]]
        for k, v in last.items():
            if k not in seated:
                values.append(arrange_guests(
                    guests, seated[:] + [k]) + happy(guests, seated[-1], k))
    else:
        for k, v in guests.items():
            values.append(arrange_guests(guests, [k]))

    return max(values)


guests = getGuests(actual)

print(arrange_guests(guests, []))
