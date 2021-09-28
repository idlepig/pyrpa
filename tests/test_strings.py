

import unittest
from pyrpa.pyrpa import string


class TestString(unittest.TestCase):

    def test_split(self):
        s = '2019 123\n2019 abc\n321'
        new = string.merge_lines(s, '2019')
        self.assertEqual(new, ['2019 123', '2019 abc'])


if __name__ == '__main__':
    unittest.main()
