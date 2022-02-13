import unittest
from unittest import TestCase
from check_pwd import check_pwd


class Test(TestCase):

    def test_1(self):
        input = ""
        expection = False
        self.assertEqual(check_pwd(input), expection)


# *********************************************************************
if __name__ == '__main__':
    unittest.main(verbosity=2)