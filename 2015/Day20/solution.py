import math
target = 36000000


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


def prime_factorization(n, primes):
    factors = []
    for prime in primes:
        if prime > n:
            break
        while n % prime == 0:
            factors.append(prime)
            n /= prime
    return factors


def permutations(length):
    if length > 0:
        for value in [0, 1]:
            for permutation in permutations(length-1):
                yield (value,) + permutation
    else:
        yield ()


def presents(house, primes):
    total = 10
    factors = prime_factorization(house, primes)
    perms = permutations(len(factors))
    for perm in perms:
        total += math.prod([factors[i]
                            for i in range(len(perm)) if perm[i] == 1]) * 10
    return total


print(len(list(permutations(3))))
