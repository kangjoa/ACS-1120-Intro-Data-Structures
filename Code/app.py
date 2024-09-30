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
from combine_texts import combine_texts

app = Flask(__name__)


def load_and_clean_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    # Clean the text
    cleaned_tokens = clean_text(text)

    return cleaned_tokens


# Combine the two source texts
combined_text = combine_texts('source_text.txt', 'second_source.txt')

# Clean the combined text
tokens = clean_text(combined_text)

# Build a single Markov chain from the combined text
markov_chain = build_second_order_markov_chain(tokens)


@app.route("/")
def home():
    # Choose a random starting pair from all available pairs
    if markov_chain:
        start_pair = random.choice(list(markov_chain.keys()))
        sentence = markov.random_walk(
            markov_chain, start_pair, 30)
    else:
        sentence = "No sentences generated."

    # print(f"Generated sentence: {sentence}")
    return render_template('index.html', sentence=sentence)


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
