import unittest
from src.Modules.Basics.RootsSolver import roots


class MyTestCase(unittest.TestCase):
    def test_negative_discr(self):
        self.assertRaises(Exception)

    def test_something(self):
        result = roots(1, 11, 1)

        self.assertTrue(len(result) == 2)


if __name__ == '__main__':
    unittest.main()
