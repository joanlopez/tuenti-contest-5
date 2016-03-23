from unittest import TestCase
from src.challange1.buffer import *


class TestChallange1(TestCase):

    def test_that_with_1_urinals_then_the_max_number_of_men_is_1(self):
        self.assertEquals(Buffer.count_max_men_for(1), 1)

    def test_that_with_2_urinals_then_the_max_number_of_men_is_1(self):
        self.assertEquals(Buffer.count_max_men_for(2), 1)

    def test_that_with_3_urinals_then_the_max_number_of_men_is_2(self):
        self.assertEquals(Buffer.count_max_men_for(3), 2)

    def test_that_with_4_urinals_then_the_max_number_of_men_is_2(self):
        self.assertEquals(Buffer.count_max_men_for(4), 2)

    def test_that_with_5_urinals_then_the_max_number_of_men_is_3(self):
        self.assertEquals(Buffer.count_max_men_for(5), 3)
