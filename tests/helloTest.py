import unittest
from unittest.mock import patch, mock_open
from hello import helloUser
import main

class TestMain(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='Alice\nBob\nCharlie\n')
    @patch('csv.reader')
    def test_hello_user_with_csv(self, mock_csv_reader, mock_open):
        firstName = 'Alice'
        lastName = 'Wonder'
        response = helloUser(firstName,lastName)
        expected = 'Hi Alice Wonder'
        self.assertEqual(response, expected)

if __name__ == '__main__':
    unittest.main()
