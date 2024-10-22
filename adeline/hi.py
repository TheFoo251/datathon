import csv
from pathlib import Path

def readfile(fp):
    data = []
    with open(Path(fp)) as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            data.append(line)
    return data


traffic_crashes = readfile('/Users/adelinechen/CPSC250/datathon/adeline/Traffic_Crashes_20241021.csv')

print(traffic_crashes)
