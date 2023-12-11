import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import dendrogram, linkage

# Load data from CSV
file_name = 'input_data.csv'  # Replace with your CSV file name
data = pd.read_csv(file_name, index_col=0)

# Perform hierarchical clustering using the provided distance matrix with complete linkage
condensed_dist_matrix = squareform(data.values)  # Convert to condensed distance matrix
linkage_matrix = linkage(condensed_dist_matrix, method='complete')

# Plot the dendrogram
plt.figure(figsize=(8, 6))  # Adjust size if needed
dendrogram(linkage_matrix, labels=data.index)
plt.title('Hierarchical Clustering Dendrogram (Complete Linkage)')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()

# Print pairs and minimum values at each step
print("Pairs and minimum values at each step:")
for i in range(len(linkage_matrix) - 1):
    print(f"Step {i+1}: Pairs: {linkage_matrix[i][:2]}, Minimum value: {linkage_matrix[i][2]}")

