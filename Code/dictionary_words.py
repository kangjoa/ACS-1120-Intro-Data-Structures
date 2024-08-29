import random
import sys
# read in the words file
with open('/usr/share/dict/words', 'r') as file:
    words = file.read().splitlines()

# select a random set of words from the file and store in a data type


# def get_five_words(words):
#     random.shuffle(words)
#     return words[:5]


# show_me = get_five_words(words)
# print(show_me)

# Get the second word in the command line
num_words = int(sys.argv[1])

# print(type(num_words))

# Take the number and then return the words in a "sentence"


def sentence_maker(num_words):
    # selected_words = words[:num_words]
    selected_words = random.sample(words, num_words)
    # random.shuffle(selected_words)
    print(' '.join(selected_words))


# output your sentence
sentence_maker(num_words)
