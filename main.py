print("\nInitiating...\n")
import os
import sys
from dotenv import load_dotenv
from modules.extract import extract_data
from modules.clean import clean_data
from modules.compute import compute_data
from modules.visualize import visualize_data

load_dotenv()

if __name__ == "__main__":
    endpoints = {
        "contacts": os.environ["CONTACTS_URL"],
        "campaigns": os.environ["CAMPAIGNS_URL"],
        "locations": os.environ["LOCATIONS_URL"],
        "customFields": os.environ["CUSTOM_FIELDS"],
        "tags": os.environ["TAGS_URL"],
        "pipelines": os.environ["PIPELINES_URL"],
    }
    os.system("cls" if os.name == "nt" else "clear")
    print("\n___  HUMBER COLLEGE  ___")
    print("______   Group 7  ______\n")
    print("Data Analytics Wizard :\n")
    print(
        "Note: If you do not wish to go through the entire wizard, you can specify the step name (extract | clean | compute | visualize)\nas the first command line argument while running the script.\n"
    )

    if len(sys.argv) > 1 and sys.argv[1] == "extract":
        user_endpoints = input(
            "Enter entities (contacts,campaigns,tags... or 'all' for all entities): "
        ).split(",")
        user_output_format = input("Enter output format (csv or xlsx): ")
        user_limit = input(
            "Enter the maximum number of data points to fetch (or leave empty for all): "
        )

        if "all" in user_endpoints:
            user_endpoints = endpoints.keys()

        limit = int(user_limit) if user_limit else None

        print("\nStarting Extraction Process.\n")
        extract_data(
            {key: endpoints[key] for key in user_endpoints}, user_output_format, limit
        )
        print("\nExtraction process complete.\n")
    elif len(sys.argv) > 1 and sys.argv[1] == "clean":
        print("\nStarting Cleaning Process.\n")
        clean_data()
        print("\nCleaning process complete.\n")
    elif len(sys.argv) > 1 and sys.argv[1] == "compute":
        print("\nStarting Computation Process.\n")
        compute_data(user_output_format)
        print("\nComputation process complete.\n")
    elif len(sys.argv) > 1 and sys.argv[1] == "visualize":
        print("\nStarting Visualization Process.\n")
        visualize_data()
        print("\nVisualization process complete.\n")
    else:
        user_endpoints = input(
            "Enter entities (contacts,campaigns,tags... or 'all' for all entities): "
        ).split(",")
        user_output_format = input("Enter output format (csv or xlsx): ")
        user_limit = input(
            "Enter the maximum number of data points to fetch (or leave empty for all): "
        )

        if "all" in user_endpoints:
            user_endpoints = endpoints.keys()

        limit = int(user_limit) if user_limit else None

        print("\nStarting Extraction Process.\n")
        extract_data(
            {key: endpoints[key] for key in user_endpoints}, user_output_format, limit
        )
        print("\nExtraction process complete.\n")

        print("\nStarting Cleaning Process.\n")
        clean_data()
        print("\nCleaning process complete.\n")

        print("\nStarting Computation Process.\n")
        compute_data(user_output_format)
        print("\nComputation process complete.\n")

        print("\nStarting Visualization Process.\n")
        visualize_data()
        print("\nVisualization process complete.\n")

        print("\nPlease check the 'exports' directory for all the resultant data.\n")
