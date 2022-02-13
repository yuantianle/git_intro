import unittest
from unittest import TestCase
from check_pwd import check_pwd


class Test(TestCase):

    def test_1(self):
        input = ""
        expection = False
        self.assertEqual(check_pwd(input), expection)

    def test_2(self):
        input = "D234567*"
        expection = False
        self.assertEqual(check_pwd(input), expection)

    def test_3(self):
        input = "d234567*"
        expection = False
        self.assertEqual(check_pwd(input), expection)

    def test_4(self):
        input = "dDddddd*"
        expection = False
        self.assertEqual(check_pwd(input), expection)

    def test_5(self):
        input = "dD1ddddd"
        expection = False
        self.assertEqual(check_pwd(input), expection)


# *********************************************************************
if __name__ == '__main__':
    unittest.main(verbosity=2)