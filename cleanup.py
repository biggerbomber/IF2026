import pandas as pd

# 1. READ FILE
# Assumes the file is in the same folder as this script
# If your file has no extension, change this to 'AllCREEP'
input_filename = 'AllCREEP.csv' 
output_filename = 'AllCREEP_cleaned.csv'

try:
    df = pd.read_csv(input_filename)
    print(f"Successfully read {input_filename}...")

    # 3. CLEAN DATA VALUES
    # Loop through all columns that contain text (strings)
    for col in df.select_dtypes(include=['object']).columns:
        # A. Strip leading and trailing whitespace
        df[col] = df[col].str.strip()
        
        # B. Convert to lowercase
        df[col] = df[col].str.lower()
        
        # C. Replace multiple internal spaces with a single space
        df[col] = df[col].replace(r'\s+', ' ', regex=True)

    # 4. HANDLE MISSING VALUES
    # Fill empty cells with an empty string so they don't look like 'nan'
    df = df.fillna('')

    # 5. SAVE TO NEW FILE
    df.to_csv(output_filename, index=False)
    print(f"Done! Cleaned data saved to: {output_filename}")

except FileNotFoundError:
    print(f"Error: The file '{input_filename}' was not found. Please check the name and location.")