import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = fetch_california_housing()
df = pd.DataFrame(data.data,columns=data.feature_names)
# print(df)



scaler = StandardScaler()

scaled_data = scaler.fit_transform(df)

# print(scaled_data)



scaled_df = pd.DataFrame(scaled_data,columns = df.columns)                      

# print(scaled_df)

x = df


# print(data.target)

df['housevalue'] = data.target

# print(df['housevalue'])

x = df.drop('housevalue',axis = 1)
y = df['housevalue']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = LinearRegression()

model.fit(x_train,y_train)
y_pred = model.predict(x_test)

print(y_pred)



















