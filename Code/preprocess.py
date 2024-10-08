from cleanup import clean_text
import json


def load_and_clean_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return clean_text(text)


def preprocess_and_save(input_files, output_file):
    all_tokens = []
    for file in input_files:
        tokens = load_and_clean_text(file)
        all_tokens.extend(tokens)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_tokens, f)


if __name__ == "__main__":
    input_files = ['source_text.txt', 'second_source.txt']
    output_file = 'cleaned_tokens.json'
    preprocess_and_save(input_files, output_file)
