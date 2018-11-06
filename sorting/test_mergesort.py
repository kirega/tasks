import unittest
import mergesort

class MergesortTest(unittest.TestCase):
    def test_mergesort(self):
        test_array = [3,5,14,1,4] #sorted array 1,3,4,5,14
        t = sorted(test_array)
        self.assertEqual(mergesort.mergesort(test_array), t)

if __name__ == '__main__':
    unittest.main()