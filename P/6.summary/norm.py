import numpy as np
import matplotlib.pyplot as plt

# Input data from user
data = input("Enter space-separated numbers: ")
data_list = list(map(float, data.split()))

# Normalizing the data between 0 and 1
normalized_data = (data_list - np.min(data_list)) / (np.max(data_list) - np.min(data_list))

minimum = np.min(normalized_data)
first_quartile = np.percentile(normalized_data, 25)
median = np.median(normalized_data)
third_quartile = np.percentile(normalized_data, 75)
maximum = np.max(normalized_data)
mean = np.mean(normalized_data)
iqr = third_quartile - first_quartile

print(f"Minimum value (normalized): {minimum}")
print(f"First quartile (25th percentile - normalized): {first_quartile}")
print(f"Median (50th percentile - normalized): {median}")
print(f"Third quartile (75th percentile - normalized): {third_quartile}")
print(f"Maximum value (normalized): {maximum}")
print(f"Mean (normalized): {mean}")
print(f"IQR (Interquartile Range - normalized): {iqr}")

# Create a boxplot of normalized data
plt.boxplot(normalized_data)
plt.title('Boxplot of the Normalized Data')

# Plotting annotations for minimum, maximum, quartiles, median, mean, and IQR on the normalized boxplot
plt.text(1, minimum, f'Min (normalized): {minimum:.2f}', verticalalignment='bottom', horizontalalignment='right')
plt.text(1, maximum, f'Max (normalized): {maximum:.2f}', verticalalignment='top', horizontalalignment='right')
plt.text(1, first_quartile, f'Q1 (normalized): {first_quartile:.2f}', verticalalignment='bottom', horizontalalignment='right')
plt.text(1, third_quartile, f'Q3 (normalized): {third_quartile:.2f}', verticalalignment='top', horizontalalignment='right')
plt.text(1, median, f'Median (normalized): {median:.2f}', verticalalignment='bottom', horizontalalignment='right')
plt.text(1, mean, f'Mean (normalized): {mean:.2f}', verticalalignment='bottom', horizontalalignment='left')
plt.text(1, first_quartile + 0.1 * iqr, f'IQR (normalized): {iqr:.2f}', verticalalignment='bottom', horizontalalignment='left')

plt.show()

