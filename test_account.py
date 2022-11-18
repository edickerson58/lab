import unittest
from account import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.person = Account('John D.')
        self.person.deposit(1000)

    def test_withdraw(self):
        self.assertEqual(self.person.withdraw(50), True)
        self.assertEqual(self.person.withdraw(0), False)
        self.assertEqual(self.person.withdraw(-50), False)
        self.assertEqual(self.person.withdraw(1001), False)

    def test_deposit(self):
        self.assertEqual(self.person.deposit(50), True)
        self.assertEqual(self.person.deposit(0), False)
        self.assertEqual(self.person.deposit(-50), False)

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), 'John D.')

    def test_get_balance(self):
        self.assertEqual(self.person.get_balance(), 1000)


if __name__ == '__main__':
    unittest.main()
