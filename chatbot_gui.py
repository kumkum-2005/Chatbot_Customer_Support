import tkinter as tk
from tkinter.scrolledtext import ScrolledText
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

# NLP setup
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Load model
model = joblib.load("models/chatbot_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# Load intents
with open("data/intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)


# -------------------------
# Text Preprocessing
# -------------------------
def preprocess(text):
    words = nltk.word_tokenize(text.lower())

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word.isalpha() and word not in stop_words
    ]

    return " ".join(words)


# -------------------------
# Chatbot Response
# -------------------------
def get_response(message):

    processed = preprocess(message)

    vector = vectorizer.transform([processed])

    prediction = model.predict(vector)[0]

    for intent in intents["intents"]:
        if intent["tag"] == prediction:
            return random.choice(intent["responses"])

    return "Sorry, I didn't understand."


# -------------------------
# Send Message
# -------------------------
def send_message(event=None):

    user_message = entry.get().strip()

    if user_message == "":
        return

    chat.config(state="normal")

    chat.insert(tk.END, "You : " + user_message + "\n")

    response = get_response(user_message)

    chat.insert(tk.END, "Bot : " + response + "\n\n")

    chat.see(tk.END)

    chat.config(state="disabled")

    entry.delete(0, tk.END)


# -------------------------
# Clear Chat
# -------------------------
def clear_chat():

    chat.config(state="normal")

    chat.delete("1.0", tk.END)

    chat.config(state="disabled")


# -------------------------
# Exit
# -------------------------
def exit_chat():

    window.destroy()


# =========================
# GUI
# =========================

window = tk.Tk()

window.title("AI Customer Support Chatbot")

window.geometry("700x600")

window.resizable(False, False)


# Chat Area
chat = ScrolledText(
    window,
    font=("Arial", 12),
    wrap=tk.WORD
)

chat.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

chat.insert(
    tk.END,
    "Bot : Hello! Welcome to AI Customer Support Chatbot.\n\n"
)

chat.config(state="disabled")


# Bottom Frame
bottom_frame = tk.Frame(window)

bottom_frame.pack(
    fill="x",
    padx=10,
    pady=10
)


# Entry Box
entry = tk.Entry(
    bottom_frame,
    font=("Arial", 12)
)

entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 10)
)


# Send Button
send_btn = tk.Button(
    bottom_frame,
    text="Send",
    width=10,
    command=send_message
)

send_btn.pack(side="right")


# Button Frame
button_frame = tk.Frame(window)

button_frame.pack(pady=5)


# Clear Button
clear_btn = tk.Button(
    button_frame,
    text="Clear Chat",
    width=15,
    command=clear_chat
)

clear_btn.pack(side="left", padx=5)


# Exit Button
exit_btn = tk.Button(
    button_frame,
    text="Exit",
    width=15,
    command=exit_chat
)

exit_btn.pack(side="left", padx=5)


# Enter Key
entry.bind("<Return>", send_message)


window.mainloop()