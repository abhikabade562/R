import numpy as np

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

input_data = input("Enter your numbers separated by space: ")
data_list = list(map(float, input_data.split()))

data = np.array(data_list)

min_max_scaled_data = min_max_scaling(data)
print("Min-max scaled data (default range 0-1):", min_max_scaled_data)

new_min = float(input("Enter the new minimum value for min-max scaling: "))
new_max = float(input("Enter the new maximum value for min-max scaling: "))
custom_min_max_scaled_data = min_max_scaling(data, new_min, new_max)
print(f"Min-max scaled data (custom range {new_min}-{new_max}):", custom_min_max_scaled_data)

z_score_normalized_data = z_score_normalization(data)
print("Z-score normalized data:", z_score_normalized_data)

