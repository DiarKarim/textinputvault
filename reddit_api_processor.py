"""
Reddit API provides json files that require processing to find dubplicates
This script performs a text on one file, but it can be rewritten to repeat
this process on multiple files and put them all into one large dataframe for 
duplicate analysis and further processing. 

Ultimately we want to export the results into a single csv file so that we can 
add it back into a shared google sheet for human analysis. 

Author: Diar Karim
Date: 04/01/2024
Version: 1.0
"""

import pandas as pd
import time 
import json
from datetime import datetime

# Update this to point to the target json file 
path_2_file = "VR_text.json" 

# Function to extract json file keys 
def extract_data_to_dataframe(json_file_path):
    # Load JSON data from file
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)
    
    # Extract data into a dataframe
    df = pd.DataFrame(json_data['data'], columns=['subreddit', 'selftext', 'title', 'name', 'created'])
    
    # Convert 'created' from Unix time to DD-MM-YY format
    # df['created'] = df['created'].apply(lambda x: datetime.utcfromtimestamp(x).strftime('%d-%m-%y'))
    df['created'] = df['created'].apply(lambda x: datetime.utcfromtimestamp(x).strftime('%d-%m-%y') if pd.notna(x) else x)

    return df


# Use the function above to extract the required keys from the json file 
json_file_path = path_2_file  # Replace with your JSON file path
dataframe = extract_data_to_dataframe(json_file_path)
dataframe

# Convert to csv for google sheet users 
dataframe.to_csv("VR_text.csv")