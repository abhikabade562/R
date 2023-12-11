import numpy as np
import pandas as pd

# Read data from the CSV file
file_path = 'norm.csv'
data = pd.read_csv(file_path)['Values'].values  # Replace 'column_name' with the appropriate column name in your CSV file

# equal frequency
num_bins = 3
data_sorted = np.sort(data)
bins = np.array_split(data_sorted, num_bins)

# Display equal frequency
print("Partition using equal frequency approach:")
for i, bin_values in enumerate(bins):
    print(f"Bin {i + 1}:", ", ".join(map(str, bin_values)))

# bin means
bin_means = [int(np.mean(bin_values)) for bin_values in bins]
smoothed_means = np.repeat(bin_means, len(data) // num_bins)

# Display bin means
print("\nSmoothing by bin means:")
for i, mean_value in enumerate(smoothed_means):
    print(f"Bin {i // (len(data) // num_bins) + 1}:", mean_value, end=", " if (i+1) % (len(data) // num_bins) != 0 else "\n")

# bin boundaries
bin_boundaries = np.zeros((num_bins, len(data) // num_bins))

for i in range(0, len(data), len(data) // num_bins):
    k = i // (len(data) // num_bins)
    for j in range(len(data) // num_bins):
        if (data_sorted[i + j] - data_sorted[i]) < (data_sorted[i + len(data) // num_bins - 1] - data_sorted[i + j]):
            bin_boundaries[k, j] = data_sorted[i]
        else:
            bin_boundaries[k, j] = data_sorted[i + len(data) // num_bins - 1]

# Display bin boundaries
print("\nSmoothing by bin boundaries:")
for i in range(num_bins):
    print(f"Bin {i + 1}:", ", ".join(map(str, bin_boundaries[i])))
