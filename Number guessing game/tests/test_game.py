import unittest
from number_guessing_game import generate_random_number

class TestGameLogic(unittest.TestCase):
    def test_generate_random_number(self):
        for _ in range(100):
            num = generate_random_number()
            self.assertTrue(1 <= num <= 100)

if __name__ == '__main__':
    unittest.main()
