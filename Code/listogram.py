#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
import random


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        # TODO: Increase word frequency by count
        # self is a list
        if word in self:
            index = self.index_of(word)
            self[index][1] += count
        else:
            self.append([word, count])
            self.types += 1

        self.tokens += 1

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        # TODO: Retrieve word frequency count
        # self = [['one', 1], ['fish', 4], ['two', 1], ['red', 1], ['blue', 1]]
        for inner_list in self:
            if inner_list[0] == word:
                # Return the frequency (second element)
                return inner_list[1]
        return 0

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        # TODO: Check if word is in this histogram
        for inner_list in self:
            if inner_list[0] == word:
                return True
        return False

    def index_of(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        # TODO: Implement linear search to find index of entry with target word
        # Iterate over the list of first values and find the target
        for index, inner_list in enumerate(self):
            if inner_list[0] == target:
                return index
        return None

    def sample(self):
        """Return a word from this histogram, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        # TODO: Randomly choose a word based on its frequency in this histogram
        #  Get all the words (first value in inner list)
        words = [inner_list[0] for inner_list in self]

        # Get all the weights (second value in inner list)
        weights = [inner_list[1] for inner_list in self]

        # Use random.choices(), which allows weights
        random_word = random.choices(words, weights=weights, k=1)[0]

        return random_word


def print_histogram(word_list):
    print()
    print('Histogram:')
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_histogram_samples(histogram)


def print_histogram_samples(histogram):
    print('Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [histogram.sample() for _ in range(10000)]
    samples_hist = Listogram(samples_list)
    print('samples: {}'.format(samples_hist))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in histogram:
        # Calculate word's observed frequency
        observed_freq = count / histogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(
            error) < 0.1 else red
        print('| {!r:<9} '.format(word)
              + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
              + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
              + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()


def main():
    # print("#####################################################")
    # # Create an empty Listogram
    # histogram = Listogram()

    # # Add values to self
    # histogram.extend([['one', 1], ['fish', 4], [
    #                  'two', 1], ['red', 1], ['blue', 1]])

    # # Test the frequency method
    # test_word = 'fish'
    # result = histogram.frequency(test_word)
    # print(f"Frequency of '{test_word}': {result}, correct: 4")

    # # Test a word that does not exist
    # test_word = 'shark'
    # result = histogram.frequency(test_word)
    # print(f"Frequency of '{test_word}': {result}, correct: 0")

    # test_word = 'fish'
    # contains_word = histogram.__contains__(test_word)
    # print(f"Contains '{test_word}': {contains_word}, correct: True")

    # test_word = 'dino'
    # contains_word = histogram.__contains__(test_word)
    # print(f"Contains '{test_word}': {contains_word}, correct: False")

    # target = 'red'
    # index_of_target = histogram.index_of(target)
    # print(f"Contains '{target}': {index_of_target}, correct: 3")

    # target = 'penguin'
    # index_of_target = histogram.index_of(target)
    # print(f"Contains '{target}': {index_of_target}, correct: None")
    # print("#####################################################")

    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()
