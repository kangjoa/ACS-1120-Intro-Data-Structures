# Import Dictogram from the dictogram module.
from dictogram import Dictogram
import random


def build_markov_chain(word_list: list) -> dict:
    """
    Takes a list of strings to build a Markov chain where each word points to a Dictogram of the words that follow it. 

    Args:
        word_list (list): List of words (strings) representing the corpus.

    Returns:
        dict: A dictionary where each key is a word (string) and each value is a Dictogram of the words that follow it and their frequency.
    """
    #  Initialize dictionary
    markov_chain = {}

    # Iterate over word_list to build the chain
    for i in range(len(word_list) - 1):
        word = word_list[i]
        next_word = word_list[i + 1]

        # If the word is not in the chain, add it with an empty Dictogram
        if word not in markov_chain:
            markov_chain[word] = Dictogram()

        # Add the next word to the Dictogram for this word
        markov_chain[word].add_count(next_word)

    return markov_chain


def random_walk(markov_chain: dict, start_word: str, length=10) -> str:
    """
    Generate a random sentence using the Markov chain.

    Args:
        markov_chain (dict): A dictionary where each key is a word (string) and each value is a Dictogram of the words that follow it and their frequency.
        start_word (str): The word to start the sentence, from the corpus. 
        length (int, optional): The number of words in the generated sentence. Defaults to 10.

    Returns:
        str: The randomly generated sentence.
    """
    word = start_word
    sentence = [word]

    i = 1
    while i < length:
        if word in markov_chain:
            # Use sample to get a weighted random word
            word = markov_chain[word].sample()
            sentence.append(word)
            i += 1
        elif word not in markov_chain:
            return "word not in corpus"
        else:
            # If no more words can be sampled, end the loop
            i = length

    single_line_sentence = ' '.join(sentence)

    return single_line_sentence


if __name__ == '__main__':
    corpus = "GUTENBERG gutenberg Gutenberg So they couldn’t understand his words any more, although they seemed clear enough to him, clearer than before—perhaps his ears had become used to the sound."

    word_list = corpus.split()
    markov_chain = build_markov_chain(word_list)
    print("Markov Chain:")
    print(markov_chain)

    sentence = random_walk(markov_chain, "clear", 10)

    print(f"sentence 1: {sentence}")

    sentence_2 = random_walk(markov_chain, "his", 10)

    print(f"sentence 2: {sentence_2}")

    file_path = 'source_text.txt'
    with open(file_path, 'r') as file:
        text = file.read()

    # Split text into a list of strings
    word_list = text.split()
    markov_chain = build_markov_chain(word_list)

    sentence_3 = random_walk(markov_chain, "his", 20)

    print(f"sentence 3: {sentence_3}")

    sentence_4 = random_walk(markov_chain, "croissant", 10)
    print(f"sentence 4: {sentence_4}")
