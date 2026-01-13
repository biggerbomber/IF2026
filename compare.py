import pandas as pd

csv_1 = "AllCREEP.csv"
csv_2 = "Aerei_Final.csv"

df1 = pd.read_csv(csv_1)
df2 = pd.read_csv(csv_2)

# 1) Compare column names
cols1 = set(df1.columns)
cols2 = set(df2.columns)

print("Columns only in first file:", cols1 - cols2)
print("Columns only in second file:", cols2 - cols1)
print("-" * 30)

# 2) Compare rows in common columns
# FIX: Convert set to list here so pandas can use it
common_cols = list(cols1.intersection(cols2))

# Use the minimum number of rows to avoid crashing if one file is longer
num_rows = min(len(df1), len(df2))

print("Checking for differences...")

# Loop through every row index
for i in range(num_rows):
    # Loop through every common column
    for col in common_cols:
        val1 = df1.iloc[i][col]
        val2 = df2.iloc[i][col]
        
        # Compare the values
        # We convert to string (str) to handle cases where one is 
        # integer (5) and one is float (5.0), or to handle missing data (NaN)
        if str(val1) != str(val2):
            print(f"Row {i} | Col '{col}': File1='{val1}' vs File2='{val2}'")
            #print full row from both files for context
            print("  File1 Row:", df1.iloc[i].to_dict())
            print("  File2 Row:", df2.iloc[i].to_dict())
            print("-" * 30)

# Check if file lengths are different
if len(df1) != len(df2):
    print("-" * 30)
    print(f"Warning: File lengths differ! File1: {len(df1)} rows, File2: {len(df2)} rows.")