import unittest


class ComprehensionsTests(unittest.TestCase):

    def setUp(self):
        # define instructions that will be executed before each test method
        # we can do stuff like 'self.customvariable = <custom value>'
        pass

    def tearDown(self):
        # define instructions that will be executed after each test method
        pass

    def test_indexing(self):
        dict = [0,1,2,3,4]
        comp = dict[:3]
        assert len(comp) == 3
        assert comp[0] == 0
        assert comp[1] == 1
        assert comp[2] == 2

    def test_combining_lists(self):
        nums = range(2, 11, 2)
        assert list(nums) == [2, 4, 6, 8, 10]

        # we want all the numbers divided by 2

        # -- instead of this---
        # halves = []
        # for num in nums:
        #    halves.append(num/2)
        # assert halves == [1.0, 2.0, 3.0, 4.0, 5.0]
        # ---------------------, we can do:
        halves = [num/2 for num in nums]
        assert halves == [1.0, 2.0, 3.0, 4.0, 5.0]

        divisible_by_3 = [num for num in nums if num % 3 == 0]
        assert divisible_by_3 == [6] # only 6 is divisible by 3 in nums

if __name__ == '__main__':
    unittest.main()
