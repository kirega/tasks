import unittest
import dice
def check_range(x):
    if x>=1 and x <= 6 :
        return True
    return False

class DiceTests(unittest.TestCase):
    def test_dice(self):
        self.assertTrue(check_range(dice.dice()))
if __name__ == '__main__':
    unittest.main()