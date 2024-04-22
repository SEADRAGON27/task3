from package.google_translator import TransLate, CodeLang
from package.deep_translator import LangDetect


def read_config_file(config_file):
    config_data = {}
    with open(config_file, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config_data[key.strip()] = value.strip()
    return config_data


def translate_text_from_file(text_file, config_file):
    try:
        config_data = read_config_file(config_file)
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()
        print(f"File Name: {text_file}")
        print(f"File Size: {len(text)} bytes")
        print(f"Number of Characters: {len(text)}")
        print(f"Number of Words: {len(text.split())}")
        print(f"Number of Sentences: {text.count('.') + text.count('!') + text.count('?')}")

        detected_language = LangDetect(text, "lang")
        print(detected_language)

        translated_text = TransLate(text, config_data['src_lang'], config_data['dest_lang'])

        if config_data['output'] == 'file':
            output_file = f"{text_file.split('.')[0]}_{config_data['dest_lang']}.txt"
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(translated_text)
            print(f"Translation saved to '{output_file}'")
        else:
            print(f"Translated Text: {translated_text}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    try:
        text_file =  r"C:\Users\Admin\Downloads\text.txt" # Specify the name of your text file
        config_file = r"C:\Users\Admin\Task-3\translation_package\config.txt"  # Specify the name of your config file
        translate_text_from_file(text_file, config_file)
    except ValueError as e:
        print("Error:", e)
        print("String causing the error:", text_file)
