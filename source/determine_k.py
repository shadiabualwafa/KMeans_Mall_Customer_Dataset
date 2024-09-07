# determine_k.py

from sklearn.cluster import KMeans
from read_and_check_data import customer_dataset


def determine_k():
    # Extract relevant columns (Annual Income and Spending Score)
    x = customer_dataset()[["Annual_Income_(k$)", "Spending_Score"]].values

    # List to store within-cluster sum of squares (WCSS)
    wc_ss = []
    for i in range(1, 11):
        kmeans_clu = KMeans(n_clusters=i, random_state=56)
        kmeans_clu.fit(x)
        wc_ss.append(kmeans_clu.inertia_)

    # Return the WCSS list
    return wc_ss
