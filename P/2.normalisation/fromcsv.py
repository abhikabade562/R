import numpy as np
import pandas as pd

def min_max_scaling(data, new_min=0, new_max=1):
    min_val = np.min(data)
    max_val = np.max(data)
    scaled_data = (data - min_val) * (new_max - new_min) / (max_val - min_val) + new_min
    return scaled_data

def z_score_normalization(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    normalized_data = (data - mean) / std_dev
    return normalized_data

# Read input data from the CSV file, skipping the header row
file_path = 'norm.csv'  # Replace with the correct path to your CSV file
data = pd.read_csv(file_path, header=0)  # Assuming header is in the first row

# Iterate through columns to find numeric data and extract it
numeric_data = []
for col in data.columns:
    numeric_col = pd.to_numeric(data[col], errors='coerce')
    numeric_col = numeric_col.dropna()  # Remove NaN values
    numeric_data.extend(numeric_col)

numeric_data = np.array(numeric_data)

min_max_scaled_data = min_max_scaling(numeric_data)
print("Min-max scaled data (default range 0-1):", min_max_scaled_data)

new_min = float(input("Enter the new minimum value for min-max scaling: "))
new_max = float(input("Enter the new maximum value for min-max scaling: "))
custom_min_max_scaled_data = min_max_scaling(numeric_data, new_min, new_max)
print(f"Min-max scaled data (custom range {new_min}-{new_max}):", custom_min_max_scaled_data)

z_score_normalized_data = z_score_normalization(numeric_data)
print("Z-score normalized data:", z_score_normalized_data)

