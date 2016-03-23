from unittest import TestCase
from src.challange7.main import *
from mock import Mock
import __builtin__ as builtins


class TestChallange7(TestCase):

    def test_that_a_girl_with_one_friend_after_adding_another_she_has_two(self):
        girl = Girl('random-name', dict())
        girl.friends = [Girl('random-name', dict())]

        girl.add_friend(Girl('random-name', dict()))

        self.assertEquals(2, len(girl.friends))

    def test_handling_question_a_works_properly(self):
        girl = Girl('random-name', dict())
        girl2 = Girl('random-name', dict())

        girl._treat_question_a('N')
        girl2._treat_question_a('Y')

        self.assertEquals(0, girl.points)
        self.assertEquals(7, girl2.points)

    def test_handling_question_b_works_properly(self):
        false_mock, true_mock = Mock(return_value=False), Mock(return_value=True)
        false_girl = Girl('true', dict())
        true_girl = Girl('true', dict())
        false_girl.like_super_heroes, true_girl.like_super_heroes = false_mock, true_mock

        girl = Girl('random-name', dict())
        girl2 = Girl('random-name', dict())
        girl.friends = [false_girl, true_girl, false_girl]
        girl2.friends = [true_girl, false_girl, true_girl]

        girl._treat_question_b()
        girl2._treat_question_b()

        self.assertEquals(3, girl.points)
        self.assertEquals(6, girl2.points)

    def test_handling_question_c_works_properly(self):
        pass

    def test_handling_question_d_works_properly(self):
        pass

    def test_that_after_handling_a_friendship_the_girls_are_friends(self):
        a = Girl('random-name', dict())
        b = Girl('random-name2', dict())

        girls = dict()
        girls[a.name] = a
        girls[b.name] = b

        handle_friendship(girls, a.name, b.name)

        self.assertTrue(b in a.friends)
        self.assertTrue(a in b.friends)

    def test_that_generate_girls_works_properly_with_random_input(self):
        builtins.raw_input = Mock(side_effect=['MINDY N Y Y Y N',
                                               'COLLEEN Y Y N N Y',
                                               'PIGGY N N N N Y'])
        girls = generate_girls(3)

        self.assertEquals(3, len(girls))
        self.assertTrue('MINDY' in girls.keys())
        self.assertTrue('COLLEEN' in girls.keys())
        self.assertTrue('PIGGY' in girls.keys())
        self.assertFalse('RANDOM' in girls.keys())
        self.assertTrue(girls['MINDY'].like_super_heroes())
        self.assertTrue(girls['MINDY'].like_leisure_suits())
        self.assertTrue(girls['COLLEEN'].like_super_heroes())
        self.assertFalse(girls['COLLEEN'].like_leisure_suits())
        self.assertFalse(girls['PIGGY'].like_super_heroes())
        self.assertFalse(girls['PIGGY'].like_leisure_suits())

    # Despite there's a full test, there are pending tests(main) to be added

    def test_that_the_example_works(self):
        builtins.raw_input = Mock(side_effect=['MINDY N Y Y Y N',
                                               'COLLEEN Y Y N N Y',
                                               'PIGGY N N N N Y',
                                               'BAMBI N N Y Y N',
                                               'BARBARA Y Y Y Y Y',
                                               'MINDY COLLEEN BAMBI',
                                               'PIGGY BAMBI'])

        girls = generate_girls(5)
        store_friendships(girls, 2)
        max_points = count_max_points(girls)
        self.assertEquals(17, max_points)
