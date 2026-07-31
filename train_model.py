import json
import os
import joblib
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Download NLTK resources
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

# Initialize NLP
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Load dataset
with open("data/intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

sentences = []
labels = []

# Preprocess text
for intent in intents["intents"]:
    tag = intent["tag"]

    for pattern in intent["patterns"]:

        pattern = pattern.lower()

        words = nltk.word_tokenize(pattern)

        words = [
            lemmatizer.lemmatize(word)
            for word in words
            if word.isalpha() and word not in stop_words
        ]

        clean_sentence = " ".join(words)

        sentences.append(clean_sentence)
        labels.append(tag)

print("Total Training Samples:", len(sentences))

# TF-IDF
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    lowercase=True,
    max_features=5000
)

X = vectorizer.fit_transform(sentences)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    labels,
    test_size=0.2,
    random_state=42,
    stratify=labels
)

# Train Model
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)

# Accuracy
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Create models folder
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(model, "models/chatbot_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("\nModel Saved Successfully!")
print("chatbot_model.pkl")
print("vectorizer.pkl")