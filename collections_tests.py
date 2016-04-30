import unittest
import urllib.parse


class CollectionsTests(unittest.TestCase):

    def setUp(self):
        # define instructions that will be executed before each test method
        # we can do stuff like 'self.customvariable = <custom value>'
        pass

    def tearDown(self):
        # define instructions that will be executed after each test method
        pass

    def test_combining_lists(self):
        a_list = [1, 2, 3]
        a_list.append(4)
        assert a_list == [1, 2, 3, 4]
        assert a_list + [5, 6, 7] == [1, 2, 3, 4, 5, 6, 7]

        a_list.extend(range(5, 8))
        assert a_list == [1, 2, 3, 4, 5, 6, 7]
        b_list = list(range(10))
        c_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert b_list == c_list
        assert b_list is not c_list  # checks for memory equality, not value

        d_list = list('acdf')
        assert d_list == ['a', 'c', 'd', 'f']
        d_list.insert(1, 'b')
        assert d_list == ['a', 'b', 'c', 'd', 'f']
        d_list.insert(4, 'e')
        assert d_list == ['a', 'b', 'c', 'd', 'e', 'f']

        d_list.remove('d')  # removes by value
        assert d_list == ['a', 'b', 'c', 'e', 'f']
        del d_list[1]  # removes by index
        assert d_list == ['a', 'c', 'e', 'f']

        temp = d_list.pop()
        assert temp == 'f'
        assert d_list == ['a', 'c', 'e']

        temp = d_list.pop(1)
        assert temp == 'c'
        assert d_list == ['a', 'e']

    def test_slicing(self):
        my_string = "Hello there"
        assert my_string[1:5] == "ello"

        a_list = list(range(0, 6))
        assert a_list == [0, 1, 2, 3, 4, 5]
        assert a_list[1:3] == [1, 2]
        assert a_list[0:5] == [0, 1, 2, 3, 4]
        assert a_list[0:6] == [0, 1, 2, 3, 4, 5]
        assert a_list[0:len(a_list)] == [0, 1, 2, 3, 4, 5]
        assert a_list[:6] == [0, 1, 2, 3, 4, 5]
        assert a_list[0:] == [0, 1, 2, 3, 4, 5]
        assert a_list[1:] == [1, 2, 3, 4, 5]
        assert a_list[:] == [0, 1, 2, 3, 4, 5]  # handy for copying lists

        # slicing with a step (skip or move back)
        b_list = list(range(10))  # same as (0,10) i.e. 0 - 9
        assert b_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert b_list[::2] == [0, 2, 4, 6, 8]  # entire list, add 2
        assert b_list[1::2] == [1, 3, 5, 7, 9]  # entire list start @ 1, add 2
        assert b_list[::-1] == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  # reverse
        assert b_list[1:4] == [1, 2, 3]
        assert b_list[3:0:-1] == [3, 2, 1]
        assert b_list[3::-1] == [3, 2, 1, 0]
        assert b_list[-1] == 9
        assert b_list[-2] == 8

        del b_list[:2]
        assert b_list == [2, 3, 4, 5, 6, 7, 8, 9]  # deleted first 2
        b_list[1:4] = ['a', 'b', 'c']  # replace index 1-3 .. 3,4,5 with a,b,c
        assert b_list == [2, 'a', 'b', 'c', 6, 7, 8, 9]

    def test_dictionaries(self):
        a_dict = {'name': 'shane'}
        assert a_dict['name'] == 'shane'

        a_dict = {'name': 'shane', 'job': 'awesomeness'}
        assert a_dict['name'] == 'shane'
        assert a_dict['job'] == 'awesomeness'

        # want to test KeyError but assertRaises takes a function so
        # using lambda to make anonymous function
        self.assertRaises(KeyError, lambda: a_dict['test'])

        final = "name='shane', job='awesomeness'"
        format_string = "name='{name}', job='{job}'"
        assert format_string.format(**a_dict) == final  # ** unpacks dictionary

    def test_update_dictionaries(self):
        a_dict = {}
        a_dict['key'] = {'a': 1, 'b': 2}
        assert a_dict['key']['a'] == 1
        assert a_dict['key']['b'] == 2

        a_dict['key']['a'] += a_dict['key']['a']
        a_dict['key']['b'] += a_dict['key']['b']

        assert a_dict['key']['a'] == 2
        assert a_dict['key']['b'] == 4

        a_dict['key']['a'] += 1
        a_dict['key']['b'] += 1

        assert a_dict['key']['a'] == 3
        assert a_dict['key']['b'] == 5

    def test_tuples(self):
        a_tuple = (1, 2, 3)
        b_tuple = 1, 2, 3
        assert a_tuple == b_tuple  # it is the comma that matters

        a, b = 1, 2
        assert a == 1
        assert b == 2

        c = (4, 5)
        d, e = c
        assert d == 4
        assert e == 5

        f = d, e
        assert f == c

        assert tuple_test() == (1, 2, 3)
        x, y, z = tuple_test()
        assert x == 1
        assert y == 2
        assert z == 3

        assert "{}, {}, {}".format(*a_tuple)  # * unpacks tuple ** unpacks list

        my_list = list('abcdefghijklmnopqrstuvwxyz')
        for index, value in enumerate(my_list):
            print('{}: {}'.format(index, value))

    def test_url_encode(self):
        list = {'a':1, 'b':2}
        url = urllib.parse.urlencode(list)
        print('test')
        print(url)


def tuple_test():
    return 1, 2, 3


if __name__ == '__main__':
    unittest.main()
