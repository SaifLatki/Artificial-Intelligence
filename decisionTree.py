from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Split the data into training and testing sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Decision Tree classifier
model = DecisionTreeClassifier(criterion='gini', max_depth=3)

# Train the model
model.fit(X_train, y_train)

# Predict the results on the test data
y_pred = model.predict(X_test)

# Calculate and display accuracy
print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred))
