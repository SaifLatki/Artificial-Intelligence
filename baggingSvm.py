import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load and preprocess data
data = pd.read_csv('../datasets/IMDB_Dataset.csv')
data.dropna(inplace=True)

x = data['review']
y = data['sentiment']


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Vectorize text data
vectorizer = TfidfVectorizer(stop_words='english', max_features=200)
x_train = vectorizer.fit_transform(x_train)
x_test = vectorizer.transform(x_test)

# Train AdaBoost model with Decision Tree as base estimator
adaboost_model = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=1),
    n_estimators=50,
    random_state=42
)

adaboost_model.fit(x_train, y_train)
y_pred_ada = adaboost_model.predict(x_test)

bagging_model = BaggingClassifier(
    estimator=DecisionTreeClassifier(max_depth=1),
    n_estimators=50,
    random_state=42
)

bagging_model.fit(x_train, y_train)
y_pred_bagg = bagging_model.predict(x_test)

print("AdaBoost Model")
accuracy = accuracy_score(y_test, y_pred_ada)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("Bagging Model")
accuracy = accuracy_score(y_test, y_pred_bagg)
print(f"Accuracy: {accuracy * 100:.2f}%")
