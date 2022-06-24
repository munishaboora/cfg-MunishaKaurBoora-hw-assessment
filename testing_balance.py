import unittest
from unittest import TestCase, main
from MunishaKaurBoora_HW4 import validating_available_balance

class TestValidatingAvailableBalanceFunc(TestCase):
    def test_unavailable_balance(self):
        expected = "Insufficient funds available."
        result = validating_available_balance(withdrawal_amount=200)
        self.assertEqual(expected, result)

    def test_available_balance(self):
        expected = "Sufficient funds available."
        result = validating_available_balance(withdrawal_amount=80)
        self.assertEqual(expected, result)

    def test_no_balance(self):
        expected = "Sufficient funds available."
        result = validating_available_balance(withdrawal_amount=100)
        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()

