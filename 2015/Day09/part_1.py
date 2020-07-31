from puzzle_input import txt, example, example_result


def get_nth_word(txt, n):
    return txt.split(" ")[n]


def nth_word_each_line(txt, n):
    return list(map(lambda c: get_nth_word(c, n), txt.split("\n")))


def place_names(txt):
    return sorted(set(nth_word_each_line(txt, 0) + nth_word_each_line(txt, 2)))

places = {}
for line in txt.split("\n"):
    words = line.split(" ")
    a = words[0]
    b = words[2]
    d = int(words[4])
    if a not in places.keys():
        places[a]={}
    places[a][b]=d
    if b not in places.keys():
        places[b]={}
    places[b][a]=d

print(places)

def shortest(visited):
    global places
    if len(visited) == len(places):
        return 0
    if len(visited) == 0:
        return min(list(map(lambda p: shortest([p]), places.keys())))
    m = 999999
    for name in filter(lambda n: n not in visited, places.keys()):
        distance = places[visited[-1]][name] + shortest(visited + [name])
        if distance < m:
            m = distance
    return distance

print(shortest([]))