import string
import re
from proper_nouns import extract_proper_nouns, remove_unwanted_proper_nouns, words_to_remove

words_to_preserve_case = ["I", "I'm", "I'll", "I've", "I'd", "as"]


def remove_punctuation(text):
    # Replace smart quotes with standard quotes
    text = text.replace('“', '"').replace(
        '”', '"').replace('‘', "'").replace('’', "'")

    # Keep sentence-ending punctuation, apostrophes, and hyphens
    punctuation = string.punctuation.replace(".", "").replace(
        "!", "").replace("?", "").replace("'", "").replace("-", "")
    translator = str.maketrans('', '', punctuation)
    return text.translate(translator)


def clean_text(text):
    # get proper nouns
    proper_nouns = extract_proper_nouns(text)

    # remove unwanted proper nouns
    cleaned_proper_nouns = remove_unwanted_proper_nouns(proper_nouns)

    # remove punctuation
    text = remove_punctuation(text)

    # split text into words
    words = text.split()

    # store cleaned words
    cleaned_text = []

    # print(f"cleaned proper nouns: {cleaned_proper_nouns}")

    # for word in words:
    #     if word in cleaned_proper_nouns:
    #         cleaned_text.append(word)
    #     elif word not in words_to_remove:
    #         cleaned_text.append(word.lower())

    for word in words:
        # Check if word is in the cleaned proper nouns list
        if word in cleaned_proper_nouns or word in words_to_preserve_case:
            cleaned_text.append(word)
        else:
            # Convert the word to lowercase and check it against words_to_remove
            word_lower = word.lower()
            found_in_remove_list = False

            # Loop through words_to_remove and compare each in lowercase
            for remove_word in words_to_remove:
                if word_lower == remove_word.lower():
                    found_in_remove_list = True
                    break

            # Only append the word if it's not found in words_to_remove
            if not found_in_remove_list:
                cleaned_text.append(word_lower)

    return cleaned_text


if __name__ == "__main__":
    # file_path = 'source_text.txt'
    # with open(file_path, 'r') as file:
    #     text = file.read()

    text = "I  Gutenberg GUTENBERG The five-thirty train has been in and gone half an hour ago,” answered that brisk official. “But there was a passenger dropped off for you--a little girl. BEYOND She’s sitting Anne Anne Anne Gutenberg GUTENBERG out there on the shingles. I asked her togo into the ladies’ waiting room, but she I'd informed me gravely that she  preferred to stay outside. ‘There was more scope for imagination,’ she said. She’s a case, I should say."

    cleaned_text = clean_text(text)
    print(f"cleaned text: {cleaned_text}")
