import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# 1. Load data
wine = load_wine()
X = wine.data
y = wine.target
target_names = wine.target_names

# 2. Split data (60/40)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)

# 3. Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Train KNN Classifier
knn_clf = KNeighborsClassifier(n_neighbors=5)
knn_clf.fit(X_train_scaled, y_train)
y_pred = knn_clf.predict(X_test_scaled)

# 5. Separate for console logs
correct_list = []
wrong_list = []

for i in range(len(y_test)):
    entry = f"Actual: {target_names[y_test[i]]:<8} | Predicted: {target_names[y_pred[i]]:<8}"
    if y_test[i] == y_pred[i]:
        correct_list.append(entry)
    else:
        wrong_list.append(entry)

print(f"=== CORRECT CLASSIFICATIONS ({len(correct_list)}) ===")
print("\n".join(correct_list[:3]) + "\n... [truncated] ...")
print(f"\n=== WRONG CLASSIFICATIONS ({len(wrong_list)}) ===")
print("\n".join(wrong_list) if wrong_list else "None")
print(f"\nAccuracy: {knn_clf.score(X_test_scaled, y_test)*100:.2f}%\n")

# 6. Plotting Classification Results (Using first two features for 2D visualization)
plt.figure(figsize=(8, 5))
for i in range(len(y_test)):
    if y_test[i] == y_pred[i]:
        plt.scatter(
            X_test[i, 0],
            X_test[i, 1],
            color="green",
            marker="o",
            alpha=0.7,
            label="Correct" if i == 0 else "",
        )
    else:
        plt.scatter(
            X_test[i, 0],
            X_test[i, 1],
            color="red",
            marker="x",
            s=100,
            linewidths=2,
            label="Wrong" if i == 34 else "",
        )  # index 34 is a known error point

plt.title("KNN Classification: Correct vs Wrong Predictions")
plt.xlabel(wine.feature_names[0].capitalize())
plt.ylabel(wine.feature_names[1].capitalize())
plt.legend()
plt.grid(True)
plt.show()
