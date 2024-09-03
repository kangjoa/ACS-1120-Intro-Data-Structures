from dictogram import Dictogram


def histogram(source_text: str) -> Dictogram:
    """
    Creates a histogram from the given source text.

    Args:
        source_text (str): A string of text or a filename to be converted into a histogram.

    Returns:
        Dictogram: A histogram where keys are words from the source text and values are the number of times each word appears.
    """
    with open('source_text.txt', 'r') as file:
        text = file.read()

    # Split text into a list of strings
    word_list = text.split()

    # Create a Dictogram
    return Dictogram(word_list)


def unique_words(histogram: Dictogram) -> int:
    """
    Takes a histogram and return the total count of unique words in the histogram.

    Args:
        histogram (Dictogram): A histogram where keys are words and values are the number of times each word appears.

    Returns:
        int: The total count of unique words in the histogram.
    """
    return histogram.types


def frequency(word: str, histogram: Dictogram) -> int:
    """
    Takes a word and histogram as arguments and returns the number of times that word appears in a text.

    Args:
        word (str): A given word to look for in the histogram.
        histogram (Dictogram): A histogram where keys are words and values are the number of times each word appears.

    Returns:
        int: Number of times a given word appears in the text.
    """
    return histogram.frequency(word)


if __name__ == '__main__':
    # Create a histogram from a string or a file
    hist = histogram('source_text')

    # Get the number of unique words
    print("Unique words:", unique_words(hist))

    # Get the frequency of a specific word
    print("Frequency of 'Gregor':", frequency('Gregor', hist))

    # You can still use the rest of your Dictogram functionality
    print("Random sample:", hist.sample())
