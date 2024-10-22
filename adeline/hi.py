import csv
import os
from pathlib import Path

def readfile(fp):
    data = []
    with open(Path(fp)) as fin:
        reader = csv.reader(fin, delimiter=',')
        for line in reader:
            data.append(line)
    return data


traffic_crashes = readfile('/Users/adelinechen/CPSC250/datathon/adeline/Traffic_Crashes_20241021.csv')

print(traffic_crashes)
