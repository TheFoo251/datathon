import csv
import os
from pathlib import Path

def readfile(file_path):
    fout = []
    with open(Path("..\\", file_path)) as fin:
        reader = csv.reader(fin, delimiter=',')
        for line in reader:
            fout.append(line)
    return fout


new_file = readfile('Traffic_Crashes_20241021.csv')


#### Read 
print(new_file)