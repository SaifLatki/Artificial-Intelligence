from sklearn.naive_bayes import GaussianNB
import numpy as np

# Sample continuous data (Hours Studied, Hours Slept)
X = np.array([[10, 6], [9, 5], [2, 9], [1, 10]])
y = np.array([1, 1, 0, 0])  # 1 = Pass, 0 = Fail

# Train GaussianNB model
gnb = GaussianNB()
gnb.fit(X, y)

# Predict for a new student
new_student = np.array([[4, 7]])  # 4 hours studied, 7 hours slept
print(gnb.predict(new_student))  # Output: [0] (Fail)"
   