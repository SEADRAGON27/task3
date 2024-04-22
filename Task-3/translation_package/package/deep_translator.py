from googletrans import Translator, LANGUAGES
from langdetect import detect


def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translator = Translator()
        translated_text = translator.translate(text, src=src, dest=dest).text
        return translated_text
    except Exception as e:
        return f"Translation Error: {str(e)}"


def LangDetect(text: str, set: str) -> str:
    try:
        lang = detect(text)
        if set == "lang":
            return f"Detected Language: {lang}"
        elif set == "confidence":
            return "Confidence Level: Not supported"
        else:
            return f"Detected Language: {lang}"
    except Exception as e:
        return f"Language Detection Error: {str(e)}"


def CodeLang(lang: str) -> str:
    lang = lang.lower()
    return LANGUAGES.get(lang, f"Language '{lang}' not found")
