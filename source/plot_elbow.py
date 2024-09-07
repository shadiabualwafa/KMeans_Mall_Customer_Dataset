# plot_elbow.py

import matplotlib.pyplot as plt
from determine_k import determine_k


def plot_elbow():
    # Get the WCSS values by calling determine_k()
    wc_ss = determine_k()

    # Plot the Elbow Method graph
    plt.figure(figsize=(10, 5))
    plt.plot(range(1, 11), wc_ss)
    plt.title('The Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()


# Call the plot_elbow function to display the graph
plot_elbow()
