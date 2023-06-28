"""
Flask server for translation endpoints.
"""

from flask import Flask, render_template, request
from machinetranslation.translator import translate_text

app = Flask("Web Translator")


@app.route("/")
def render_index_page():
    """
    Renders the index.html template.
    """
    return render_template("index.html")


@app.route("/englishToFrench")
def english_to_french():
    """
    Translates English text to French.
    """
    text_to_translate = request.args.get("textToTranslate")
    translation = translate_text("en", "fr", text_to_translate)
    return f"Translated text to French: {translation}"


@app.route("/frenchToEnglish")
def french_to_english():
    """
    Translates French text to English.
    """
    text_to_translate = request.args.get("textToTranslate")
    translation = translate_text("fr", "en", text_to_translate)
    return f"Translated text to English: {translation}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
