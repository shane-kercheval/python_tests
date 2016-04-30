import unittest


class PythonTests(unittest.TestCase):


    def test_round(self):
        assert round(20.8) == 21
        assert round(12.5) == 12 # PYTHON ROUNDS DOWN AT .5



if __name__ == '__main__':
    unittest.main()
