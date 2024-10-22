import csv
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

"""
def readfile(fp):
    data = []
    with open(Path(fp)) as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            data.append(line)
    return data
"""


# read csv file into pandas
df = pd.read_csv('/Users/adelinechen/CPSC250/datathon/adeline/Traffic_Crashes_20241021.csv')

# convert 'datetime' to proper datetime object
df['Datetime'] = pd.to_datetime(df['Datetime'], errors='coerce')

# convert numeric columns to the proper format
numeric_columns = [
    'Number of Vehicles Involved', 'Number of Fatalities',
    'Number of People with Suspected Serious Injury', 'Number of People with Suspected Minor Injury',
    'Number of People with Possible Injury', 'Number of People Injured',
    'Number of Pedestrian Fatalities', 'Number of Pedestrians Injured',
    'Maximum Speed Difference'
]
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# handle missing values (drop or fill as needed)
df.dropna(subset=['Crash Severity', 'Number of Vehicles Involved'], inplace=True)


# strip extra spaces from categorical columns
categorical_columns = [
    'Crash Severity', 'Weather Condition', 'Light Condition',
    'Roadway Surface Condition', 'Driver Action', 'Intersection Type'
]
df[categorical_columns] = df[categorical_columns].apply(lambda x: x.str.strip())

# group by intersection
intersection_crashes = df.groupby('Intersection Type').size().reset_index(name='Crash Count')

# sort by crash data
intersection_crashes = intersection_crashes.sort_values(by='Crash Count', ascending=False)

# plot data yay!
plt.figure(figsize=(10,6))
plt.bar(intersection_crashes['Intersection Type'], intersection_crashes['Crash Count'], color='pink')
plt.xlabel('Intersection Type')
plt.ylabel('Number of Crashes')
plt.title('Number of Crashes by Intersection Type')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# print(intersection_crashes)

# print fatalities by intersection

# filter crashes with fatalities
fatal_crashes = df[df['Number of Fatalities'] > 0]

# group by intersection type and count the number of fatal crashes
fatal_crashes_by_intersection = fatal_crashes.groupby('Intersection Type').size().reset_index(name='Fatal Crash Count')

# sort by fatal crash count to see which intersection types had the most fatalities
fatal_crashes_by_intersection = fatal_crashes_by_intersection.sort_values(by='Fatal Crash Count', ascending=False)

# print the grouped data
print(fatal_crashes_by_intersection)
