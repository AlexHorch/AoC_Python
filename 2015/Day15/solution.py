import math

with open('input.txt', 'r') as file:
    text = file.read().split("\n")


def parse_ingredient(text):
    parts = text.split(", ")
    return [int(p.split(" ")[-1]) for p in parts]


def total(ingredients, distribution):
    calories = sum([ingredients[i][4] * distribution[i] for i in range(len(distribution))])
    list = []
    for i in range(4):
        tot = 0
        for j in range(len(distribution)):
            tot += ingredients[j][i] * distribution[j]
        list.append(max(0, tot))
    return math.prod(list)


def distributions(length, total):
    if length == 1:
        yield (total,)
    else:
        for value in range(total+1):
            for permutation in distributions(length-1, total-value):
                yield (value,) + permutation


def optimal(text):
    ingredients = [parse_ingredient(line) for line in text]
    return max([total(ingredients, distribution) for distribution in list(distributions(len(ingredients), 100))])

def optimal_c(text, calories):
    ingredients = [parse_ingredient(line) for line in text]
    return max([total(ingredients, distribution) for distribution in list(distributions(len(ingredients), 100)) if sum([ingredients[i][4] * distribution[i] for i in range(len(distribution))]) == calories])

print(optimal(text))
print(optimal_c(text, 500))