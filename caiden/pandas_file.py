import pandas as pd
import csv
from pathlib import Path
import matplotlib.pyplot as plt

def readfile(file_path):
    fout = []
    with open(Path(".", file_path)) as fin:
        reader = csv.reader(fin, delimiter=',')
        for line in reader:
            fout.append(line)
    return fout
new_file = readfile('data.csv')

df = pd.read_csv(Path("data.csv"))

#print(df.unique())
#print(list(df))


#print(df['Crash Severity'].unique())  # Shows unique values in the 'Series' column
#print(df['Crash Severity'].value_counts())

intersection_injury_counts = df.groupby('Intersection Type')['Crash Severity'].value_counts()

# Display the result
print(intersection_injury_counts)



intersection_injury_counts = intersection_injury_counts.reset_index(name='Count')

# Example plot of injury types by intersection type
intersection_injury_counts.pivot(index='Intersection Type', columns='Crash Severity', values='Count').plot(kind='bar', stacked=True)
plt.ylabel('Count of Injuries')
plt.title('Injury Types by Intersection Type')
plt.show()
