import unittest


class PythonTests(unittest.TestCase):

    def setUp(self):
        # define instructions that will be executed before each test method
        # we can do stuff like 'self.customvariable = <custom value>'
        pass

    def tearDown(self):
        # define instructions that will be executed after each test method
        pass

    def test_something(self):
        assert True



if __name__ == '__main__':
    unittest.main()
