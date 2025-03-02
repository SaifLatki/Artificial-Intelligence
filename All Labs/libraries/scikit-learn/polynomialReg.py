import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x=np.array([[1],[2],[3],[4],[5]])
y=np.array([30000,35000,40000,45000,50000])

poly=PolynomialFeatures(degree=2)
x_poly=poly.fit_transform(x)

model=LinearRegression()
model.fit(x_poly,y)

#predictions
X_range=np.linspace(1,6,100).reshape(-1,1)
X_range_poly=poly.transform(X_range)
y_pred=model.predict(X_range_poly)

#plot
plt.scatter(x,y, color='blue',label='Actual data')
plt.plot(X_range,y_pred,color='red',label='Polynomial fit (Degree=2)')
plt.xlabel("years of Experience")
plt.ylabel("Salary ($1000s)")
plt.legend()
plt.show()