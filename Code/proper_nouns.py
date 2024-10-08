import spacy
import re

# Load the English NLP model
nlp = spacy.load('en_core_web_sm')

words_to_remove = ['PG', 'Project', 'Gutenberg',
                   'Project', 'Literary', 'Archive', 'eBooks', 'ebook', 'ebooks', 'eBook', 'PROJECT', 'GUTENBERG', 'gutenberg']

custom_proper_nouns = ['Gables', 'States', 'Gregor', "Gregor's", "Anne's"]

# Add common adjectives that are being misclassified
common_adjectives = ['eyed', 'rapt', 'starry']


def extract_proper_nouns(text: str) -> list:
    """
    Takes a string of text, processes the text with spaCy, and returns a list if proper nouns. 

    Args:
        text (str): A string of text like the corpus.

    Returns:
        list: A list of proper nouns from the text.
    """
    # Process the text with spaCy
    doc = nlp(text)

    # Extract proper nouns
    proper_nouns = [token.text for token in doc if token.pos_ ==
                    'PROPN' and token.text.lower() not in common_adjectives]

    # for token in doc:
    #     print(f"{token.text}: {token.pos_}")

    # Add custom proper nouns to the list
    for custom_word in custom_proper_nouns:
        if custom_word in text.split():
            proper_nouns.append(custom_word)

    return proper_nouns


def remove_unwanted_proper_nouns(proper_nouns: list) -> list:
    """
    Takes a string of proper nouns from the text and returns a cleaned list.

    Args:
        proper_nouns (list): Proper nouns from the text.

    Returns:
        list: List of proper nouns with unwanted ones removed, like Project Gutenberg specific text.
    """
    cleaned_proper_nouns = []

    # words_to_remove_lower = []
    # for word in words_to_remove:
    #     words_to_remove_lower.append(word.lower())
    # print(words_to_remove_lower)

    cleaned_proper_nouns = []

    # regex pattern to match any word in words_to_remove, ignoring case
    words_pattern = '|'.join([re.escape(word) for word in words_to_remove])
    pattern = re.compile(words_pattern, re.IGNORECASE)

    for noun in proper_nouns:
        if not pattern.match(noun):
            cleaned_proper_nouns.append(noun)

    # for noun in proper_nouns:
    #     if noun not in words_to_remove:
    #         cleaned_proper_nouns.append(noun)

    return cleaned_proper_nouns


if __name__ == "__main__":
    # file_path = 'second_source.txt'
    # with open(file_path, 'r') as file:
    #     text = file.read()
    # text = '“Anne Anne Anne Marilla Green Gables Gutenberg GUTENBERG Red Beyond The five-thirty train has been Gilbert Blythe Marilla in and gone half an hour ago,” answered that brisk official. “But there was a passenger dropped off for you--a little girl. She’s sitting Anne Anne Anne’s Gutenberg GUTENBERG out there on the shingles. I asked Gilbert’s her togo into the ladies’ waiting room, but she informed me gravely that she  preferred to stay outside. ‘There was more scope for imagination,’ she said. She’s a case, I should say.”'

    text = "“You did just splendidly, Anne,” puffed Diana, recovering sufficiently to sit up and speak, for Anne, starry eyed and rapt, had not uttered a word."

    proper_nouns = extract_proper_nouns(text)
    # print(f"{proper_nouns}")
    cleaned_proper_nouns = remove_unwanted_proper_nouns(proper_nouns)
    print(f"cleaned prop nouns: {cleaned_proper_nouns}")

    # cleaned_proper_nouns = extract_proper_nouns(text)
    # print(f"cleaned prop nouns: {cleaned_proper_nouns}")
