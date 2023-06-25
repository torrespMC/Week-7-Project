import random

def guess():
    return random.randint(2, 5000)

def isPrime(x):
    for i in range(x):
        for j in range(x):
            if i * j == x:
                return False
    return True

def isPrimeVersion2(x):
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

def findPrimesVersion2(num):
    primes = []
    for i in range(num):
        p = guess()
        while not isPrimeVersion2(p):
            p = guess()
        primes += [p]
    return primes

import cProfile
cProfile.run('print(findPrimes(500)[:10])')
cProfile.run('print(findPrimesVersion2(500)[:10])')

