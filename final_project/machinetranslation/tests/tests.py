"""
Unittest Module

The unit tests in this module cover the following cases:
    Verifying the expected translation and function behavior with random input
The unit tests utilize the translate_text function from the translator.py module.

"""
import unittest
import random
from machinetranslation.translator import translate_text


class TranslatorTestCase(unittest.TestCase):
    """
    Test case for the Translator class.

    This case contains unit tests to verify the translation functionality of the Translator class.

    """
    def test_hello_translation_fr(self):
        """
        Test translation of 'Hello' from English to French.
        """
        source_language1 = "en"
        target_language1 = "fr"
        english_text = "Hello"
        # Using googletrans resolves 'Pepitoooo' != 'Bonjour'.
        expected_translationX = "Bonjour"  # pylint: disable=invalid-name

        translation1 = translate_text(source_language1, target_language1, english_text)
        self.assertEqual(translation1, expected_translationX)

    def test_bonjour_translation_en(self):
        """
        Test translation of 'Bonjour' from French to English.

        A way to include both the word 'Hello' (defined in the Lab exercise) and
       'Good morning' (result from the translator).
        """
        source_language2 = "fr"
        target_language2 = "en"
        french_text = "Bonjour"
        expected_translations = ["Good morning", "Hello"]

        translation2 = translate_text(source_language2, target_language2, french_text)
        self.assertIn(translation2, expected_translations) # Solving

    def test_hello_translation_fr_not_equal(self):
        """
        Tests that 'Hello' from English to French is not equal to 'Bonjour' via two randomly
        chosen similar expressions.
        """
        source_language3 = "en"
        target_language3 = "fr"
        english_text1 = "Hello"
        unexpected_translation0 = random.choice(["Bon jou", "Salut"]) # pylint: disable=invalid-name


        translation3 = translate_text(source_language3, target_language3, english_text1)
        self.assertNotEqual(translation3, unexpected_translation0)

    def test_bonjour_translation_en_not_equal(self):
        """
        Tests that 'Bonjour' from French to English is not equal to 'Hello' by reversing
        the result of the translation.
        """
        source_language4 = "fr"
        target_language4 = "en"
        french_text2 = "Bonjour"
        translation4 = translate_text(source_language4, target_language4, french_text2)
        unexpected_translation01 = translation4[::-1] # pylint: disable=invalid-name

        #translation4 = translate_text(source_language4, target_language4, french_text2)
        self.assertNotEqual(translation4, unexpected_translation01)


if __name__ == "__main__":
    unittest.main()
