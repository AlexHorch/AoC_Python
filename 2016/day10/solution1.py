from puzzle_input import instructions


class Bot:
    def __init__(self):
        self.values = []

    def set_low_recipient(self, low):
        self.low = low
        self.pass_down()

    def set_high_recipient(self, high):
        self.high = high
        self.pass_down()

    def add_value(self, value):
        self.values = [*self.values, value]
        self.pass_down()

    def pass_down(self):
        if len(self.values)==2:
            self.low.add_value(min(self.values))
            self.high.add_value(max(self.values))


class Output:
    def add_value(self, value):
        self.value = value


bots = {}
outputs = {}
for i in range(210):
    bots[i] = Bot()
    outputs[i] = Output()


for line in filter(lambda l: len(l) == 6, instructions):
    (v, b) = map(lambda x: int(line[x]), [1, 5])
    bots[b] = Bot()
    bots[b].add_value(v)


def parse_split(t):
    (b, l, h) = map(lambda n: int(t[n]), [1, 6, 11])
    (x, y) = (t[5], t[10])
    return b, l, h, x, y


def get_bot_or_output(num, type):
    return bots[num] if type == "bot" else outputs[num]

for line in filter(lambda l: len(l) == 12, instructions):
    split = parse_split(line)
    bot = bots[split[0]]
    low = get_bot_or_output(split[1], split[3])
    high = get_bot_or_output(split[2], split[4])

    bot.set_low_recipient(low)
    bot.set_high_recipient(high)

for num, bot in bots.items():
    print(num, bot.values)
