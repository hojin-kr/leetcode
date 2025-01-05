import unittest
from shifting_letters_ii import Solution

class TestShiftingLetters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.shiftingLetters("abc", [[0,1,0],[1,2,1],[0,2,1]]), "ace")

if __name__ == '__main__':
    unittest.main()
