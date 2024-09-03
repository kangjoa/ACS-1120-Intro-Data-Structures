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

    # Initialize dictionary to keep track of words and frequencies
    hist = {}

    for word in word_list:
        if word in hist:
            hist[word] += 1
        else:
            hist[word] = 1

    return hist


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


if __name__ == '__main__':
    # Create a histogram from a string or a file
    hist = histogram('source_text.txt')

    # Truncate the histogram to the first 5 items
    truncated_hist = truncate_histogram(hist, 5)

    # Print the truncated histogram
    print("First 5 items in the histogram:")
    print(truncated_hist.items())

    # Get the number of unique words
    print("Unique words:", unique_words(hist))

    # Get the frequency of a specific word
    print("Frequency of 'Gregor':", frequency('Gregor', hist))
