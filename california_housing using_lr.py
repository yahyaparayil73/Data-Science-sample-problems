import numpy as np
import pandas as pd
from  sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

import matplotlib as plt


data = fetch_california_housing()
df = pd.DataFrame(data.data,columns=data.feature_names)
# print(df)

# print(df.isnull().sum())

x = df
df["HouseValue"] = data.target
x = df.drop("HouseValue", axis=1)
y = df["HouseValue"]

# print(y)
# print(x)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

lr = LinearRegression()

lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)

print("R2 Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))

# Predict one house
sample = x_test.iloc[[0]]

prediction = lr.predict(sample)

print("Predicted Value:", prediction[0])
print("Actual Value:", y_test.iloc[0])









