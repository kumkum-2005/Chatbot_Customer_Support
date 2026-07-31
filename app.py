from flask import Flask, render_template, request, jsonify
import json
import random
import joblib
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK data
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

# Initialize Flask
app = Flask(__name__)

# NLP Setup
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Load ML Model
model = joblib.load("models/chatbot_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# Load Intents
with open("data/intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)


# -----------------------------
# Text Preprocessing
# -----------------------------
def preprocess(text):

    words = nltk.word_tokenize(text.lower())

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word.isalpha() and word not in stop_words
    ]

    return " ".join(words)


# -----------------------------
# Get Chatbot Response
# -----------------------------
def get_response(message):

    processed = preprocess(message)

    vector = vectorizer.transform([processed])

    prediction = model.predict(vector)[0]

    for intent in intents["intents"]:

        if intent["tag"] == prediction:
            return random.choice(intent["responses"])

    return "Sorry, I didn't understand your question."


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Chat API
# -----------------------------
@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "")

    bot_response = get_response(user_message)

    return jsonify({
        "response": bot_response
    })


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)