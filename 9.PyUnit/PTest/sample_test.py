import unittest


class TestExample(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('mayur'.upper(), 'MAYUR')

    def test_isupper(self):
        self.assertTrue('MAYUR'.isupper())
        self.assertTrue('MAYUR'.islower())


if __name__ == "__main__":
    unittest.main()
