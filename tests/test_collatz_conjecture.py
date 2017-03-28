from __future__ import print_function

import unittest

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
