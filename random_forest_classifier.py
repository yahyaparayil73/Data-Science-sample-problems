import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample Data
data = {
    'Study_Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Pass':        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[['Study_Hours']]
y = df['Pass']

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Random Forest Model
model = RandomForestClassifier(
    n_estimators=10,   # Number of trees
    random_state=42
)

# Train Model
model.fit(X_train, y_train)

# Make Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Predictions:", y_pred)
print("Actual:", y_test.values)
print("Accuracy:", accuracy)

# Predict for a new student
new_student = [[6]]
result = model.predict(new_student)

if result[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")