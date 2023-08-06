import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_histogram(df):
    # Add your Seaborn and Matplotlib visualization code for files with specific string 1 here
    # sns.histplot(data=df)
    # plt.show()
    print("histplot")


def plot_scatter(df):
    # Add your Seaborn and Matplotlib visualization code for files with specific string 2 here
    # sns.scatterplot(data=df, x="x_column", y="y_column")
    # plt.show()
    print("scatterplot")


def plot_line(df):
    # Add your Seaborn and Matplotlib visualization code for files with specific string 3 here
    # sns.lineplot(data=df, x="x_column", y="y_column")
    # plt.show()
    print("lineplot")


visualization_functions = {
    "contacts": plot_histogram,
    "campaigns": plot_scatter,
    "locations": plot_line,
    "tags": plot_line,
    "customFields": plot_scatter,
    "pipelines": plot_histogram,
}


def visualize_data():
    data_folder_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "exports"
    )
    cleaned_folder_path = os.path.join(data_folder_path, "cleaned")
    df = pd.DataFrame()

    for filename in os.listdir(cleaned_folder_path):
        if filename.endswith(".csv") or filename.endswith(".xlsx"):
            file_path = os.path.join(cleaned_folder_path, filename)
            if filename.endswith(".csv"):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)

            df.reset_index(drop=True, inplace=True)

            for keyword, visualization_function in visualization_functions.items():
                if keyword in filename:
                    visualization_function(df)
