from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np

x=np.array([[1],[2],[3],[4],[5]])
y=np.array([2,4,6,17,30])

poly=PolynomialFeatures(degree=2)
x_poly=poly.fit_transform(x)


model=LinearRegression()
model.fit(x_poly,y)

#predictions
x_new=np.array([[6]])
x_new_poly=poly.transform(x_new)
predicted_value=model.predict(x_new_poly)
print(predicted_value)