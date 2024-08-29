import random
import sys
# read in the words file and store in a list
with open('/usr/share/dict/words', 'r') as file:
    words = file.read().splitlines()

# Get the second word in the command line
num_words = int(sys.argv[1])

# Take the number and then return the words in a "sentence"


def sentence_maker(num_words):
    selected_words = random.sample(words, num_words)
    print(' '.join(selected_words))


# output your sentence
sentence_maker(num_words)
