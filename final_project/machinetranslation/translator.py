"""
Translator Module

This module provides translation functionality using the Google Translate API.
Note: We are using googletrans/Translator instead of deep_translator/MyMemoryTranslator
as per the decision made for this project.

"""

from googletrans import Translator


def translate_text(source_language, target_language, text):
    """
    Translates the given text from the source language to the target language.

    Args:
        source_language (str): The source language code.
        target_language (str): The target language code.
        text (str): The text to be translated.

    Returns:
        str: The translated text.
    """
    translator = Translator(service_urls=["translate.google.com", "translate.google.co.kr"])
    translated = translator.translate(text, src=source_language, dest=target_language)
    return translated.text


def main():
    """
    Main function to interact with the translation functionality.
    """
    english_text = input("Enter English Text:   ")
    translated = translate_text("en", "fr", english_text)
    print(translated)

    french_text = input("Enter French Text:   ")
    translated = translate_text("fr", "en", french_text)
    print(translated)


if __name__ == "__main__":
    main()
