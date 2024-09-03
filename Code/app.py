"""Main script, uses other modules to generate sentences."""
from flask import Flask
from histogram import histogram
from sample import sample

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
# app.py

# Initialize histogram by using the imported histogram function
histogram_data = histogram('source_text.txt')


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    # Sample a random word from the histogram
    random_word_weighted = sample(histogram_data)

    return f"<p>{random_word_weighted}</p>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
