"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template, request, redirect
import twitter
import markov_chain_second as markov
import random
import json
import re

app = Flask(__name__)

# Load the pre-processed tokens
with open('cleaned_tokens.json', 'r', encoding='utf-8') as f:
    cleaned_tokens = json.load(f)

# Build a Markov chain from the cleaned tokens
markov_chain = markov.build_second_order_markov_chain(cleaned_tokens)


def capitalize_sentences(text):
    # Split text into sentences
    sentences = re.split('([.!?] )', text)
    capitalized_sentences = []
    for i in range(0, len(sentences), 2):
        words = sentences[i].split()
        if words:
            words[0] = words[0].capitalize()
        capitalized_sentence = ' '.join(words)
        if i + 1 < len(sentences):
            capitalized_sentence += sentences[i + 1]
        capitalized_sentences.append(capitalized_sentence)
    return ''.join(capitalized_sentences)


def generate_sentence():
    if markov_chain:
        start_pair = random.choice(list(markov_chain.keys()))
        raw_sentence = markov.random_walk(markov_chain, start_pair, 30)
        return capitalize_sentences(raw_sentence)
    else:
        return "No sentences generated."


@app.route("/")
def home():
    sentence = generate_sentence()
    return render_template('index.html', sentence=sentence)


@app.route('/tweet', methods=['POST'])
def tweet():
    status = generate_sentence()  # Generate a new sentence for tweeting
    twitter.tweet(status)
    return redirect('/')


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
