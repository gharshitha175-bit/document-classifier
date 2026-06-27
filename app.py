import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Read dataset
df = pd.read_csv("data.csv")

print("Training Data")
print(df)

# Convert text into numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

# Train model
model = MultinomialNB()
model.fit(X, df["category"])

while True:
    user_input = input("\nEnter document (or type exit): ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    new_vector = vectorizer.transform([user_input])

    prediction = model.predict(new_vector)

    print("Predicted Category:", prediction[0])