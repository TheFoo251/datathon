import pandas as pd
from pathlib import Path
from sklearn.preprocessing import LabelEncoder


# No Injury vs Injury -- 1 vs 0


def get_dataframe():
    data = pd.read_csv(Path("data.csv"))
    # replace row with 0 or 1

    codes = {
        "Property Damage Only": 0,
        "Visible Injury": 1,
        "Nonvisible Injury": 2,
        "Severe Injury": 3,
        "Fatal Injury": 4,
    }
    data["Crash Severity"] = data["Crash Severity"].map(codes)
    data["Severe?"] = data["Crash Severity"] >= 3
    return data


if __name__ == "__main__":
    data = get_dataframe()
    print(data["Crash Severity"].unique())
    # print(list(data))
    print(data["Intersection Type"].unique())
    print(data.groupby("Intersection Type")["Severe?"].value_counts())
