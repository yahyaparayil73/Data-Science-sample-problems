from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# Sample Dataset: Loan Eligibility
# Features: [Monthly Income (in INR), Credit Score, Existing Debt (in INR)]
X = [
    [85000, 750, 120000],
    [30000, 580, 450000],
    [120000, 810, 50000],
    [25000, 600, 200000],
    [95000, 720, 80000]
]
# Labels: 1 = Approved, 0 = Rejected
y = [1, 0, 1, 0, 1]

# 1. Initialize the Random Forest with 100 trees
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 2. Train the model
model.fit(X, y)

# 3. Predict for a new applicant (Income: ₹90,000, Credit Score: 740, Debt: ₹100,000)
new_applicant = [[90000, 740, 100000]]
prediction = model.predict(new_applicant)

print("Loan Status:", "Approved" if prediction[0] == 1 else "Rejected")