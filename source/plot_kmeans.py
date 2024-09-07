# plot_kmeans.py

import matplotlib.pyplot as plt
from perform_kmeans import perform_kmeans
from read_and_check_data import customer_dataset


def plot_clusters():
    # Get the clustering results
    y_kmeans, kmeans = perform_kmeans()

    # Assuming you have the original data loaded (Annual Income and Spending Score)
    x = customer_dataset()[["Annual_Income_(k$)", "Spending_Score"]].values  # Correct dataset for plotting

    # Plot the clusters
    plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s=100, c='pink', label='Cluster 1')
    plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s=100, c='yellow', label='Cluster 2')
    plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s=100, c='red', label='Cluster 3')
    plt.scatter(x[y_kmeans == 3, 0], x[y_kmeans == 3, 1], s=100, c='orange', label='Cluster 4')
    plt.scatter(x[y_kmeans == 4, 0], x[y_kmeans == 4, 1], s=100, c='green', label='Cluster 5')

    # Plot the centroids
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='black', label='Centroids')

    plt.title('Clusters of customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend()
    plt.show()


# Call the function to plot clusters
plot_clusters()
