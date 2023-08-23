import pandas as pd

# Load the input Excel file
input_file = "input/sample.xlsx"
df = pd.read_excel(input_file)

# Drop unnecessary columns
# df = df.drop(columns=['nouse', 'nouse.1', 'nouse.2'])

# Pivot the DataFrame to reshape it
pivot_df = df.pivot(index='name', columns='item', values='price')

# Reset index and rename columns
pivot_df = pivot_df.reset_index()
pivot_df.columns.name = None

# Save the output Excel file
output_file = "output/sample.xlsx"
pivot_df.to_excel(output_file, index=False)

print("Output generated successfully using pandas!")
