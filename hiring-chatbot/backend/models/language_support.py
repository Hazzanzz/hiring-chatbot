from googletrans import Translator

translator = Translator()

def translate_text(text, target_language):
    """Translate text to the target language."""
    translation = translator.translate(text, dest=target_language)
    return translation.text
