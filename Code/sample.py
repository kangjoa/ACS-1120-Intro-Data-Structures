from histogram import histogram
import sys
import random


def sample(hist: histogram) -> str:
    """
    Takes a histogram and returns a single word at random.

    Args:
        hist (histogram): A histogram where keys are words and values are the number of times each word appears.

    Returns:
        str: Single random word.
    """
    # Get the second word in the command line
    file_path = str(sys.argv[1])

    random_word = random.choice(list(hist.keys()))

    return random_word


if __name__ == '__main__':
    corpus_hist = histogram('corpus_sample.txt')

    print_me = sample(corpus_hist)

    print(print_me)
