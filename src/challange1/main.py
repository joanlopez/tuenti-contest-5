#!/usr/bin/env python

from buffer import *


def main():
    num_of_iterations = int(raw_input())

    for i in range(num_of_iterations):
        num_of_urinals = int(raw_input())
        print(Buffer.count_max_men_for(num_of_urinals))

if __name__ == '__main__':
    main()