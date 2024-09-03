from histogram import histogram
import sys
import random


def sample(hist: histogram) -> str:
    """
    Takes a histogram and returns a single word at random, weighted by the frequency of the word.

    Args:
        hist (histogram): A histogram where keys are words and values are the number of times each word appears.

    Returns:
        str: Single random word.
    """
    #  Get all the words (keys)
    words = list(hist.keys())

    # Get all the weights (values/frequencies)
    weights = list(hist.values())

    # Use random.choices(), which allows weights
    random_word = random.choices(words, weights=weights, k=1)[0]

    return random_word


if __name__ == '__main__':
    # Get the second word in the command line
    file_path = str(sys.argv[1])

    # Generate the histogram from the provided file
    hist = histogram(file_path)

    # Sample a random word from the histogram
    random_word_weighted = sample(hist)

    # Print the selected random word
    print(random_word_weighted)
