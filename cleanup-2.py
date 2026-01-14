import pandas as pd
import numpy as np

def clean_flight_data(file_path, output_path):
    try:
        # 1. Read the CSV
        # We read all as strings initially to easily check for "Unknown"
        df = pd.read_csv(file_path, dtype=str)
        
        print(f"Original rows: {len(df)}")

        # 2. Remove rows containing "Unknown" (case insensitive)
        # We apply a mask to find 'Unknown' in any column
        mask_unknown = df.apply(lambda x: x.astype(str).str.contains('Unknown', case=False, na=False)).any(axis=1)
        df = df[~mask_unknown].copy()
        
        # 3. Remove rows containing "0"
        # We check if any cell contains the string "0" exactly
        mask_zero = (df == '0').any(axis=1)
        df = df[~mask_zero].copy()

        # 4. Prepare for the Math check (Sum of last 2 columns)
        # Convert the last two columns ('Dead', 'Survivors') to numbers
        # The example shows they are the 3rd and 4th columns (index 2 and 3)
        cols_to_sum = df.columns[-2:] # Takes the last two columns dynamicall
        
        # Convert to numeric, forcing errors to NaN (though we filtered Unknowns, this is safe)
        for col in cols_to_sum:
            df[col] = pd.to_numeric(df[col])

        # 5. Remove rows where sum of last 2 columns < 10
        df['Total_Passengers'] = df[cols_to_sum].sum(axis=1)
        df = df[df['Total_Passengers'] >= 10]

        # Drop the temporary calculation column if you don't want it in the final file
        df = df.drop(columns=['Total_Passengers'])

        print(f"Cleaned rows: {len(df)}")
        
        # Save to file
        df.to_csv(output_path, index=False)
        print(f"File saved to {output_path}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the script
clean_flight_data('dati/ALL.csv', 'dati/cleaned_ALL.csv')