import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def visualize_contacts(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x="country")
    plt.title("Country Distribution")
    plt.xlabel("Country")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.figure(figsize=(12, 6))
    tags_counts = df["tags"].apply(len)
    sns.barplot(x=tags_counts.value_counts().index, y=tags_counts.value_counts().values)
    plt.title("Number of Tags per Contact")
    plt.xlabel("Number of Tags")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

    print("Plotted visualization for Contacts")


def visualize_campaigns(df):
    status_counts = df["status"].value_counts()
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))
    sns.barplot(x=status_counts.index, y=status_counts.values)
    plt.title("Campaign Status Distribution")
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.show()

    print("Plotted visualization for Campaigns")


visualization_functions = {
    "contacts": visualize_contacts,
    "campaigns": visualize_campaigns,
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
