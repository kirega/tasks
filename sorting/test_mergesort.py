import unittest
import mergesort


class MergesortTest(unittest.TestCase):
    def test_mergesort(self):
        test_array = [3, 5, 14, 1, 4]  # sorted array 1,3,4,5,14
        t = sorted(test_array)
        self.assertEqual(mergesort.mergesort(test_array), t)
    def test_mixed_list(self):
        test_array = [3, 2, 'e', 4, 'john']
        self.assertFalse(mergesort.check_type(test_array))

    def test_empty_list(self):
        test_array = []
        self.assertEqual(mergesort.mergesort(test_array),'Empty List')

if __name__ == '__main__':
    unittest.main()
