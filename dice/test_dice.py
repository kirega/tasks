import unittest
import dice
from unittest import mock


def check_range(x):
    # Ensures that the randomized values are within 1 and 6
    if x >= 1 and x <= 6:
        return True
    return False


class DiceTests(unittest.TestCase):
    def test_dice(self):
        self.assertTrue(check_range(dice.dice()))

    # Mocking the expected output for get_input
    @mock.patch('dice.get_input', return_value='fadfad')
    def test_invalid_input(self, input):
        self.assertEqual(
            dice.entry(), 'Invalid input, type "y" to roll dice again and "n" to exit')

    @mock.patch('dice.get_input', return_value='no')
    def test_valid_input(self, input):
        self.assertEqual(dice.entry(), False)


if __name__ == '__main__':
    unittest.main()
