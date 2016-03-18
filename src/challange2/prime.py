#!/usr/bin/env python

import math


class Primes:

    def __init__(self):
        pass

    @classmethod
    def get_primes_of(cls, number):
        prime_factors = []
        while number % 2 == 0:
            prime_factors.append(2)
            number /= 2

        i = 3
        while i <= math.sqrt(number):
            while number % i == 0:
                prime_factors.append(i)
                number /= i
            i += 2

        if number > 2:
            prime_factors.append(number)

        return prime_factors

    @classmethod
    def is_almost_prime(cls, number):
        prime_factors = cls.get_primes_of(number)
        return len(prime_factors) == 2

    @classmethod
    def almost_primes_between(cls, begin, end):
        almost_primes = []
        for i in range(begin, end+1):
            if cls.is_almost_prime(i):
                almost_primes.append(i)
        return almost_primes