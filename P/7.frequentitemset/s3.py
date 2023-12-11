import math
from itertools import combinations

# Function to read data from file and convert it into a dictionary format
def read_data_in_dict(filename):
    with open(filename) as f:
        lines = f.readlines()
        transactions = []
        items = lines[0].strip().split(',')  # Extract items and strip newline characters
        for line in lines[1:]:
            transaction = line.strip().split(',')  # Extract transactions and strip newline characters
            transactions.append(list(map(int, transaction)))  # Convert transactions to integers
    data = {
        'items': items,  # Store items in the dictionary
        'transactions': transactions  # Store transactions in the dictionary
    }
    return data

# Function to calculate frequency of itemsets in transactions
def get_freq(s, items, transaction):
    freq = 0
    for t in transaction:
        tmp = 1
        for itm in s:
            tmp *= t[items.index(itm)]
        if tmp == 1:
            freq = freq + 1
    return freq

# Function to find frequent itemsets based on minimum support
def frequent_itemset(data, min_support):
    items = data['items']  # Extract items from the data dictionary
    transactions = data['transactions']  # Extract transactions from the data dictionary
    for level in range(1, len(items) + 1):  # Iterate through different itemset lengths
        min_freq = math.ceil(min_support * len(transactions))  # Calculate minimum frequency based on support
        sets = list(combinations(items, level))  # Generate combinations of itemsets of current length
        frequent_set = []
        for s in sets:  # Check frequency of each itemset
            freq = get_freq(s, items, transactions)
            if freq >= min_freq:  # If frequency meets the minimum support, add to frequent_set
                frequent_set.append(s)
        if frequent_set:  # Print frequent itemsets for each length if found
            print(f"Frequent {level}-itemsets: {frequent_set}")

filename = 'itemsets.csv'  # Replace with your file name
data = read_data_in_dict(filename)  # Read data from the file and store it in 'data' variable

# Input minimum support from user
min_support = float(input("Enter minimum support (as a decimal value): "))

# Find frequent itemsets based on the provided minimum support
frequent_itemset(data, min_support)

