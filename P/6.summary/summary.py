import numpy as np
import matplotlib.pyplot as plt

data = input("Enter data: ")
data_list = list(map(float, data.split()))

minimum = np.min(data_list)
first_quartile = np.percentile(data_list, 25)
median = np.median(data_list)
third_quartile = np.percentile(data_list, 75)
maximum = np.max(data_list)
mean = np.mean(data_list)
iqr = third_quartile - first_quartile

print(f"Minimum value: {minimum}")
print(f"First quartile (25th percentile): {first_quartile}")
print(f"Median (50th percentile): {median}")
print(f"Third quartile (75th percentile): {third_quartile}")
print(f"Maximum value: {maximum}")
print(f"Mean: {mean}")
print(f"IQR (Interquartile Range): {iqr}")

# Create a boxplot
plt.boxplot(data_list)
plt.title('Boxplot of the Data')

# Plotting annotations for minimum, maximum, quartiles, median, mean, and IQR
plt.text(1, minimum, f'Min: {minimum}', verticalalignment='bottom', horizontalalignment='right')
plt.text(1, maximum, f'Max: {maximum}', verticalalignment='top', horizontalalignment='right')
plt.text(1, first_quartile, f'Q1: {first_quartile}', verticalalignment='bottom', horizontalalignment='right')
plt.text(1, third_quartile, f'Q3: {third_quartile}', verticalalignment='top', horizontalalignment='right')
plt.text(1, median, f'Median: {median}', verticalalignment='bottom', horizontalalignment='right')
plt.text(1, mean, f'Mean: {mean}', verticalalignment='bottom', horizontalalignment='left')


plt.show()

