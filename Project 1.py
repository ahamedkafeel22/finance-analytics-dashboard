import pandas as pd

# Load the file
df = pd.read_excel(r"C:\Users\syedk\Documents\Self Projects\Project 1\Financial Sample.xlsx")

# Basic check
print(df.shape)           # How many rows & columns
print(df.dtypes)          # Column data types
print(df.isnull().sum())  # Any missing values?
print(df.describe())      # Summary statistics

# Check date range
print(df['Date'].min())
print(df['Date'].max())
print(df['Year'].unique())

import pandas as pd

# Load
df = pd.read_excel(r"C:\Users\syedk\Documents\Self Projects\Project 1\Financial Sample.xlsx")

# Fix column name with leading space
df.columns = df.columns.str.strip()

# Fill missing Discount Band with 'None'
df['Discount Band'] = df['Discount Band'].fillna('None')

# Verify no more nulls
print("Null values after cleaning:")
print(df.isnull().sum())

# Verify Sales column name is fixed
print("\nColumn names:", df.columns.tolist())

# Add a Profit Margin % column (useful for Power BI)
df['Profit Margin %'] = (df['Profit'] / df['Sales'] * 100).round(2)

# Add Month-Year column for clean time axis in Power BI
df['Month-Year'] = pd.to_datetime(df['Date']).dt.to_period('M').astype(str)

# Final shape check
print(f"\nFinal dataset shape: {df.shape}")
print(df[['Sales', 'COGS', 'Profit', 'Profit Margin %', 'Month-Year']].head())

# Save clean file
# Save clean file
df.to_csv(r"C:\Users\syedk\Documents\Self Projects\Project 1\finance_clean.csv", index=False)
print("\n✅ finance_clean.csv saved successfully!")