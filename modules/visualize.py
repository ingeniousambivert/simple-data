import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def visualize_data():
    data_folder_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "exports"
    )
    cleaned_folder_path = os.path.join(data_folder_path, "cleaned")
    df = pd.DataFrame()
    for file in cleaned_folder_path:
        if file.endswith(".csv") or file.endswith(".xlsx"):
            file_path = os.path.join(folder_path, file)
            data = (
                pd.read_csv(file_path)
                if file.endswith(".csv")
                else pd.read_excel(file_path)
            )
            df = pd.concat([df, data])

    df.reset_index(drop=True, inplace=True)
    sns.set()
    # sns.scatterplot(x="column_name1", y="column_name2", data=df)
    # sns.barplot(x="column_name", y="count_column", data=df.groupby("column_name").size().reset_index(name="count_column"))
    # sns.lineplot(x="time_column", y="value_column", data=df)

    plt.show()
