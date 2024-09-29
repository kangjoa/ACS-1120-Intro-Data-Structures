"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template, request, redirect
import twitter
from histogram import histogram
from sample import sample
import markov_chain_second as markov
from markov_chain_second import build_second_order_markov_chain, random_walk
import random
from tokens import tokenize, remove_punctuation
from cleanup import clean_text
from proper_nouns import extract_proper_nouns, remove_unwanted_proper_nouns

app = Flask(__name__)


def load_and_clean_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Clean the text
    cleaned_tokens = clean_text(text)

    return cleaned_tokens


tokens = load_and_clean_text('source_text.txt')
markov_chain = build_second_order_markov_chain(tokens)

tokens_2 = load_and_clean_text('second_source.txt')
markov_chain_2 = build_second_order_markov_chain(tokens_2)


@app.route("/")
def home():
    sentences = []

    for chain in [markov_chain, markov_chain_2]:
        for _ in range(5):
            # Choose a random starting pair from all available pairs
            if chain:
                start_pair = random.choice(list(chain.keys()))
                sentence = markov.random_walk(
                    chain, start_pair, 50)  # Increased length to 50
                sentences.append(sentence)

    random_sentence = random.choice(
        sentences) if sentences else "No sentences generated."
    print(f"Generated sentence: {random_sentence}")
    return render_template('index.html', sentence=random_sentence)

    # # Join sentences into HTML
    # html_content = "<h1>Second OrderMarkov Chain Generated Sentences</h1>"

    # html_content += "<h2>Sentences from a 25, 058 token corpus:</h2>"
    # for i, sentence in enumerate(sentences[:5], 1):
    #     html_content += f"<p><strong>Sentence {i}:</strong> {sentence}</p>"

    # # Add a sub-header before the sixth sentence
    # html_content += "<h2>Sentences from a 105, 563 token corpus:</h2>"

    # # Add sentences from the second source
    # for i, sentence in enumerate(sentences[5:], 6):
    #     html_content += f"<p><strong>Sentence {i}:</strong> {sentence}</p>"
    # return html_content


@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    text = 'Gutenberg GUTENBERG gutenberg I The five-thirty train has been in and gone half an hour ago...”'
    cleaned_text = clean_text(text)
    # print(f"Final cleaned text: {cleaned_text}")

    app.run(debug=True)
