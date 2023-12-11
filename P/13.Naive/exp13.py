import csv
from collections import defaultdict

# Function to calculate probabilities for each class and attribute value
def train(dataset):
    class_counts = defaultdict(int)
    attribute_counts = defaultdict(lambda: defaultdict(int))
    total_samples = 0

    for row in dataset:
        class_val = row[-1]  # last column is the class label
        class_counts[class_val] += 1
        total_samples += 1

        for i in range(len(row) - 1):
            attribute_counts[i][row[i], class_val] += 1

    return class_counts, attribute_counts, total_samples

# Function to predict class for a given instance
def predict(class_counts, attribute_counts, total_samples, instance):
    max_prob = float('-inf')
    predicted_class = None

    for class_val, class_count in class_counts.items():
        prob = 1.0
        for i in range(len(instance)):
            count = attribute_counts[i][instance[i], class_val]
            prob *= (count + 1) / (class_count + len(attribute_counts[i]))

        prob *= class_count / total_samples

        if prob > max_prob:
            max_prob = prob
            predicted_class = class_val

    return predicted_class

def read_csv(filename):
    dataset = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            dataset.append(row)
    return dataset

if __name__ == "__main__":
    filename = 'exp12_input2.csv'
    dataset = read_csv(filename)

    class_counts, attribute_counts, total_samples = train(dataset)

    # Taking test instance as input from the user
    print("Enter the attributes of the test instance:")
    test_instance = []
    for i in range(len(dataset[0]) - 1):  # assuming the test instance has the same number of attributes as the dataset
        attribute = input(f"Attribute {i + 1}: ")
        test_instance.append(attribute)

    predicted_class = predict(class_counts, attribute_counts, total_samples, test_instance)
    print(f"Predicted class: {predicted_class}")

