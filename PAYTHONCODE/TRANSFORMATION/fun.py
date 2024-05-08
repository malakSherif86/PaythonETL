import pandas as pd

def process_csv(input_file, output_file, column_to_convert):
    
    df = pd.read_csv(input_file)
    
    df[column_to_convert] = pd.to_datetime(df[column_to_convert])
    
    df.to_csv(output_file, index=False)

