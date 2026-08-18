import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

# Load data (Iris)
data = load_iris().data
X = StandardScaler().fit_transform(data)
X_2d = PCA(2).fit_transform(X)

# K-Means
kmeans = KMeans(3, random_state=42, n_init=10).fit(X)
km_labels = kmeans.labels_

# EM (GMM)
gmm = GaussianMixture(3, random_state=42, n_init=10).fit(X)
gmm_labels = gmm.predict(X)

# Scores
print("K-Means Silhouette:", round(silhouette_score(X, km_labels), 4))
print("EM Silhouette:    ", round(silhouette_score(X, gmm_labels), 4))

# Plot
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
ax[0].scatter(X_2d[:,0], X_2d[:,1], c=km_labels, cmap='viridis')
ax[0].set_title("K-Means")
ax[1].scatter(X_2d[:,0], X_2d[:,1], c=gmm_labels, cmap='viridis')
ax[1].set_title("EM (GMM)")
plt.show()
