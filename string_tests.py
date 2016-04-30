import unittest


class StringTests(unittest.TestCase):

    def test_something(self):
        string = "123456789"
        assert string[:-1] == "12345678"

    def test_split(self):
        assert 'test1|test2'.split('|')[0] == 'test1'
        assert 'test1'.split('|')[0] == 'test1'

if __name__ == '__main__':
    unittest.main()
