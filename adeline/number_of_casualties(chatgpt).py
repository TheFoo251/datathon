import csv
import matplotlib.pyplot as plt
import pandas as pd

# Load the crash data into a DataFrame
df = pd.read_csv('/Users/adelinechen/CPSC250/datathon/adeline/Traffic_Crashes_20241021.csv')

# 1. Convert 'Datetime' to a proper datetime object
df['Datetime'] = pd.to_datetime(df['Datetime'], errors='coerce')

# 2. Convert numeric columns to the proper format
numeric_columns = [
    'Number of Vehicles Involved', 'Number of Fatalities',
    'Number of People with Suspected Serious Injury',
    'Number of People with Suspected Minor Injury',
    'Number of People with Possible Injury',
    'Number of People Injured', 'Number of Pedestrian Fatalities',
    'Number of Pedestrians Injured', 'Maximum Speed Difference'
]
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# 3. Handle missing values (either drop or fill as needed)
df.dropna(subset=['Crash Severity', 'Number of Vehicles Involved'], inplace=True)
# or df.fillna(0, inplace=True)

# 4. Strip extra spaces from categorical columns
categorical_columns = [
    'Crash Severity', 'Weather Condition', 'Light Condition',
    'Roadway Surface Condition', 'Driver Action',
    'Intersection Type'
]
df[categorical_columns] = df[categorical_columns].apply(lambda x: x.str.strip())

# 5. Create a new column to classify crashes as 'Severe' or 'Non-Severe'
df['Severity'] = df.apply(
    lambda row: 'Severe' if row['Number of Fatalities'] > 0 or row['Number of People with Suspected Serious Injury'] > 0 else 'Non-Severe',
    axis=1
)

# 6. Group by 'Intersection Type' and 'Severity' and count the number of crashes
severity_crashes_by_intersection = df.groupby(['Intersection Type', 'Severity']).size().unstack(fill_value=0)

# 7. Print the results
print(severity_crashes_by_intersection)

severity_crashes_by_intersection.plot(kind='bar', stacked=True, color=['#ff9999', '#66b3ff'])
plt.title('Crash Severity by Intersection Type')
plt.xlabel('Intersection Type')
plt.ylabel('Number of Crashes')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Severity', loc='upper right')
plt.tight_layout()  # Adjusts plot to fit into figure area
plt.show()
