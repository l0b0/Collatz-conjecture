from __future__ import print_function

import unittest

from mock import mock

from collatz_conjecture import collatz_conjecture


class TestCollatzConjectureSequenceGenerator(unittest.TestCase):
    def setUp(self):
        self.sequence_generator = collatz_conjecture.SequenceGenerator()

    def test_should_generate_trivial_sequence(self):
        sequence = self.sequence_generator.generate(1)
        self.assertEqual(sequence, [1])

    def test_should_generate_sequence_with_an_even_starting_point(self):
        sequence = self.sequence_generator.generate(2)
        self.assertEqual(sequence, [2, 1])

    def test_should_generate_sequence_with_an_odd_starting_point(self):
        sequence = self.sequence_generator.generate(3)
        self.assertEqual(sequence, [3, 10, 5, 16, 8, 4, 2, 1])

    def test_should_generate_sequence_which_does_not_contain_earlier_sequences(self):
        sequence = self.sequence_generator.generate(7)
        self.assertEqual(sequence, [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    def test_should_fail_with_a_starting_point_below_one(self):
        self.assertRaises(AssertionError, self.sequence_generator.generate, 0)


class TestCollatzConjectureArcGenerator(unittest.TestCase):
    def test_should_join_together_sequences(self):
        self.sequence_generator = mock.Mock()
        first_sequence = mock.Mock()
        second_sequence = mock.Mock()
        third_sequence = mock.Mock()

        def sequence_generator(number):
            return {1: first_sequence, 2: second_sequence, 3: third_sequence}[number]

        self.sequence_generator.side_effect = sequence_generator
        self.arc_generator = collatz_conjecture.ArcGenerator(self.sequence_generator)

        arc = self.arc_generator.generate([1, 2, 3])
        self.assertEqual(arc, [first_sequence, second_sequence, third_sequence])
