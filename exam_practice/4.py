from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

# Load & split
iris = load_iris()
X, y = iris.data, iris.target
names = iris.target_names
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

# Train & predict
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

# Separate correct & wrong
correct, wrong = [], []
for i in range(len(y_test)):
    line = f"Sample {i+1:02d} | Actual: {names[y_test[i]]:<10} | Predicted: {names[y_pred[i]]}"
    if y_test[i] == y_pred[i]:
        correct.append(line)
    else:
        wrong.append(line)

# Print results
print(f"=== CORRECT ({len(correct)}) ===")
for item in correct[:5]:
    print(item)
if len(correct) > 5:
    print("... (more correct) ...")

print(f"\n=== WRONG ({len(wrong)}) ===")
for item in wrong:
    print(item)

print(f"\nAccuracy: {knn.score(X_test, y_test)*100:.2f}%")

# Scatterplot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
colors = ['blue', 'orange', 'green']

# Left: Actual
for i, name in enumerate(names):
    ax1.scatter(X_test[y_test==i, 2], X_test[y_test==i, 3], c=colors[i], label=name)
ax1.set_title("Actual Labels")
ax1.set_xlabel("Petal length")
ax1.set_ylabel("Petal width")
ax1.legend()

# Right: Predicted (X = wrong)
for i, name in enumerate(names):
    correct_mask = (y_pred == i) & (y_test == y_pred)
    wrong_mask   = (y_pred == i) & (y_test != y_pred)
    ax2.scatter(X_test[correct_mask, 2], X_test[correct_mask, 3], c=colors[i], marker='o', label=f"{name} correct")
    ax2.scatter(X_test[wrong_mask, 2],   X_test[wrong_mask, 3],   c=colors[i], marker='X', s=100, edgecolors='red', label=f"{name} wrong")
ax2.set_title(f"Predictions (Acc: {knn.score(X_test, y_test)*100:.1f}%)")
ax2.set_xlabel("Petal length")
ax2.set_ylabel("Petal width")
ax2.legend(fontsize=8)

plt.tight_layout()
plt.show()
