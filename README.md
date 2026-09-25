# 📧 Spam Email Classifier

## 📌 Project Overview

The **Spam Email Classifier** is a Machine Learning and Web Development project that automatically classifies email messages as **Spam** or **Not Spam**.

The project uses **Python and Machine Learning** for email classification and **Flask, HTML, CSS, and JavaScript** to create an interactive web application.

---

## 🎯 Objective

The main objective of this project is to develop a machine learning system that can automatically detect spam emails and provide the prediction through a user-friendly web interface.

---

## ✨ Features

* 📧 Spam and Not Spam email classification
* 🧹 Text preprocessing
* 🔤 Lowercase conversion
* 🛑 Stopword removal
* 🌱 Stemming
* 📊 TF-IDF feature extraction
* 🤖 Machine Learning classification
* 📈 Model evaluation
* 🌐 Flask web application
* 🎨 Responsive HTML/CSS interface
* ⚡ JavaScript-based user interaction
* 💾 Saved trained ML model
* 🔮 Real-time spam prediction

---

## 🛠️ Technologies Used

| Technology       | Purpose                                  |
| ---------------- | ---------------------------------------- |
| **Python**       | Machine Learning and backend development |
| **Flask**        | Web application framework                |
| **Scikit-learn** | Machine Learning and TF-IDF              |
| **NLTK**         | Text preprocessing                       |
| **Pandas**       | Dataset processing                       |
| **NumPy**        | Numerical operations                     |
| **Pickle**       | Saving trained model                     |
| **HTML5**        | Web page structure                       |
| **CSS3**         | Web page styling and responsive design   |
| **JavaScript**   | Frontend interaction and validation      |

---

## 🧠 Machine Learning Workflow

```text
Email Dataset
      ↓
Text Preprocessing
      ↓
Remove Noise
      ↓
Stopword Removal
      ↓
Stemming
      ↓
TF-IDF Feature Extraction
      ↓
Machine Learning Model
      ↓
Model Evaluation
      ↓
Save Trained Model
      ↓
Flask Backend
      ↓
HTML + CSS + JavaScript
      ↓
User Enters Email
      ↓
Spam / Not Spam Prediction
```

---

## 📂 Project Structure

```text
spam-email-classifier/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── dataset/
│   └── spam.csv
│
├── models/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## 🔤 Text Preprocessing

The email text is cleaned before sending it to the machine learning model.

### Preprocessing Steps

1. Convert text to lowercase.
2. Remove URLs.
3. Remove email addresses.
4. Remove numbers.
5. Remove punctuation.
6. Remove extra spaces.
7. Remove stopwords.
8. Apply stemming.

Example:

```text
Original:
Congratulations! You have won $1000. Click here to claim your prize.

After preprocessing:
congratul won click claim prize
```

---

## 📊 Feature Extraction

### TF-IDF

TF-IDF (**Term Frequency-Inverse Document Frequency**) converts email text into numerical features that can be processed by the machine learning model.

```text
Email Text
    ↓
Text Preprocessing
    ↓
TF-IDF Vectorizer
    ↓
Numerical Features
    ↓
ML Model
```

---

## 🤖 Machine Learning

The project uses a classification algorithm to distinguish between spam and legitimate emails.

Possible classification algorithms include:

* Multinomial Naive Bayes
* Logistic Regression
* Support Vector Machine (SVM)

The trained model is saved as:

```text
models/spam_model.pkl
```

The TF-IDF vectorizer is saved as:

```text
models/vectorizer.pkl
```

---

## 🌐 Web Application

The web application is developed using **Flask**.

### Frontend

The frontend uses:

* HTML5
* CSS3
* JavaScript

### Backend

The backend uses:

* Python
* Flask
* Machine Learning model

### Working

```text
User enters email
       ↓
JavaScript validates input
       ↓
Flask receives email
       ↓
Python preprocesses text
       ↓
TF-IDF converts text
       ↓
ML model predicts
       ↓
Result displayed on webpage
```

---

## 🎨 Frontend

### HTML

HTML is used to create:

* Email input area
* Predict button
* Result section
* Navigation/content structure

### CSS

CSS is used for:

* Page design
* Colors
* Buttons
* Cards
* Responsive layout
* User interface styling

### JavaScript

JavaScript is used for:

* Input validation
* Button interaction
* Form handling
* Dynamic prediction result
* Improving user experience

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Open Project

```bash
cd spam-email-classifier
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Train the Model

Run:

```bash
python train_model.py
```

This will:

* Load the dataset
* Preprocess email text
* Generate TF-IDF features
* Train the classifier
* Evaluate the model
* Save the trained model

---

## ▶️ Run the Application

Run:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

---

## 🧪 Example

### Spam Email

```text
Congratulations! You have won a free prize.
Click here to claim your reward.
```

Prediction:

```text
🚫 Spam Email
```

### Normal Email

```text
Hello, please send me the project report.
```

Prediction:

```text
✅ Not Spam
```

---

## 📈 Model Evaluation

The model can be evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

These metrics help measure the performance of the spam classification model.

---

## 💡 Real-World Applications

* Email spam filtering
* Phishing detection
* Email security
* Enterprise email management
* Cybersecurity applications
* Automated email classification

---

## 🎓 Skills Learned

* Python Programming
* Machine Learning
* Natural Language Processing
* Text Preprocessing
* TF-IDF Feature Extraction
* Classification Algorithms
* Model Evaluation
* Flask
* HTML
* CSS
* JavaScript
* Git and GitHub

---

## 🔮 Future Improvements

* Add phishing URL detection
* Add attachment analysis
* Add BERT/deep learning models
* Add prediction confidence score
* Support multiple languages
* Improve UI/UX
* Deploy the application online
* Use a larger dataset

---

## 👩‍💻 Author

**Kumkum Kumari**

B.Tech Computer Science & Engineering
Specialization: Artificial Intelligence & Machine Learning

---

## 📌 Project Summary

**Spam Email Classifier** combines **Machine Learning, NLP, Python, Flask, HTML, CSS, and JavaScript** to create an automated email spam detection system.

```text
Python + Machine Learning
          +
       Flask
          +
HTML + CSS + JavaScript
          ↓
Spam Email Classifier
```
