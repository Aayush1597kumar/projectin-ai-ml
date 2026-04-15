#  Sentiment Analysis using NLP (TF-IDF + Naive Bayes)

##  About This Project

This is a simple and beginner-friendly **Sentiment Analysis project** built using Python.
The main idea is to understand how machines can read human text and decide whether the sentiment is **positive** or **negative**.

Instead of using complex models, this project focuses on **basic concepts of NLP**, making it easy to learn and explain in exams or interviews.

---

##  What It Can Do

* Accept multiple user reviews as input
* Predict whether each review is **Positive** or **Negative**
* Keep count of total positive and negative reviews
* Show a final summary at the end

---

##  Tech Stack

* **Python**
* **Pandas** → for handling data
* **Scikit-learn** → for machine learning

  * TF-IDF Vectorizer
  * Naive Bayes Classifier

---

##  How It Works (Simple Explanation)

The whole system follows a simple pipeline:

```
User Input → Convert Text to Numbers → Apply ML Model → Get Sentiment
```

### Step 1: Create Dataset

We start with a small dataset of sentences labeled as:

* Positive
* Negative

This helps the model learn patterns.

---

### Step 2: Convert Text into Numbers

Since machines don’t understand text directly, we use **TF-IDF** to convert words into numerical values.

Example:

* "love" → higher positive weight
* "hate" → higher negative weight

---

### Step 3: Train the Model

We use **Naive Bayes**, which is a simple and effective algorithm for text classification.

The model learns:

* Which words indicate positive sentiment
* Which words indicate negative sentiment

---

### Step 4: Take User Input

The user can enter multiple reviews one by one.

---

### Step 5: Predict Sentiment

Each input is:

* Converted into numbers using TF-IDF
* Passed into the trained model
* Classified as **positive** or **negative**

---

### Step 6: Show Final Result

At the end, the program displays:

* Total Positive Reviews
* Total Negative Reviews

---

##  How to Run the Project

1. Install required libraries:

```
pip install pandas scikit-learn
```

2. Run the Python file:

```
python sentiment_analysis.py
```

3. Enter reviews:

```
Enter review: I love this product
Sentiment: positive

Enter review: This is bad
Sentiment: negative
```

4. Type `done` to stop and see results.

---

##  Example

**Input:**

```
I love this product
Worst experience ever
```

**Output:**

```
Sentiment: positive
Sentiment: negative
```

---

##  Future Improvements

* Add more data to improve accuracy
* Include a **Neutral** category
* Try other models like Logistic Regression
* Build a simple GUI or web app

---

##  What I Learned

* Basics of **Natural Language Processing (NLP)**
* How to convert text into numbers using TF-IDF
* How Naive Bayes works for classification
* How a simple ML pipeline is built

---

##  Final Thoughts

This project is a great starting point for understanding how sentiment analysis works.
It is simple, easy to implement, and perfect for beginners who are getting started with NLP and Machine Learning.

---

