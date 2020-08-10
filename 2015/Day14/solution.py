with open('input.txt', 'r') as file:
    text = file.read()


class Reindeer:
    def __init__(self, name, speed, interval, rest):
        self.name = name
        self.speed = int(speed)
        self.interval = int(interval)
        self.rest = int(rest)

    def __eq__(self, other):
        return self.name == other.name and self.speed == other.speed and self.interval == other.interval and self.rest == other.rest

    def distance(self, time):
        dis = 0
        rest = False
        while time > 0:
            if rest:
                time -= self.rest
            else:
                t = min(self.interval, time)
                time -= self.interval
                dis += t * self.speed
            rest = not rest
        return dis


def to_reindeer(txt):
    x = txt.split(" ")
    return Reindeer(x[0], x[3], x[6], x[-2])


time = 2503

winner = max([to_reindeer(txt).distance(time) for txt in text.split("\n")])

print(winner)


def reindeers(text):
    return {line.split(" ")[0]: to_reindeer(line) for line in text.split("\n")}


rs = reindeers(text)


def scores(reindeers, time):
    s = {it: 0 for it in reindeers.keys()}
    for i in range(time):
        m = max([r.distance(i+1) for r in reindeers.values()])
        for v in reindeers.values():
            if v.distance(i+1) == m:
                s[v.name] += 1
    return s


print(scores(rs, time))
