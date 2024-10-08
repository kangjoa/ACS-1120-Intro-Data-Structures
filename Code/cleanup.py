import re
from proper_nouns import extract_proper_nouns, remove_unwanted_proper_nouns, words_to_remove
from tokens import tokenize

words_to_preserve_case = ["I", "I'm", "I'll", "I've", "I'd", "as"]


def remove_tm_symbol(text):
    return text.replace('™', '')


def remove_smart_quotes(text):
    return text.replace('“', '').replace('”', '').replace('‘', "").replace('’', "'")


def remove_special_combos(text):
    text = re.sub(r"\.\'\s*", ".", text)
    text = re.sub(r',"\s*', '', text)
    text = text.replace(", '", '')
    return text


def remove_new_lines(text):
    return text.replace("\n", " ")


def remove_some_punctuation(text):
    text = text.replace('(', '').replace(')', '')
    return text


def clean_text(text):
    text = remove_new_lines(text)

    text = remove_tm_symbol(text)

    text = remove_some_punctuation(text)

    text = remove_smart_quotes(text)

    text = remove_special_combos(text)

    proper_nouns = extract_proper_nouns(text)
    cleaned_proper_nouns = remove_unwanted_proper_nouns(proper_nouns)

    words = tokenize(text)

    cleaned_text = []
    for word in words:
        # Remove punctuation for comparison, except apostrophes
        word_stripped = re.sub(r'[^\w\s\']', '', word)
        if word_stripped in cleaned_proper_nouns or word in words_to_preserve_case:
            cleaned_text.append(word)
        elif word.lower() in [w.lower() for w in cleaned_proper_nouns]:
            cleaned_text.append(word)
        else:
            word_lower = word.lower()
            if word_lower not in [w.lower() for w in words_to_remove]:
                cleaned_text.append(word_lower)

    return cleaned_text


if __name__ == "__main__":
    # file_path = 'source_text.txt'
    # with open(file_path, 'r') as file:
    #     text = file.read()

    # text = "I  Gutenberg GUTENBERG gutenberg™ The five-thirty train has been in and gone half an hour ago,” answered that brisk official. “But there was a passenger dropped off for you--a little girl. BEYOND She’s sitting Anne Anne Anne Gutenberg GUTENBERG out there on the shingles. I asked her togo into the ladies’ waiting room, but she I'd informed me gravely that she  preferred to stay outside. ‘There was more scope for imagination,’ she said. She’s a case, I should say."

    text = "“You did just splendidly, Anne,” puffed Diana, recovering sufficiently to I sit up and speak, for Anne, starry eyed and rapt, hadn't uttered a word,"

    cleaned_text = clean_text(text)
    print(f"Final cleaned text: {cleaned_text}")
