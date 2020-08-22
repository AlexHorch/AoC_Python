target = 36000000

houses = [11 for i in range(target//11)]

for i in range(2, len(houses)):
    j = i
    count = 0
    while j < len(houses) and count < 50:
        houses[j] += i * 11
        j += i
        count += 1

for i in range(len(houses)):
    if houses[i] >= target:
        print(i)
        break