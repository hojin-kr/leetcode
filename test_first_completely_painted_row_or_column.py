import unittest
from first_completely_painted_row_or_column import Solution

class TestFirstCompletelyPaintedRowOrColumn(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.firstCompleteIndex([1,3,4,2], [[1,4],[2,3]]), 2)

if __name__ == '__main__':
    unittest.main()