import timeit


def histogram(file_path: str) -> dict:
    """
    Creates a histogram from the given source text.

    Args:
        file_path (str): A string of text or a filename to be converted into a histogram.

    Returns:
        dict: A histogram where keys are words from the source text and values are the number of times each word appears.
    """
    with open(file_path, 'r') as file:
        text = file.read()

    # Split text into a list of strings
    word_list = text.split()

    return make_histogram(word_list)
    # # Initialize dictionary to keep track of words and frequencies
    # hist = {}

    # for word in word_list:
    #     if word in hist:
    #         hist[word] += 1
    #     else:
    #         hist[word] = 1

    # return hist


def unique_words(hist: dict) -> int:
    """
    Takes a histogram and return the total count of unique words in the histogram.

    Args:
        hist (dict): A histogram where keys are words and values are the number of times each word appears.

    Returns:
        int: The total count of unique words in the histogram.
    """
    # The number of unique words is just the number of keys
    return len(hist)


def frequency(word: str, hist: dict) -> int:
    """
    Takes a word and histogram as arguments and returns the number of times that word appears in a text.

    Args:
        word (str): A given word to look for in the histogram.
        hist (dict): A histogram where keys are words and values are the number of times each word appears.

    Returns:
        int: Number of times a given word appears in the text.


    """
    # Find the given word (key) and then return the associated value
    return hist.get(word, 0)


def make_histogram(words: list) -> dict:
    # create a new list called hgram
    # for each word in the list of words
    #    check if word has been counted already
    #    if word is not in histogram
    #        add a new word-count pair to hgram (count is one)
    #    if word is already in hgram
    #        find its current count
    #        make a new word-count pair with
    #         the same word and the current count plus one
    #        replace the word-count pair with the new pair
    # when all words have been read, return the hgram
    hgram = {}
    for word in words:
        if word in hgram:
            hgram[word] += 1
        else:
            hgram[word] = 1
    return hgram


def truncate_histogram(hist: dict, n: int) -> dict:
    """
    Truncates the histogram to the first n items.

    Args:
        hist (dict): The original histogram.
        n (int): The number of items to include in the truncated histogram.

    Returns:
        dict: A truncated histogram containing only the first n items.
    """
    return dict(list(hist.items())[:n])


def list_of_words(length):
    dict_words = '/usr/share/dict/words'
    words_str = open(dict_words, 'r').read()
    all_words = words_str.split("\n")
    return all_words[0:length]


def find(word, hgram):
    """
    Takes a word and the histogram, and then return either the index of the matching word-count pair or None if the word does not exist in the histogram.
    """
    if word in hgram:
        return hgram[word]
    else:
        return None


def count(word, hgram):
    """
    Takes a word and the histogram, and then returns either the index of the matching word-count pair or None if the word does not exist in the histogram.
    """
    return hgram.get(word, 0)


def tuple_histogram(file_path: str) -> list:
    """
    Creates a tuple-based histogram from the given source text.

    Args:
        file_path (str): A string of text or a filename to be converted into a tuple-based histogram.

    Returns:
        list: A tuple-based histogram where each element is a tuple (word, count).
    """
    with open(file_path, 'r') as file:
        text = file.read()

    # Split text into a list of words
    word_list = text.split()

    # Create a tuple-based histogram
    return make_tuple_histogram(word_list)


def make_tuple_histogram(words: list) -> list:
    hgram = []
    for word in words:
        # Search for the word in the list
        for i, (w, count) in enumerate(hgram):
            if w == word:
                hgram[i] = (w, count + 1)
                break
        else:
            hgram.append((word, 1))
    return hgram


def count_in_tuple_histogram(word: str, hgram: list) -> int:
    for w, count in hgram:
        if w == word:
            return count
    return 0


def benchmark_dict_count():
    hundred_words = list_of_words(100)
    ten_thousand_words = list_of_words(10000)

    # Create dictionary-based histograms for 100 words and 10,000 words
    hundred_hgram = make_histogram(hundred_words)
    ten_thousand_hgram = make_histogram(ten_thousand_words)

    # Words to search
    hundred_search = hundred_words[-1]
    ten_thousand_search = ten_thousand_words[-1]

    # Setup for timeit to benchmark dictionary-based histogram
    setup_100 = f"""
from __main__ import count
hundred_hgram = {repr(hundred_hgram)}
hundred_search = {repr(hundred_search)}
"""
    stmt_100 = "count(hundred_search, hundred_hgram)"
    timer_100 = timeit.Timer(stmt_100, setup=setup_100)

    setup_10000 = f"""
from __main__ import count
ten_thousand_hgram = {repr(ten_thousand_hgram)}
ten_thousand_search = {repr(ten_thousand_search)}
"""
    stmt_10000 = "count(ten_thousand_search, ten_thousand_hgram)"
    timer_10000 = timeit.Timer(stmt_10000, setup=setup_10000)

    # Run benchmark
    iterations = 10000
    result_100 = timer_100.timeit(number=iterations)
    result_10000 = timer_10000.timeit(number=iterations)

    print(f"Dict-based count time for 100-word histogram: {result_100}")
    print(f"Dict-based count time for 10,000-word histogram: {result_10000}")


def benchmark_tuple_count():
    hundred_words = list_of_words(100)
    ten_thousand_words = list_of_words(10000)

    # Create tuple-based histograms for 100 words and 10,000 words
    hundred_hgram = make_tuple_histogram(hundred_words)
    ten_thousand_hgram = make_tuple_histogram(ten_thousand_words)

    # Words to search
    hundred_search = hundred_words[-1]
    ten_thousand_search = ten_thousand_words[-1]

    # Setup for timeit to benchmark tuple-based histogram
    setup_100 = f"""
from __main__ import count_in_tuple_histogram
hundred_hgram = {repr(hundred_hgram)}
hundred_search = {repr(hundred_search)}
"""
    stmt_100 = "count_in_tuple_histogram(hundred_search, hundred_hgram)"
    timer_100 = timeit.Timer(stmt_100, setup=setup_100)

    setup_10000 = f"""
from __main__ import count_in_tuple_histogram
ten_thousand_hgram = {repr(ten_thousand_hgram)}
ten_thousand_search = {repr(ten_thousand_search)}
"""
    stmt_10000 = "count_in_tuple_histogram(ten_thousand_search, ten_thousand_hgram)"
    timer_10000 = timeit.Timer(stmt_10000, setup=setup_10000)

    # Run benchmark
    iterations = 10000
    result_100 = timer_100.timeit(number=iterations)
    result_10000 = timer_10000.timeit(number=iterations)

    print(f"Tuple-based count time for 100-word histogram: {result_100}")
    print(f"Tuple-based count time for 10,000-word histogram: {result_10000}")


if __name__ == '__main__':
    benchmark_dict_count()
    benchmark_tuple_count()

# if __name__ == '__main__':
#     # Create a dictionary-based histogram from a file
#     dict_hist = histogram(
#         '/Users/kang/Documents/acs_1120/ACS-1120-Intro-Data-Structures/Code/source_text.txt')

#     # Use dictionary-based functions
#     print("Unique words (dict):", unique_words(dict_hist))
#     print("Frequency of 'Gregor' (dict):", frequency('Gregor', dict_hist))

# if __name__ == '__main__':
#     # Create a tuple-based histogram from the source text file
#     tuple_hist = tuple_histogram(
#         '/Users/kang/Documents/acs_1120/ACS-1120-Intro-Data-Structures/Code/source_text.txt')

#     # Print the tuple-based histogram
#     print("Tuple-based histogram:", tuple_hist)

#     # Use tuple-based count function
#     print("Count of 'Gregor' (tuple):",
#           count_in_tuple_histogram('Gregor', tuple_hist))

    # word_list = list_of_words(5)
    # word_list.append('aal')
    # word_list.append('a')
    # word_list.append('a')

    # # Create a tuple-based histogram from a list of words
    # tuple_hist = make_tuple_histogram(word_list)
    # print(tuple_hist)

    # # Use tuple-based functions
    # print("Count of 'a' (tuple):", count_in_tuple_histogram('a', tuple_hist))
    # print("Count of 'aal' (tuple):", count_in_tuple_histogram('aal', tuple_hist))

    # print(make_histogram(list_of_words(10000)))

    # word_list = list_of_words(5)
    # print(word_list)

    # hgram = make_histogram(word_list)

    # print(count('aal', hgram) == 3)
    # print(count('aal', hgram) == 3)

    # print(histogram('source_text.txt'))
    # print(histogram('corpus_sample.txt'))

    # Truncate the histogram to the first 5 items
    # truncated_hist = truncate_histogram(hist, 5)

    # Print the truncated histogram
    # print("First 5 items in the histogram:")
    # print(truncated_hist.items())

    # # Get the number of unique words
    # print("Unique words:", unique_words(hist))

    # # Get the frequency of a specific word
    # print("Frequency of 'Gregor':", frequency('Gregor', hist))
