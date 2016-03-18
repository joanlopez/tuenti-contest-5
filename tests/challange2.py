from unittest import TestCase
from src.challange2.prime import Primes


class TestChallange2(TestCase):

    def test_that_prime_factors_of_315_are_3_3_5_and_7(self):
        self.assertEquals(Primes.get_primes_of(315), [3, 3, 5, 7])

    def test_that_6_is_an_almost_prime(self):
        self.assertTrue(Primes.is_almost_prime(6))

    def test_that_25_is_an_almost_prime(self):
        self.assertTrue(Primes.is_almost_prime(25))

    def test_that_17_is_not_an_almost_prime(self):
        self.assertFalse(Primes.is_almost_prime(17))

    def test_that_81_is_not_an_almost_prime(self):
        self.assertFalse(Primes.is_almost_prime(81))

    def test_that_there_are_4_almost_primes_between_1_and_10(self):
        self.assertEquals(4, len(Primes.almost_primes_between(1, 10)))

    def test_that_there_are_3_almost_primes_between_10_and_20(self):
        self.assertEquals(3, len(Primes.almost_primes_between(10, 20)))
