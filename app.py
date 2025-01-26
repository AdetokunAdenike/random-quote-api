from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

# Load quotes from quotes.json
with open("quotes.json", "r") as file:
    quotes = json.load(file)

@app.route('/api/quotes', methods=['GET'])
def get_all_quotes():
    """
    Retrieve all available quotes from the dataset.
    
    Returns:
        JSON response containing all quotes.
    """
    return jsonify(quotes)

@app.route('/api/quotes/random', methods=['GET'])
def get_random_quote():
    """
    Retrieve a random quote from the dataset.
    
    Returns:
        JSON response containing a single random quote.
    """
    random_quote = random.choice(quotes)
    return jsonify(random_quote)

@app.route('/api/quotes/<int:quote_id>', methods=['GET'])
def get_quote_by_id(quote_id):
    """
    Retrieve a specific quote by its ID.
    
    Args:
        quote_id (int): The ID of the quote to retrieve.
    
    Returns:
        JSON response containing the quote if found, else a 404 error.
    """
    quote = next((q for q in quotes if q["id"] == quote_id), None)
    if quote:
        return jsonify(quote)
    return jsonify({"error": "Quote not found"}), 404

@app.route('/', methods=['GET'])
def home():
    """
    Default route providing a welcome message and API usage guide.
    
    Returns:
        JSON response with a welcome message.
    """
    return jsonify({
        "message": "Welcome to the Random Quote API! Use /api/quotes to get started."
    })

if __name__ == '__main__':
    # Run the Flask application on port 5000, accessible from any host.
    app.run(host="0.0.0.0", port=5000, debug=True)
