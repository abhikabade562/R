import numpy as np

def min_max_scaling(data):
    min_val = np.min(data)
    max_val = np.max(data)
    scaled_data = (data - min_val) / (max_val - min_val)
    return scaled_data

def z_score_normalization(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    normalized_data = (data - mean) / std_dev
    return normalized_data

input_data = input("Enter your no: ")
data_list = list(map(float, input_data.split()))

data = np.array(data_list)


min_max_scaled_data = min_max_scaling(data)
print("Min-max scaled data:", min_max_scaled_data)


z_score_normalized_data = z_score_normalization(data)
print("Z-score normalized data:", z_score_normalized_data)
