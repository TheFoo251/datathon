import pandas as pd
import matplotlib.pyplot as plt


# From the dataset, we need the "Intersection Type" for the x-axis, and the ratio of severe/fatal injury crashes to total crashes for the y-axis.
# Severe injury = "Number of People with Suspected Serious Injury" > 0
# Fatal injury = "Number of Fatalities" > 0

# Let's group the data by "Intersection Type" and calculate the ratio of severe/fatal crashes to total crashes.


def get_summary(df, x_axis):
    # Filter crashes with severe or fatal injuries
    severe_or_fatal = (df["Number of People with Suspected Serious Injury"] > 0) | (
        df["Number of Fatalities"] > 0
    )

    # Group by intersection type and calculate total crashes and severe/fatal crashes
    grouped = df.groupby(x_axis).agg(
        total_crashes=("Document Number", "count"),
        severe_fatal_crashes=(
            "Document Number",
            lambda x: severe_or_fatal.loc[x.index].sum(),
        ),
    )

    # Calculate the ratio of severe/fatal crashes to total crashes
    grouped["ratio_severe_fatal"] = (
        grouped["severe_fatal_crashes"] / grouped["total_crashes"]
    )

    return grouped


def plot_data(df, x_axis):
    print(df.head())
    # grouped = grouped.nlargest(10, 'ratio_severe_fatal')
    # Plot
    plt.figure(figsize=(10, 6))
    df["ratio_severe_fatal"].plot(kind="bar", color="skyblue")
    plt.title(f"Ratio of Severe/Fatal Crashes to Total Crashes by {x_axis}")
    plt.xlabel(x_axis)
    plt.ylabel("Ratio of Severe/Fatal Crashes")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # Show the plot
    plt.show()


def plot_all_features(df):
    intersection_df = get_summary(df, "Intersection Type")
    description_df = get_summary(df, "Roadway Description")
    defects_df = get_summary(df, "Roadway Defects")

    plot_data(intersection_df, "Intersection Type")
    plot_data(description_df, "Roadway Description")
    plot_data(defects_df, "Roadway Defects")


if __name__ == "__main__":

    # Load the dataset
    file_path = "data.csv"
    data = pd.read_csv(file_path)

    # plot_all_features(data)

    # filter by HAMPTON BLVD
    hampton_blvd_data = data.loc[data["Route or Street Name"] == "HAMPTON BLVD"]

    # count = 0
    # for letter in hampton_blvd_data["Alcohol Involved"].sum():
    #     if letter == 'Y':
    #         count += 1

    non_interstate_data = data.loc[
        ~data["Route or Street Name"].str.contains("I-")
        & ~data["Route or Street Name"].str.contains("INTER")
    ]
    plot_all_features(non_interstate_data)
    # print(non_interstate_data.head())
    # plot_all_features(hampton_blvd_data)
