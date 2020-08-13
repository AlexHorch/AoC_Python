target = 36000000


def presents(house, primes):
    x = (house + 1) * 10
    ps = (prime for prime in primes if prime < house)
    for prime in ps:
        y = house
        while y % prime == 0:
            x += 

    return sum([i*10 for i in range(house) if i > 0 and house % i == 0])


def primes(n):
    ps = [2]
    for i in range(n-2):
        p = True
        for prime in ps:
            if (i+3) % prime == 0:
                p = False
                break
        if p:
            ps.append(i+3)
    return ps
