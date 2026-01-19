import unittest
from main import find_min

class TestFindMin(unittest.TestCase):

    def test_mixed_numbers(self):
        numbers = [10, 3.14, -5.5, 0, 2]
        self.assertEqual(find_min(numbers), -5.5)

if __name__ == "__main__":
    unittest.main()
