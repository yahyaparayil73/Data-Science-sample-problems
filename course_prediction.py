import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error


df = pd.read_csv( 'datasets/Course_Completion_Prediction.csv')

# print(df.head())

# print(df.info)

# print(df.describe())

# print(df.columns)

# print(df.shape)

# print(df.dtypes)

# print(df.isnull().sum())

# sns.boxplot(x = df['Course_Duration_Days'])
# plt.show()

# sns.countplot(x = df['Gender'])
# plt.show()

# sns.countplot(x = df['Completed'])
# plt.show()

df = df.drop(["Student_ID","Name","Course_Name","City","Enrollment_Date"],axis=1)




for col in df.columns:
    if df[col].dtype == "str" :
        df = pd.get_dummies(df,columns=[col])

# print(df.columns)

print(df.head())

corr_matrix = df.corr(numeric_only=True)

sns.heatmap(corr_matrix)
plt.show()















    





