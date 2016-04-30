import unittest


class TestClass:
    classVariable = 5
    __privateVariable = 20

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_private_variable(self):
        return self.__privateVariable

    def set_private_variable(self, value):
        self.__privateVariable = value


class ClassTests(unittest.TestCase):
    def test_variables(self):
        assert TestClass.classVariable == 5
        test_class1 = TestClass(1, 2)
        test_class2 = TestClass(3, 4)
        assert test_class1.classVariable == 5
        assert test_class2.classVariable == 5
        assert test_class1.a == 1
        assert test_class1.b == 2
        assert test_class2.a == 3
        assert test_class2.b == 4

        test_class1.a = 10
        test_class1.classVariable = 100 # this isn't static, only changes for 1

        assert test_class1.a == 10
        assert test_class2.a == 3

        assert test_class1.classVariable == 100
        assert test_class2.classVariable == 5  # class variable still equal 5!!
        assert TestClass.classVariable == 5

        TestClass.classVariable = 200
        assert TestClass.classVariable == 200
        assert test_class1.classVariable == 100  # didn't change, retained val
        assert test_class2.classVariable == 200

        # can't access __privateVariable
        self.assertRaises(AttributeError,
                          lambda: print(test_class1.__privateVariable))

        assert test_class1.get_private_variable() == 20
        assert test_class2.get_private_variable() == 20

        test_class1.set_private_variable(40)

        assert test_class1.get_private_variable() == 40
        assert test_class2.get_private_variable() == 20

if __name__ == '__main__':
    unittest.main()
