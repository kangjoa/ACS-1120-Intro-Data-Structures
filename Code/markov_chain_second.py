# Import Dictogram from the dictogram module.
from dictogram import Dictogram
import random


def build_second_order_markov_chain(word_list: list) -> dict:
    """
    Takes a list of strings to build a Markov chain where each word pair points to a Dictogram of the words that follow it. 

    Args:
        word_list (list): List of words (strings) representing the corpus.

    Returns:
        dict: A dictionary where each key is a word pair (tuple) and each value is a Dictogram of the words that follow it and their frequency.
    """
    #  Initialize dictionary
    markov_chain = {}

    # Iterate over word_list to build the chain
    for i in range(len(word_list) - 2):
        word_pair = (word_list[i], word_list[i + 1])
        next_word = word_list[i + 2]

        # If the word pair is not in the chain, add it with an empty Dictogram
        if word_pair not in markov_chain:
            markov_chain[word_pair] = Dictogram()

        # Add the next word to the Dictogram for this word pair
        markov_chain[word_pair].add_count(next_word)

    return markov_chain


def random_walk(markov_chain: dict, start_words: tuple, length=10) -> str:
    """
    Generate a random sentence using the Markov chain.

    Args:
        markov_chain (dict): A dictionary where each key is a word pair (tuple) and each value is a Dictogram of the words that follow it and their frequency.
        start_words (tuple): The word pair to start the sentence, from the corpus. 
        length (int, optional): The number of words in the generated sentence. Defaults to 10.

    Returns:
        str: The randomly generated sentence.
    """
    current_pair = start_words
    sentence = list(start_words)

    for _ in range(length - 2):
        if current_pair in markov_chain:
            next_word = markov_chain[current_pair].sample()
            sentence.append(next_word)
            current_pair = (current_pair[1], next_word)
        else:
            break

    return ' '.join(sentence)


if __name__ == '__main__':
    corpus = "So they couldn’t understand his words any more, although they seemed clear enough to him, clearer than before—perhaps his ears had become used to the sound."

    word_list = corpus.split()
    markov_chain = build_second_order_markov_chain(word_list)
    # print("Second-Order Markov Chain:")
    # print(markov_chain)

    sentence = random_walk(markov_chain, ("So", "they"), 10)
    print(f"sentence 1: {sentence}")

    sentence_2 = random_walk(markov_chain, ("his", "words"), 10)
    print(f"sentence 2: {sentence_2}")

    print("\n")
    print("################### With source text #########################")

    file_path = 'source_text.txt'
    with open(file_path, 'r') as file:
        text = file.read()

    # Split text into a list of strings
    word_list = text.split()
    markov_chain = build_second_order_markov_chain(word_list)

    sentence_3 = random_walk(markov_chain, ("father", "looked"), 50)
    print(f"sentence 3: {sentence_3}")

    sentence_5 = random_walk(markov_chain, ("Gregor", "was"), 30)
    print(f"sentence 5: {sentence_5}")

    print("Word not found: croissant")
    sentence_word_not_found = random_walk(
        markov_chain, ("croissant", "nope"), 10)
    print(f"sentence 4: {sentence_word_not_found}")
