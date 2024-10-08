# Import Dictogram from the dictogram module.
from dictogram import Dictogram
import random
import timeit


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

    while len(sentence) < length:
        if current_pair in markov_chain:
            next_word = markov_chain[current_pair].sample()
            sentence.append(next_word)
            current_pair = (current_pair[1], next_word)

            # End the sentence if we encounter a period, exclamation mark, or question mark
            if next_word.endswith(('.', '!', '?')):
                break
        else:
            break

    # Capitalize the first word of the sentence
    sentence[0] = sentence[0].capitalize()
    if sentence[-1].endswith(','):
        sentence[-1] = sentence[-1].replace(',', '') + '.'
    elif not sentence[-1].endswith(('.', '!', '?')):
        sentence[-1] += '.'

    return ' '.join(sentence)


def build_fourth_order_markov_chain(word_list: list) -> dict:
    """
    Takes a list of strings to build a Markov chain where each word quadruple points to a Dictogram of the words that follow it.

    Args:
        word_list (list): List of words (strings) representing the corpus.

    Returns:
        dict: A dictionary where each key is a word quadruple (tuple) and each value is a Dictogram of the words that follow it and their frequency.
    """
    # Initialize dictionary
    markov_chain = {}

    # Iterate over word_list to build the chain
    for i in range(len(word_list) - 4):
        word_quadruple = (word_list[i], word_list[i + 1],
                          word_list[i + 2], word_list[i + 3])
        next_word = word_list[i + 4]

        # If the word quadruple is not in the chain, add it with an empty Dictogram
        if word_quadruple not in markov_chain:
            markov_chain[word_quadruple] = Dictogram()

        # Add the next word to the Dictogram for this word quadruple
        markov_chain[word_quadruple].add_count(next_word)

    return markov_chain


def random_walk_fourth(markov_chain: dict, start_words: tuple, length=10) -> str:
    """
    Generate a random sentence using the Markov chain.

    Args:
        markov_chain (dict): A dictionary where each key is a word quadruple (tuple) and each value is a Dictogram of the words that follow it and their frequency.
        start_words (tuple): The word quadruple to start the sentence, from the corpus. 
        length (int, optional): The number of words in the generated sentence. Defaults to 10.

    Returns:
        str: The randomly generated sentence.
    """
    current_quadruple = start_words
    sentence = list(start_words)

    for _ in range(length - 4):
        if current_quadruple in markov_chain:
            next_word = markov_chain[current_quadruple].sample()
            sentence.append(next_word)
            current_quadruple = (
                current_quadruple[1], current_quadruple[2], current_quadruple[3], next_word)
        else:
            break

    return ' '.join(sentence)


def benchmark_markov_chain(chain_function, markov_chain, start_words, length):
    """
    Benchmarks the time taken by the markov_chain random walk function to generate a sentence.

    Args:
        chain_function (func): The random walk function to benchmark.
        markov_chain (dict): The Markov chain dictionary.
        start_words (tuple): The starting word pair.
        length (int): The length of the generated sentence.

    Returns:
        float: The time taken in seconds.
    """
    setup_code = f"""
from __main__ import {chain_function.__name__}
markov_chain = {repr(markov_chain)}
start_words = {repr(start_words)}
length = {length}
"""

    stmt = f"{chain_function.__name__}(markov_chain, start_words, length)"

    # Using timeit to run 1000 iterations and return the average time
    timer = timeit.Timer(stmt, setup=setup_code)
    result = timer.timeit(number=1000) / 1000  # Average over 1000 runs

    return result


def build_second_order_chain(word_list: list):
    """
    Builds a second-order Markov chain.
    """
    build_second_order_markov_chain(word_list)


def build_fourth_order_chain(word_list: list):
    """
    Builds a fourth-order Markov chain.
    """
    build_fourth_order_markov_chain(word_list)


def benchmark_markov_chains(file_path: str):
    """
    Benchmarks the build time of second-order and fourth-order Markov chains.

    Args:
        file_path (str): Path to the text file for the Markov chain.
    """
    # Read the file and split it into words
    with open(file_path, 'r') as file:
        word_list = file.read().split()

    # Benchmark second-order Markov chain build time
    timer_2nd_order = timeit.Timer(
        'build_second_order_chain(word_list)', globals=globals())
    second_order_time = timer_2nd_order.timeit(number=100) / 100
    print(f'Second-order Markov chain build time: {second_order_time}')

    # Benchmark fourth-order Markov chain build time
    timer_4th_order = timeit.Timer(
        'build_fourth_order_chain(word_list)', globals=globals())
    fourth_order_time = timer_4th_order.timeit(number=100) / 100
    print(f'Fourth-order Markov chain build time: {fourth_order_time}')


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

    # file_path = 'source_text.txt'
    file_path = 'Code/source_text.txt'
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

    print("\n")
    print("################### Fourth-Order Markov Chain #########################")
    print("Too deterministic and just gets sentences out of the source text")

    # Build the fourth-order Markov chain
    markov_chain_fourth = build_fourth_order_markov_chain(word_list)

    # Generate sentences using the fourth-order Markov chain
    sentence_1 = random_walk_fourth(
        markov_chain_fourth, ("was", "a", "sort", "of"), 50)
    print(f"sentence 1: {sentence_1}")

    sentence_2 = random_walk_fourth(
        markov_chain_fourth, ("to", "look", "out", "the"), 30)
    print(f"sentence 2: {sentence_2}")

    print("Word not found: croissant")
    sentence_word_not_found = random_walk_fourth(
        markov_chain_fourth, ("croissant", "not", "in", "book"), 10)
    print(f"sentence 3: {sentence_word_not_found}")

    print("\n")
    print("################### Benchmark #########################")
    # Run the benchmark
    benchmark_markov_chains(file_path)
