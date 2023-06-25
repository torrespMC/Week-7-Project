import random

def guess():
    return random.randint(2, 5000)

def isPrime(x):
        # check for factors
        for i in range(2, x):
            if (x % i) == 0:
                return False
        return True

def findPrimes(num):
    primes = []
    for i in range(num):
        p = guess()
        while not isPrime(p):
            p = guess()
        primes += [p]
    return primes

import cProfile
cProfile.run('print(findPrimes(500)[:10])')
