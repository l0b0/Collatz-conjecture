from __future__ import print_function

import unittest

from collatz_conjecture import collatz_conjecture


class TestCollatzConjectureGraphGenerator(unittest.TestCase):
    def test_should_generate_trivial_graph(self):
        dot_generator = collatz_conjecture.GraphGenerator()
        graph = dot_generator.generate(1)
        self.assertEqual(graph, [1])

    def test_should_generate_graph_with_an_even_starting_point(self):
        dot_generator = collatz_conjecture.GraphGenerator()
        graph = dot_generator.generate(2)
        self.assertEqual(graph, [2, 1])

    def test_should_generate_graph_with_an_odd_starting_point(self):
        dot_generator = collatz_conjecture.GraphGenerator()
        graph = dot_generator.generate(3)
        self.assertEqual(graph, [3, 10, 5, 16, 8, 4, 2, 1])
