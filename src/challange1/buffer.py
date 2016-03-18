#!/usr/bin/env python


class Buffer:

    def __init__(self):
        pass

    @classmethod
    def count_max_men_for(cls, num_of_urinals):
        if num_of_urinals <= 2:
            return 1
        else:
            return num_of_urinals / 2 + num_of_urinals % 2
