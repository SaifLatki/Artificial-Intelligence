import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Load the data
df = pd.read_csv(r"C:/Users/hp/Desktop/datasets/Home_Prices.csv")
print("Data loaded successfully")

df=df.dropna()
print(f'Dataset after removing missing values: {df.shape}')
