

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Expanded dataset (better accuracy)
data = {
    "text": [
        "I love this product", "This is amazing", "I am very happy",
        "I hate this", "This is terrible", "Very bad experience",

        "Great service", "Amazing food", "Loved the experience",
        "Worst service ever", "Not good at all", "Very poor quality",

        "Great workout today", "I feel strong after gym",
        "Had an awesome workout", "Feeling powerful after lifting",

        "Bad food", "Terrible taste", "I am disappointed",
        "Excellent service", "Really enjoyed", "Superb experience"
    ],
    "label": [
        "positive","positive","positive",
        "negative","negative","negative",

        "positive","positive","positive",
        "negative","negative","negative",

        "positive","positive","positive","positive",

        "negative","negative","negative",
        "positive","positive","positive"
    ]
}

df = pd.DataFrame(data)

# Convert text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# Train model
model = MultinomialNB()
model.fit(X, y)

print(" Model is ready!")

# Counters
positive_count = 0
negative_count = 0

print("\n Enter multiple reviews (type 'done' to finish)\n")

# Loop for multiple inputs
while True:
    user_input = input("Enter review: ")

    if user_input.lower() == "done":
        break

    input_data = vectorizer.transform([user_input])
    prediction = model.predict(input_data)[0]

    print("Sentiment:", prediction)

    if prediction == "positive":
        positive_count += 1
    else:
        negative_count += 1

# Final Summary
print("\n Final Report:")
print("Total Positive Reviews:", positive_count)
print("Total Negative Reviews:", negative_count)