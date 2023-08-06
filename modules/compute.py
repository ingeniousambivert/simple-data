import os
import datetime
import pandas as pd

# from sklearn.linear_model import LogisticRegression, LinearRegression


def compute_data(output_format):
    data = []
    data_folder_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "exports"
    )
    cleaned_folder_path = os.path.join(data_folder_path, "cleaned")

    for filename in os.listdir(cleaned_folder_path):
        if filename.endswith(".csv") or filename.endswith(".xlsx"):
            file_path = os.path.join(cleaned_folder_path, filename)
            if filename.endswith(".csv"):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)

            print(f"Summarizing data from {filename}...")

            summary = {
                "File": filename,
                "Rows": len(df),
                "Columns": len(df.columns),
                "Missing Values": df.isnull().sum().sum(),
                "Data Types": df.dtypes.to_dict(),
            }

            for column in df.columns:
                # if df[column].dtype in ["int64", "float64"]:
                # summary[f"Mean {column}"] = df[column].mean()
                # summary[f"Median {column}"] = df[column].median()
                summary[f"Unique {column}"] = df[column].nunique()

                if df[column].dtype == "object":
                    summary[f"Total Length {column}"] = df[column].str.len().sum()

            data.append(summary)

    summary_df = pd.DataFrame(data)

    computed_folder_path = os.path.join(data_folder_path, "computed")
    os.makedirs(computed_folder_path, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    file_name = f"computed_data_{timestamp}.{output_format}"
    file_path = os.path.join(computed_folder_path, file_name)
    if output_format == "csv":
        print(f"Saving {file_name}...")
        summary_df.to_csv(file_path, index=False)
    elif output_format == "xlsx":
        print(f"Saving {file_name}...")
        summary_df.to_excel(file_path, index=False)

    return summary_df

    # ml_algorithms = [
    #     ("Logistic Regression", LogisticRegression()),
    #     ("Linear Regression", LinearRegression()),
    # ]

    # result_df = pd.DataFrame(columns=["File", "Algorithm", "Result"])
    # data_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
    # cleaned_folder_path = os.path.join(data_folder_path, "cleaned")
    # for filename in os.listdir(cleaned_folder_path):
    #     if filename.endswith(".csv") or filename.endswith(".xlsx"):
    #         file_path = os.path.join(cleaned_folder_path, filename)
    #         data = pd.read_excel(file_path) if filename.endswith(".xlsx") else pd.read_csv(file_path)

    #         for algorithm_name, algorithm in ml_algorithms:
    #             result = algorithm.fit(data.drop("target_column", axis=1), data["target_column"])
    #             result_df = result_df.append({"File": filename, "Algorithm": algorithm_name, "Result": result}, ignore_index=True)

    # computed_file_path = os.path.join(data_folder_path, "computed")
    # os.makedirs(computed_file_path, exist_ok=True)

    # timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    # file_name = f"computed_data_{timestamp}.{output_format}"
    # file_path = os.path.join(computed_file_path, file_name)
    # result_df.to_csv(file_path, index=False)

    # return result_df
