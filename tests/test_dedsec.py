import unittest
from io import StringIO
from unittest.mock import patch
from src.dedsec import dedsec_recruitment

class TestDedSecRecruitment(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_high_skill_recruitment(self, mock_stdout):
        dedsec_recruitment(30)
        self.assertIn("Welcome to DedSec", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_low_skill_recruitment(self, mock_stdout):
        dedsec_recruitment(10)
        self.assertIn("Sorry, but you're not quite ready for DedSec", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
