
import unittest

from module2 import add

class TestAdd(unittest.TestCase):

    def test_in_2and4_out_6(self):

        self.assertEqual(add(2, 4), 6)

        self.assertEqual(add(0, 0), 0)

        self.assertEqual(add(2.3, 3.6), 5.9)

        self.assertEqual(add('hello', 'wolrd'), 'hellowolrd')

        self.assertNotEqual(add(-2, -2),0)

unittest.main()
