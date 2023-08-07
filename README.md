# Capstone - Marketing Data Analysis

Data Retrieval -> Data Cleaning -> Data Analysis -> Data Visualization

## Getting Started

Getting up and running is simple.

1. Make sure you have [Python3](https://www.python.org/), [pip](https://pip.pypa.io/en/stable/) installed.

2. Create and activate the vitual environment for the script.

   ```bash
   python3 -m venv capenv
   source ./capenv/bin/activate
   ```

3. Install your dependencies.

   ```bash
   pip install -r requirements.txt
   ```

4. Configuring the server with environment variables

   - Create a `.env` file in the root
   - Add the following lines to it (modify according to your environment/requirements)

   ```env
    # configure the api
   BASE_URL=
   API_KEY=
   CONTACTS_URL=
   CAMPAIGNS_URL=
   LOCATIONS_URL=
   PIPELINES_URL=
   ```

5. Start your script.

   ```bash
   python3 main.py
   ```

_All the resultant data is versioned using timestamps (yyyy-mm-dd) and will be stored categorically in the "exports" directory_
