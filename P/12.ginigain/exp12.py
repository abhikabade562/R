import pandas as pd
import math

# Function to calculate entropy
def calculate_entropy(data, class_column):
    class_counts = data[class_column].value_counts()
    entropy = 0

    for count in class_counts:
        probability = count / len(data)
        entropy -= probability * math.log2(probability)

    return entropy

# Function to calculate Gini index
def calculate_gini_index(data, class_column):
    class_counts = data[class_column].value_counts()
    gini_index = 1

    for count in class_counts:
        probability = count / len(data)
        gini_index -= probability ** 2

    return gini_index

# Function to calculate Information Gain for a given attribute
def calculate_gain(data, attribute, class_column):
    total_entropy = calculate_entropy(data, class_column)

    attribute_entropy = 0
    attribute_values = data[attribute].unique()

    for value in attribute_values:
        subset = data[data[attribute] == value]
        subset_entropy = calculate_entropy(subset, class_column)
        weight = len(subset) / len(data)
        attribute_entropy += weight * subset_entropy

    information_gain = total_entropy - attribute_entropy
    return information_gain

# Function to calculate Gini Gain for a given attribute
def calculate_gini_gain(data, attribute, class_column):
    total_gini = calculate_gini_index(data, class_column)

    attribute_gini = 0
    attribute_values = data[attribute].unique()

    for value in attribute_values:
        subset = data[data[attribute] == value]
        subset_gini = calculate_gini_index(subset, class_column)
        weight = len(subset) / len(data)
        attribute_gini += weight * subset_gini

    gini_gain = total_gini - attribute_gini
    return gini_gain

# Load data from CSV
file_path = 'input_data.csv'  # Replace with your CSV file path
data = pd.read_csv(file_path)

# Target class column
class_column_name = 'PlayTennis'

# Calculate Information Gain and Gini Gain for each attribute
all_attributes = list(data.columns)
all_attributes.remove(class_column_name)

for attribute in all_attributes:
    information_gain = calculate_gain(data, attribute, class_column_name)
    gini_gain = calculate_gini_gain(data, attribute, class_column_name)
    print(f"For Attribute '{attribute}':")
    print(f"Information Gain: {information_gain}")
    print(f"Gini Gain: {gini_gain}")
    print("\n")

