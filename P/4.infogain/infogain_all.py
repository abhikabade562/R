from collections import Counter
import pandas as pd
import numpy as np
import math
import csv

def find_entropy(x, y, t):
    if x != 0 and y != 0:
        return -((x / t) * (math.log2(x / t)) + (y / t) * (math.log2(y / t)))
    else:
        return 0.0

# Read the CSV file into a DataFrame
PlayTennis = pd.read_csv('tennis.csv')

# Label encode non-numeric columns
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

PlayTennis['outlook'] = le.fit_transform(PlayTennis['outlook'])
PlayTennis['temp'] = le.fit_transform(PlayTennis['temp'])
PlayTennis['humidity'] = le.fit_transform(PlayTennis['humidity'])
PlayTennis['windy'] = le.fit_transform(PlayTennis['windy'])
PlayTennis['play'] = le.fit_transform(PlayTennis['play'])

# Calculate total entropy of 'play' attribute
frequencyPlay = Counter(PlayTennis.play)
total_instances = PlayTennis.play.size
EntropyOfData = find_entropy(frequencyPlay[0], frequencyPlay[1], total_instances)
print("Total entropy is:", EntropyOfData)

# Calculate information gain for each attribute
attributes = ['outlook', 'temp', 'humidity', 'windy']
info_gain_results = {}

for attr in attributes:
    frequency_attr = Counter(PlayTennis[attr])
    info_gain_attr = 0.0

    for val in frequency_attr:
        cnt = sum((PlayTennis[attr] == val) & (PlayTennis['play'] == 1))
        info_gain_attr += (frequency_attr[val] / total_instances) * find_entropy(frequency_attr[val] - cnt, cnt, frequency_attr[val])

    info_gain_attr = EntropyOfData - info_gain_attr
    info_gain_results[attr] = info_gain_attr
    print(f"Information gain by {attr} is:", info_gain_attr)

# Write information gains to output.csv
with open('output.csv', 'w', newline='') as file:
    header = ['Attribute', 'Information Gain']
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    for attr, info_gain in info_gain_results.items():
        writer.writerow({'Attribute': attr, 'Information Gain': info_gain})
