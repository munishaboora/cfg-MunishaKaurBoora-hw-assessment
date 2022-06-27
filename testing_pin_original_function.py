from unittest import TestCase, main
from MunishaKaurBoora_HW4 import validate_pin

class TestOriginalPinFunc(TestCase):

    def test_one_incorrect_pin_entries(self):
        mock_input = [1245, 1222, 1789]
        with self.assertRaises(ValueError):
            validate_pin(mock_input)

    def test_one_incorrect_pin_entry(self):
        mock_input = [1245, 1234]
        expected = "Correct pin entered."
        result = validate_pin(mock_input)
        self.assertEquals(expected, result)

    def test_two_incorrect_pin_entries(self):
        mock_input = [5639, 2784, 1234]
        expected = "Correct pin entered."
        result = validate_pin(mock_input)
        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()


