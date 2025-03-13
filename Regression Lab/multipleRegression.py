import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the data
data = {
    'years_experince': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'age': [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    'education_level': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'salary': [45000, 50000, 60000, 80000, 110000, 150000, 200000, 300000, 500000, 1000000]
}

df = pd.DataFrame(data)

# Split the data
X = df[['years_experince', 'age', 'education_level']]
y = df['salary'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')


# Plot predicted vs actual salaries
plt.scatter(y_test, y_test, color='black', label='Actual Salary')
plt.scatter(y_test, y_pred, color='red', label='Predicted Salary')
plt.plot(y_test, y_test, color='black', linewidth=2,linestyle='dashed', label='Actual Salary')
plt.plot(y_test, y_pred, color='red', linewidth=2, linestyle='dashed', label='Predicted Salary')

plt.xlabel("Actual Salary")
plt.ylabel("Predicted Salary")
plt.title("Multiple Regression: Predicted vs Actual Salary")
plt.legend()
plt.show()
