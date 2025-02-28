import pandas as pd

df=pd.read_csv('C:/Users/hp/Desktop/dirtydata.csv')

print("information:\n ",df.info())
print("content: \n",df.describe())
print ("first five values:\n ",df.head())
print("last five values:\n ",df.tail())
print("Missing Values: \n",df.isnull().sum())
print("fill missing values with mean: \n",df.fillna(df["Calories"].mean(),inplace=True))
print("Remove the duplicate values: \n",df.drop_duplicates(inplace=True))
df2=df[(df['Pulse'] >= 50) & (df['Pulse'] <= 200)]
print("Remove extreme and check for outliers: \n", df2)

# Save the cleaned DataFrame to a new CSV
df.to_csv('C:/Users/hp/Desktop/cleaned_data.csv', index=False)


corelation_matrix=df.corr()
print("Correlation matrix:\n", corelation_matrix)



