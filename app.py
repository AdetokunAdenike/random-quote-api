from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

# Load quotes from quotes.json
with open("quotes.json", "r") as file:
    quotes = json.load(file)

@app.route('/api/quotes', methods=['GET'])
def get_all_quotes():
    """Return all quotes."""
    return jsonify(quotes)

@app.route('/api/quotes/random', methods=['GET'])
def get_random_quote():
    """Return a random quote."""
    random_quote = random.choice(quotes)
    return jsonify(random_quote)

@app.route('/api/quotes/<int:quote_id>', methods=['GET'])
def get_quote_by_id(quote_id):
    """Return a quote by its ID."""
    quote = next((q for q in quotes if q["id"] == quote_id), None)
    if quote:
        return jsonify(quote)
    return jsonify({"error": "Quote not found"}), 404

@app.route('/', methods=['GET'])
def home():
    """Default route for the API."""
    return jsonify({
        "message": "Welcome to the Random Quote API! Use /api/quotes to get started."
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
