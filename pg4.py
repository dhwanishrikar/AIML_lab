# Write a program to implement KNN algorithm to classify the iris dataset. print both correct and wrong predictions

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# 1. Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# 2. Convert to DataFrame and display the first few rows
df = pd.DataFrame(data=X, columns=iris.feature_names)
df['species_id'] = y
df['species_name'] = df['species_id'].apply(lambda x: target_names[x])

print("=== FIRST FEW ROWS OF THE DATASET ===")
print(df.head())
print("\n" + "="*60 + "\n")

# 3. Split dataset (60% train, 40% test) to deliberately introduce boundary difficulty
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

# 4. Initialize and train the KNN Classifier (k=5)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 5. Predict on the test data
y_pred = knn.predict(X_test)

# 6. Separate predictions into correct and wrong lists
correct_list = []
wrong_list = []

for i in range(len(y_test)):
    actual_name = target_names[y_test[i]]
    pred_name = target_names[y_pred[i]]
    features = X_test[i]
    
    log_entry = f"Sample #{i+1:02d} | Features: {features} | Actual: {actual_name:<10} | Predicted: {pred_name:<10}"
    
    if y_test[i] == y_pred[i]:
        correct_list.append(log_entry)
    else:
        wrong_list.append(log_entry)

# 7. Print separated categories
print(f"=== CORRECT PREDICTIONS ({len(correct_list)} samples) ===")
# Showing first few correct samples to save terminal space, prints all if desired
for item in correct_list[:5]: 
    print(item)
print("... [truncated for readability] ...")

print(f"\n=== WRONG PREDICTIONS ({len(wrong_list)} samples) ===")
if not wrong_list:
    print("None! Perfect accuracy.")
else:
    for item in wrong_list:
        print(item)

print("\n" + "="*60)
# 8. Print ultimate performance summary
accuracy = knn.score(X_test, y_test) * 100
print(f"Final Model Accuracy: {accuracy:.2f}%")
