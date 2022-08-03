from unittest import TestCase, main
from MunishaKaurBoora_Specialisation_HW3 import generate_phrase

class TestGeneratePhrase(TestCase):
    def test_code_first_girls(self):
        characters = "odeC stFir slrG"
        phrase = "Code First Girls"

        expected = False
        result = generate_phrase(characters, phrase)
        self.assertEqual(expected, result)

    def test_capital_letter(self):
        characters = "A"
        phrase = "a"

        expected = False
        result = generate_phrase(characters, phrase)
        self.assertEqual(expected, result)

    def test_empty_string(self):
        characters = "odeC stFir slrG"
        phrase = ""

        expected = True
        result = generate_phrase(characters, phrase)
        self.assertEqual(expected, result)

    def test_word_hello(self):
        characters = "aheaollabbhb"
        phrase = "hello"

        expected = True
        result = generate_phrase(characters, phrase)
        self.assertEqual(expected, result)




if __name__ == "__main__":
    main()



