import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

# Read CSV file
data = pd.read_csv("data.csv")

# K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(data)

# EM
em = GaussianMixture(n_components=3, random_state=42)
em_labels = em.fit_predict(data)

# Calculate clustering quality
kmeans_score = silhouette_score(data, kmeans_labels)
em_score = silhouette_score(data, em_labels)

print("K-Means Silhouette Score:", kmeans_score)
print("EM Silhouette Score:", em_score)

# Compare results
if kmeans_score > em_score:
    print("K-Means gives better clustering quality.")
else:
    print("EM gives better clustering quality.")
