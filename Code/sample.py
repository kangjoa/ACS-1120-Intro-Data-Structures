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


def tally_samples(hist: dict, num_samples: int) -> dict:
    """
    Takes a histogram and samples words a specified number of times, tallying the frequency of each word.

    Args:
        hist (dict): A histogram where keys are words and values are the number of times each word appears.
        num_samples (int): The number of times to run the sample function.

    Returns:
        dict: A dictionary where keys are words and values are the number of times each word was sampled.
    """
    # Initialize a dictionary with all words/keys, set all counts/values to 0
    tally = {word: 0 for word in hist.keys()}

    # Sample the histogram num_samples times and tally the results
    for _ in range(num_samples):
        word = sample(hist)
        tally[word] += 1

    return tally


if __name__ == '__main__':
    # Get the second word in the command line
    file_path = str(sys.argv[1])

    # Generate the histogram from the provided file
    hist = histogram(file_path)

    # Sample a random word from the histogram
    random_word_weighted = sample(hist)

    # Print the selected random word
    print(random_word_weighted)

    # Sample the histogram n times and tally the results
    n = 1000
    tally = tally_samples(hist, n)

    # Print the tally results
    for word, count in tally.items():
        print(f'{word}: {count/n}')
