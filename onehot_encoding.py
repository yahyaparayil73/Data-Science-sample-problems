import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

df = pd.read_excel('datasets/restaurant_dataset_100_rows.xlsx')

# df =  pd.get_dummies(df,columns=['listed_in'])
df = df.drop('name',axis=1)

for col in df.columns:

    if df[col].dtype == "str":

        print("Encoding:", col)

        df = pd.get_dummies(df, columns=[col])

print(df.head())        

# print(df.dtypes)
