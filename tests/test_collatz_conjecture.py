from __future__ import print_function

import unittest

from collatz_conjecture import collatz_conjecture


class TestCollatzConjectureGraphGenerator(unittest.TestCase):
    def test_should_generate_trivial_graph(self):
        dot_generator = collatz_conjecture.GraphGenerator()
        graph = dot_generator.generate(1)
        self.assertEqual(graph, [1])
