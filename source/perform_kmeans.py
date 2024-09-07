# perform_kmeans.py

#based on previous plot, K = 5
##performing K-Means clustering with 5 clusters:

from sklearn.cluster import KMeans
from read_and_check_data import customer_dataset


def perform_kmeans():
    # Load the dataset and extract the relevant columns (Annual Income and Spending Score)
    x = customer_dataset()[["Annual_Income_(k$)", "Spending_Score"]].values  # Correct dataset for clustering

    # Initialize and perform KMeans clustering with 5 clusters
    kmeans = KMeans(n_clusters=5, random_state=56)
    y_kmeans = kmeans.fit_predict(x)

    # Return the cluster labels and the KMeans object
    return y_kmeans, kmeans

