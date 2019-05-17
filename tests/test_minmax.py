import unittest
from algs import minmax


class TestStringMethods(unittest.TestCase):

    def test_minmax_1(self):
        self.assertEqual((1, 10), minmax.minmax_1([5, 1, 2, 10]))


if __name__ == '__main__':
    unittest.main()