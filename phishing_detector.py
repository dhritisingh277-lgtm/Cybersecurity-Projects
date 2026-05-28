from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Sample email dataset
emails = [
    "Win a free iPhone now",
    "Your bank account has been hacked",
    "Claim your lottery prize",
    "Meeting scheduled for tomorrow",
    "Project submission is due",
    "Update your password immediately",
    "Congratulations! You won money",
    "Let's have lunch tomorrow",
    "Click here to verify your account",
    "Team meeting at 5 PM"
]

# Labels
# 1 = Phishing
# 0 = Safe
labels = [1,1,1,0,0,1,1,0,1,0]

# Convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.3, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Test custom email
test_email = ["Click here to win free cash"]

test_data = vectorizer.transform(test_email)

prediction = model.predict(test_data)

print("\nEmail:", test_email[0])

if prediction[0] == 1:
    print("Result: Phishing Email 🚨")
else:
    print("Result: Safe Email ✅")