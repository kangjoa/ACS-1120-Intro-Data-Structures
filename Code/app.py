"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template, request, redirect
import twitter
from histogram import histogram
from sample import sample
import markov_chain_second as markov
import random
from tokens import tokenize, remove_punctuation

app = Flask(__name__)

# Initialize histogram and build Markov chain
with open('source_text.txt', 'r') as file:
    text = file.read()

text = remove_punctuation(text)
tokens = text.split()

markov_chain = markov.build_second_order_markov_chain(tokens)

with open('second_source.txt', 'r') as file:
    text_2 = file.read()

text_2 = remove_punctuation(text_2)
tokens = text_2.split()

markov_chain_2 = markov.build_second_order_markov_chain(tokens)


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentences = []

    # Generate 5 sentences
    for _ in range(5):
        # Choose a random starting pair
        start_pair = tuple(random.choice(list(markov_chain.keys())))
        sentence = markov.random_walk(markov_chain, start_pair, 30)
        sentences.append(sentence)

    for _ in range(5):
        # Choose a random starting pair
        start_pair = tuple(random.choice(list(markov_chain_2.keys())))
        sentence = markov.random_walk(markov_chain_2, start_pair, 30)
        sentences.append(sentence)

    random_sentence = random.choice(
        sentences) if sentences else "No sentences generated."

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
    app.run(debug=True)
