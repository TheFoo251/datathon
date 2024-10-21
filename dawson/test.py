import pandas as pd
from pathlib import Path
from sklearn import datasets, decomposition
from sklearn.preprocessing import LabelEncoder

# pca = decomposition.PCA(n_components=3)
# pca.fit(X)
# X = pca.transform(X)

# No Injury vs Injury -- 1 vs 0


def get_dataframe():
    data = pd.read_csv(Path("../data.csv"))
    # replace row with 0 or 1

    encoder = LabelEncoder()
    data["Injury?"] = encoder.fit_transform(data["Crash Severity"])
    return data


if __name__ == "__main__":
    data = get_data()
    print(data["Injury?"])
    print(data["Crash Severity"].unique())
    print(list(data))
