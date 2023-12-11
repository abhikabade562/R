from asyncore import write
import numpy as np
import pandas as pd
import csv
PlayTennis = pd.read_csv('tennis.csv')

def find_entropy(x,y,t):
    if x!=0 and y!=0:
        return -((x/t)*(math.log2((x/t)))+(y/t)*(math.log2((y/t))))
    else:
        return 0.0

from sklearn.preprocessing import LabelEncoder
import collections
Le = LabelEncoder() #non-numeric->numeric

PlayTennis['outlook'] = Le.fit_transform(PlayTennis['outlook'])
PlayTennis['temp'] = Le.fit_transform(PlayTennis['temp'])
PlayTennis['humidity'] = Le.fit_transform(PlayTennis['humidity'])
PlayTennis['windy'] = Le.fit_transform(PlayTennis['windy'])
PlayTennis['play'] = Le.fit_transform(PlayTennis['play'])
frequencyPlay = collections.Counter(PlayTennis.play)
tot=PlayTennis.play.size
import math
EntropyOfData=find_entropy(frequencyPlay[0],frequencyPlay[1],tot)
print("Total entropy is:"+str(EntropyOfData))

# print(PlayTennis)
frequencyWindy = collections.Counter(PlayTennis.windy)
#print(frequencyWindy) #count of occurences of unique elements
infogainWind=0.0
for i in frequencyWindy:
    cnt=0
    for x in range(PlayTennis.play.size):
      if PlayTennis.play.get(x)==1 and PlayTennis.windy.get(x)==i:
        cnt=cnt+1
    infogainWind=infogainWind+(frequencyWindy[i]/tot)*find_entropy(frequencyWindy[i]-cnt,cnt,frequencyWindy[i])
infogainWind=EntropyOfData-infogainWind
print("Information gain by wind is:"+str(infogainWind))
file=open('output.csv','w',newline='')
with file:
    header=['Total Entropy','Information Gain']
    writer=csv.DictWriter(file,fieldnames=header)
    writer.writeheader()
    writer.writerow({'Total Entropy' : str(EntropyOfData),
                     'Information Gain': str(infogainWind)
                     })