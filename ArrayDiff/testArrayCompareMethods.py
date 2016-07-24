import unittest;
from arrayDiff import ArrayDiff

class TestArrayCompareMethods(unittest.TestCase):

    def test_getArrayAdditions(self):
        currentArray = ArrayDiff([1, 3, 5, 6, 8, 9]);
        targetArray = [1, 2, 5, 7, 9];
        self.assertEqual(currentArray.getArrayAdditions(targetArray), set([2, 7]));

    def test_getArrayDeletions(self):
        currentArray = ArrayDiff([1, 3, 5, 6, 8, 9]);
        targetArray = [1, 2, 5, 7, 9];
        self.assertEqual(currentArray.getArrayDeletions(targetArray), set([3, 6, 8]));


if __name__ == '__main__':
    unittest.main()
