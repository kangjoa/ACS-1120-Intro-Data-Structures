import re


def tokenize(text):
    text = text.replace('--', ' -- ')
    tokens = re.findall(r'\S+(?:[.!?](?=\s|$))?', text)
    return tokens


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, 'r', encoding='utf-8') as file:
            source = file.read()
        tokens = tokenize(source)
        print(len(tokens))
    else:
        print('No source text filename given as argument')
