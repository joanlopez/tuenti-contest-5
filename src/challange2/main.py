#!/usr/bin/env python

from prime import *


def main():
    num_of_iterations = int(raw_input())

    for i in range(num_of_iterations):
        inputs = raw_input().split(' ')
        A = int(inputs[0])
        B = int(inputs[1])
        print(len(Primes.almost_primes_between(A, B)))

if __name__ == '__main__':
    main()