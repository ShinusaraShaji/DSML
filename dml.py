import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, accuracy_score, f1_score

# Read Excel file
data = pd.read_excel(
    r'C:\Users\MCETCSE\Desktop\DSML\knn\Book1.xlsx'
)

print(data)

# Features and target
X = data[['Feature1', 'Feature2']]
y = data['Class']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Prediction
y_pred = knn.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Precision
precision = precision_score(
    y_test, y_pred, average='macro', zero_division=1
)
print("Precision:", precision)

# F1 score
f1 = f1_score(
    y_test, y_pred, average='macro', zero_division=1
)
print("F1:", f1)

# Predict new sample
new_sample = pd.DataFrame(
    [[6, 4]],
    columns=['Feature1', 'Feature2']
)

new_prediction = knn.predict(new_sample)

print("\nTomato is a:", new_prediction[0])