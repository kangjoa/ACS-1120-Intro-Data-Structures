def combine_texts(*file_paths):
    combined_text = ""
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            combined_text += file.read() + "\n\n"
    return combined_text


if __name__ == "__main__":
    combined = combine_texts('source_text.txt', 'second_source.txt')
    text_1 = open('source_text.txt', 'r').read()
    text_2 = open('second_source.txt', 'r').read()
    print(f"Source text length: {len(text_1)} characters")
    print(f"Second text length: {len(text_2)} characters")
    print(f"Combined text length: {len(combined)} characters")
    start_index = 136259
    end_index = start_index + 5000
    print(f"# characters from index {start_index}:")
    print(combined[start_index:end_index])
