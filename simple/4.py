from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load data
iris = load_iris()
X, y = iris.data, iris.target
names = iris.target_names

# Split (60% train, 40% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

# Train KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict
y_pred = knn.predict(X_test)

# Separate correct & wrong
correct, wrong = [], []

for i in range(len(y_test)):
    actual = names[y_test[i]]
    pred = names[y_pred[i]]
    line = f"Sample {i+1:02d} | Actual: {actual:<10} | Predicted: {pred}"

    if y_test[i] == y_pred[i]:
        correct.append(line)
    else:
        wrong.append(line)

# Print results
print(f"=== CORRECT PREDICTIONS ({len(correct)}) ===")
for item in correct[:5]:          # show only first 5 for readability
    print(item)
if len(correct) > 5:
    print("... (more correct predictions) ...")

print(f"\n=== WRONG PREDICTIONS ({len(wrong)}) ===")
if not wrong:
    print("None! Perfect accuracy.")
else:
    for item in wrong:
        print(item)

print(f"\nAccuracy: {knn.score(X_test, y_test)*100:.2f}%")
