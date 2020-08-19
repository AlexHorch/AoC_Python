player = [50, 500]
boss = [51, 9]

effects = {"shield": 0, "poison": 0, "recharge": 0}


def mm(player, boss, effects, turn):
    if player[1] < 53:
        return 100000
    player[1] -= 53
    boss[0] -= 4
    return boss_turn(player, boss, effects, turn)


def drain(player, boss, effects, turn):
    if player[1] < 73:
        return 100000
    player[1] -= 73
    player[0] += 2
    boss[0] -= 2
    return boss_turn(player, boss, effects, turn)


def shield(player, boss, effects, turn):
    if player[1] < 113:
        return 100000
    player[1] -= 113
    effects["shield"] = 6
    return boss_turn(player, boss, effects, turn)


def poison(player, boss, effects, turn):
    if player[1] < 173:
        return 100000
    player[1] -= 173
    effects["poison"] = 6
    return boss_turn(player, boss, effects, turn)


def recharge(player, boss, effects, turn):
    if player[1] < 229:
        return 100000
    player[1] -= 229
    effects["recharge"] = 5
    return boss_turn(player, boss, effects, turn)


spells = {mm: 53, drain: 73, shield: 113, poison: 173, recharge: 229}


def player_turn(player, boss, effects, turn):
    player[0]-=1
    if player[0] < 1:
        return 100000
    if turn > 30 or player[0] < 1:
        return 100000
    if effects["recharge"] > 0:
        player[1] += 101
    if effects["poison"] > 0:
        boss[0] -= 3
    if boss[0] < 1:
        return 0
    for e in effects.keys():
        effects[e] -= 1
    return min([cost + spell(player.copy(), boss.copy(), effects.copy(), turn+1)
                for spell, cost in spells.items()])


def boss_turn(player, boss, effects, turn):
    if effects["poison"] > 0:
        boss[0] -= 3
    if boss[0] < 1:
        return 0

    if turn > 30:
        return 100000

    if effects["recharge"] > 0:
        player[1] += 101

    if effects["shield"] > 0:
        player[0] -= max(1, boss[1]-7)
    else:
        player[0] -= boss[1]

    for e in effects.keys():
        effects[e] -= 1
    return player_turn(player, boss, effects, turn+1)


print(player_turn([50, 500], [51, 9], effects, 0))
