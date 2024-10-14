import unittest
from algorithm1 import algorithm1
from algorithm2 import algorithm2
from algorithm3 import algorithm3

class TestAlgorithms(unittest.TestCase):

    def test_algorithm1(self):
        self.assertEqual(algorithm1([1, 2, 3]), 6)

    def test_algorithm2(self):
        self.assertEqual(algorithm2([1, 2, 3]), 3)

    def test_algorithm3(self):
        self.assertEqual(algorithm3([1, 2, 3]), 1)

if __name__ == '__main__':
    unittest.main()
