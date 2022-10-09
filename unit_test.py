import unittest
import question_one
import question_two
import question_three
import question_four
import question_five

class wordtest(unittest.TestCase):
    def test_data(self):
        self.assertIsInstance(question_one.df('DataBase.csv'), dict)
    def test_test_inv_date(self):
        self.assertEqual(question_one.df('invalid.csv'), "file not found")


if __name__ == '__main__':
    unittest.main()