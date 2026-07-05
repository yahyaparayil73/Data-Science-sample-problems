import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

df = pd.read_excel('datasets/restaurant_dataset_100_rows.xlsx')
# print(df)
# print(df.head())

# plt.bar(x=df["listed_in"])
# plt.show()  

le = LabelEncoder()

for col in df.columns:
    if df[col].dtype == "str":
        print('yahyaparayil')
        df[col] = le.fit_transform(df[col])

print(df.tail())

# print(df.dtypes)
