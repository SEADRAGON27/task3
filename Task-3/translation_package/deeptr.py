
from package.deep_translator import TransLate, LangDetect, CodeLang

def main():
    print("Welcome to the Deep Translation Chat!")
    while True:
        print("\nEnter 'exit' to quit the chat.")
        txt = input("Enter the text you want to translate: ")
        if txt.lower() == 'exit':
            print("Goodbye!")
            break
        lang = input("Enter the language code or name to translate to: ")
        print(f"\nOriginal text: {txt}")
        print(LangDetect(txt, "all"))
        translated_text = TransLate(txt, "auto", lang)
        print(f"Translated text: {translated_text}")
        print(f"Language: {CodeLang(lang)}")

if __name__ == "__main__":
    main()
