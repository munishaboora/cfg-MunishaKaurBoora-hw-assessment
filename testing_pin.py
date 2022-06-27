from unittest import TestCase, main
from MunishaKaurBoora_HW4 import validating_pin

class TestValidatingPinFunc(TestCase):
    def test_wrong_pin(self):
        expected = "Please enter your pin code again."
        result = validating_pin(pin_code=1233)
        self.assertEqual(expected, result)

    def test_correct_pin(self):
        expected = "Correct pin entered"
        result = validating_pin(pin_code=1234)
        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()

