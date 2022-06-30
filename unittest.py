from unittest import TestCase, main
from MunishaKaurBoora_assessment_two import is_palindrome


class TestPalindrome(TestCase):
    def test_palindrome_word_one(self):
        expected = True
        result = is_palindrome(word = 'bob')
        self.assertEqual(expected, result)

    def test_not_palindrome_word(self):
        expected = False
        result = is_palindrome(word = 'joe')
        self.assertEqual(expected, result)

    def test_palindrome_word_two(self):
        expected = True
        result = is_palindrome(word = 'hannah')
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()

