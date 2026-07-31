import json
import random
import joblib
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK resources
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)

# NLP setup
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Load trained model
model = joblib.load("models/chatbot_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# Load intents
with open("data/intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

# Text preprocessing
def preprocess(text):
    text = text.lower()

    words = nltk.word_tokenize(text)

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word.isalpha() and word not in stop_words
    ]

    return " ".join(words)

# Get chatbot response
def get_response(user_input):

    processed = preprocess(user_input)

    vector = vectorizer.transform([processed])

    # Prediction
    prediction = model.predict(vector)[0]

    # Confidence score
    probabilities = model.predict_proba(vector)[0]
    confidence = max(probabilities)

    print(f"Confidence: {confidence:.2f}")

    # Low confidence
    if confidence < 0.50:
        return "I'm sorry, I didn't understand your question. Could you please rephrase it?"

    # Find matching response
    for intent in intents["intents"]:

        if intent["tag"] == prediction:

            return random.choice(intent["responses"])

    return "Sorry, I didn't understand your question."

# Chat loop
print("=" * 45)
print("      AI Customer Support Chatbot")
print("=" * 45)
print("Type 'bye' or 'exit' to quit.\n")

while True:

    user = input("You : ")

    if user.lower() in ["bye", "exit", "quit"]:
        print("Bot : Thank you for contacting us. Goodbye!")
        break

    response = get_response(user)

    print("Bot :", response)