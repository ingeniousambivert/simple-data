import os
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import VarianceThreshold


def clean_data():
    data_folder_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "exports"
    )
    cleaned_folder_path = os.path.join(data_folder_path, "cleaned")
    os.makedirs(cleaned_folder_path, exist_ok=True)

    extracted_folder_path = os.path.join(data_folder_path, "extracted")

    dfs = {}

    for file in os.listdir(extracted_folder_path):
        if file.endswith(".csv") or file.endswith(".xlsx"):
            file_path = os.path.join(extracted_folder_path, file)
            if file.endswith(".csv"):
                df = pd.read_csv(file_path)
                print(f"Reading {file}...")
            elif file.endswith(".xlsx"):
                df = pd.read_excel(file_path)
                print(f"Reading {file}...")

            df.drop_duplicates(inplace=True)
            print(f"Removed duplicates from {file}...")

            numerical_cols = df.select_dtypes(include=["float64", "int64"]).columns
            non_empty_numerical_cols = [
                col for col in numerical_cols if df[col].notnull().any()
            ]
            if not non_empty_numerical_cols:
                print("No valid numerical columns found.")
            else:
                print(f"Numerical columns found: {non_empty_numerical_cols}")

                imputer = SimpleImputer(strategy="mean")
                df[non_empty_numerical_cols] = imputer.fit_transform(
                    df[non_empty_numerical_cols]
                )
                print(f"Imputed values from {file}...")

                scaler = MinMaxScaler()
                df[non_empty_numerical_cols] = scaler.fit_transform(
                    df[non_empty_numerical_cols]
                )
                print(f"Scaled values from {file}...")

            filename_without_extension = os.path.splitext(file)[0]
            dfs[filename_without_extension] = df

            cleaned_file_path = os.path.join(cleaned_folder_path, file)
            if file.endswith(".csv"):
                df.to_csv(cleaned_file_path, index=False)
                print(f"Cleaned data saved as {file}")
            elif file.endswith(".xlsx"):
                df.to_excel(cleaned_file_path, index=False)
                print(f"Cleaned data saved as {file}")

    return dfs
