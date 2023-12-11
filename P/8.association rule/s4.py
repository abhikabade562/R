import math
from itertools import combinations, permutations
import csv

def read_data_in_dict(filename):
    f = open(filename)
    lines = f.readlines()
    transactions = []
    items = lines[0].strip().split(',')
    for line in lines[1:]:
        transactions.append(list(map(int, line.strip().split(','))))
    data = {
        'items': items,
        'transactions': transactions
    }
    return data


def frequent_itemsets(data, level, min_support):
    items = data['items']
    transactions = data['transactions']
    min_freq = math.ceil(min_support * len(transactions))
    sets = list(combinations(items, level))
    frequent_sets = []
    for s in sets:
        freq = get_freq(s, items, transactions)
        if freq >= min_freq:
            frequent_sets.append(s)
    return frequent_sets

def get_freq(s, items, transactions):
    freq = 0
    for t in transactions:
        temp = 1
        for item in s:
            temp *= t[items.index(item)]
        if temp == 1:
            freq += 1  
    return freq

def generate_rule(data, min_support, min_confidence):
    items = data['items']
    transactions = data['transactions']
    with open('output.csv', 'w', newline='') as file:
        for l in range(2, len(data['items']) + 1):
            frequent_set = frequent_itemsets(data, l, min_support)
            for s in frequent_set:
                freq_s = get_freq(s, items, transactions)
                _s_permute = list(permutations(s))
                for _s in _s_permute:
                    for i in range(0, len(_s) - 1):
                        x = _s[0:i + 1]
                        y = _s[i + 1:]
                        freq_x = get_freq(x, items, transactions)
                        if freq_x != 0:
                            c = freq_s / freq_x
                            if c >= min_confidence:
                                print(x, ' -> ', y, 'confidence is ', c)
                                writer = csv.writer(file)
                                writer.writerow([str(x) + '->' + str(y), c])

filename = 'itemsets.csv'  # Replace with your file name
data = read_data_in_dict(filename)  # Read data from the file and store it in 'data' variable

# Input minimum support from user
min_support = float(input("Enter minimum support (as a decimal value): "))

# Input minimum confidence from user
min_confidence = float(input("Enter minimum confidence (as a decimal value): "))

# Generate association rules based on provided minimum support and confidence
generate_rule(data, min_support, min_confidence)

