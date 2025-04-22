import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load and preprocess data
data = pd.read_csv('../datasets/IMDB_Dataset.csv')
data.dropna(inplace=True)

x = data['review']
y = data['sentiment']

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Vectorize text data
vectorizer = TfidfVectorizer(stop_words='english', max_features=200)
x_train = vectorizer.fit_transform(x_train)
x_test = vectorizer.transform(x_test)

# Train SVM model
svm_model = SVC(kernel='linear', C=1.0, random_state=42)
svm_model.fit(x_train, y_train)

# Predict and evaluate
y_pred = svm_model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
