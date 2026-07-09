import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# =====================================================
# STEP 1: CREATE DATASET
# =====================================================

df = pd.DataFrame({
    "Name": [
        "Ahmed", "Ali", "Yahya", "Fathima", "Rahul",
        "Aisha", "John", "Sara", "Nabeel", "Anu"
    ],

    "Age": [
        25, 30, 35, 28, 40,
        26, 32, 29, 38, 27
    ],

    "Experience": [
        2, 5, 8, 3, 12,
        2, 6, 4, 10, 3
    ],

    "Department": [
        "IT", "HR", "IT", "Finance", "IT",
        "HR", "Finance", "IT", "HR", "Finance"
    ],

    "Salary": [
        30000, 50000, 80000, 40000, 120000,
        35000, 65000, 55000, 100000, 45000
    ]
})

print("ORIGINAL DATASET")
print(df)

# =====================================================
# STEP 2: FEATURE ENGINEERING
# =====================================================

df["Exp_Age_Ratio"] = df["Experience"] / df["Age"]

print("\nAFTER FEATURE ENGINEERING")
print(df)

# =====================================================
# STEP 3: FEATURE SELECTION
# =====================================================

df.drop("Name", axis=1, inplace=True)

print("\nAFTER FEATURE SELECTION")
print(df)

# =====================================================
# STEP 4: ENCODING
# =====================================================

df = pd.get_dummies(df, columns=["Department"])

print("\nAFTER ENCODING")
print(df)

# =====================================================
# STEP 5: SPLIT FEATURES AND TARGET
# =====================================================

X = df.drop("Salary", axis=1)

y = df["Salary"]

print("\nFEATURES (X)")
print(X.head())

print("\nTARGET (y)")
print(y.head())

# =====================================================
# STEP 6: TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)

# =====================================================
# STEP 7: STANDARD SCALER
# =====================================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# =====================================================
# STEP 8: TRAIN MODEL
# =====================================================

model = LinearRegression()

model.fit(X_train, y_train)

# =====================================================
# STEP 9: PREDICTION
# =====================================================

y_pred = model.predict(X_test)

print("\nPREDICTION")

for actual, predicted in zip(y_test, y_pred):
    print(
        f"Actual Salary: {actual:,.0f} | "
        f"Predicted Salary: {predicted:,.0f}"
    )

# =====================================================
# STEP 10: EVALUATION
# =====================================================

print("\nMODEL PERFORMANCE")

print("R2 Score:", r2_score(y_test, y_pred))

print("MSE:", mean_squared_error(y_test, y_pred))