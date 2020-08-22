import math
target = 36000000


def primes_to(n):
    ps = [2]
    for i in range(3, n+1):
        p = True
        for prime in ps:
            if i % prime == 0:
                p = False
                break
        if p:
            ps.append(i)
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
    total = 0
    factors = prime_factorization(house, primes)
    perms = permutations(len(factors))
    return sum(set([math.prod([factors[i] * perm[i] + (not perm[i]) for i in range(len(perm))]) for perm in perms]))*10


print(presents(40320, primes_to(40320)))