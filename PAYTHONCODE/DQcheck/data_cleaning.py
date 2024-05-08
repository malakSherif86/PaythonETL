# data_cleaning.py

import pandas as pd

def clean_csv(input_path, output_path):

    df = pd.read_csv(input_path)
    

    df_cleaned = df.dropna()
    

    df_cleaned = df_cleaned.drop_duplicates()
    
    df_cleaned.to_csv(output_path, index=False)
    
   
    nulls_exist = df_cleaned.isnull().any().any()
    duplicates_exist = df_cleaned.duplicated().any()
    
   
    if not nulls_exist and not duplicates_exist:
        print("Data has been cleaned successfully. No nulls or duplicates found.")
    else:
        print("Data has been cleaned, but nulls or duplicates still exist.")
