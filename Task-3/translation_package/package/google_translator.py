from googletrans import Translator, LANGUAGES
from langdetect import detect


def TransLate(text: str, scr: str, dest: str) -> str:
    translator = Translator()
    try:
        translated_text = translator.translate(text, src=scr, dest=dest).text
        return translated_text
    except Exception as e:
        return f"Translation Error: {str(e)}"


def LangDetect(text: str, set: str) -> str:
    try:
        if set == "lang":
            lang = detect(text)
            return f"Detected Language: {lang}"
        elif set == "confidence":
            lang = detect(text)
            return f"Confidence Level: Not supported"  # LangDetect doesn't provide confidence level
        else:
            lang = detect(text)
            confidence = lang.confidence
            return f"Detected Language: {lang}, Confidence Level: {confidence}"
    except Exception as e:
        return f"Language Detection Error: {str(e)}"


def CodeLang(lang: str) -> str:
    lang = lang.lower()
    return LANGUAGES.get(lang, f"Language '{lang}' not found")


def LanguageList(out: str, text: str) -> str:
    try:
        if out == "file":
            with open("languages.txt", "w", encoding="utf-8") as file:
                file.write("N\tLanguage\tISO-639 code\tText\n")
                file.write("-----------------------------------------------\n")
                count = 1
                for code, lang in LANGUAGES.items():
                    translation = TransLate(text, "en", code)
                    file.write(f"{count}\t{lang}\t{code}\t{translation}\n")
                    count += 1
            return "Ok"
        else:
            print("N\tLanguage\tISO-639 code\tText")
            print("-----------------------------------------------")
            count = 1
            for code, lang in LANGUAGES.items():
                translation = TransLate(text, "en", code)
                print(f"{count}\t{lang}\t{code}\t{translation}")
                count += 1
            return "Ok"
    except Exception as e:
        return f"Error: {str(e)}"
