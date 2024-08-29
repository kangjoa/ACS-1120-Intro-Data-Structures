import random
import sys
# Take some words and rearrange them randomly

# Start on the second word in the command line and return a list
words = sys.argv[1:]

random.shuffle(words)

print(' '.join(words))
