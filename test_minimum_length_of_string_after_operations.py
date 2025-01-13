import unittest
from minimum_length_of_string_after_operations import Solution

class TestMinOperations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_exeample_1(self):
        self.assertEqual(self.solution.minimumLength("abaacbcbb"), 5)


if __name__ == '__main__':
    unittest.main()