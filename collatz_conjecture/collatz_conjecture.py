from __future__ import print_function


class SequenceGenerator(object):
    def generate(self, number):
        assert number >= 1

        graph = []
        while number != 1:
            graph.append(number)
            if number % 2 == 0:
                number >>= 1
            else:
                number *= 3
                number += 1
        graph.append(1)

        return graph


class ArcGenerator(object):
    def __init__(self, sequence_generator):
        self.sequence_generator = sequence_generator

    def generate(self, numbers):
        return [self.sequence_generator(number) for number in numbers]
