import os
import requests
import datetime
import pandas as pd
import time

def log_failure(message):
    log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "errors.txt")
    with open(log_file_path, "a") as log_file:
        log_file.write(message + "\n")
        
        
def fetch_data(url, key, retry_count=0, limit=None):
    api_key = os.environ["API_KEY"]
    headers = {
        "Authorization": "Bearer " + api_key
    }
    try:
        if limit is None:
            print(f"Fetching data for {key}...")
            response = requests.get(url, headers=headers)
        else:
            print(f"Fetching data for {key}...")
            response = requests.get(url, headers=headers, params={"limit": limit})
        response.raise_for_status()
        data = response.json()
        if key in data:
            return data[key]
        else:
            return []

    except requests.exceptions.RequestException as e:
        error_message = f"{datetime.datetime.now()}:{url}:{str(e)}"
        print(f"Request failed for {key}. Retrying in {2 ** retry_count} seconds...")
        log_failure(error_message)
        time.sleep(2 ** retry_count)
        return fetch_data(url, key, retry_count + 1, limit) if retry_count < 5 else []

def extract_data(endpoints, output_format, limit=None):
    dfs = {}
    base_url = os.environ["BASE_URL"]
    for key, endpoint in endpoints.items():
        all_data = fetch_data(base_url + endpoint, key, limit=limit)
        df = pd.DataFrame(all_data)
        dfs[key] = df

    data_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
    extracted_folder_path = os.path.join(data_folder_path, "extracted")

    os.makedirs(extracted_folder_path, exist_ok=True)

    for key, df in dfs.items():
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
        file_name = f"{key}_data_{timestamp}.{output_format}"
        file_path = os.path.join(extracted_folder_path, file_name)
            
        if output_format == "csv":
            print(f"Saving {file_name}...")
            df.to_csv(file_path, index=False)
        elif output_format == "xlsx":
            print(f"Saving {file_name}...")
            df.to_excel(file_path, index=False)

    return dfs







