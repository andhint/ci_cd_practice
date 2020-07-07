import unittest

from my_script import add_two 

class TestMyScript(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(add_two(2), 4)
        self.assertEqual(add_two(0), 2)
        self.assertEqual(add_two(-4), -2)
        self.assertEqual(add_two(-2), 0)