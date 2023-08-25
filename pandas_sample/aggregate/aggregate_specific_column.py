import datetime
import pandas as pd

start_date = datetime.date(2019, 1, 1)
end_date = datetime.date(2019, 1, 31)

for date_delta in range((end_date - start_date).days + 1):
    # Load the input Excel file
    input_file = "input/sample.xlsx"
    df = pd.read_excel(input_file)

    # Drop unnecessary columns
    # df = df.drop(columns=['nouse', 'nouse.1', 'nouse.2'])

    # Pivot the DataFrame to reshape it
    pivot_df = df.pivot(index='name', columns='item', values='price')
    pivot_df = pivot_df.sort_index()

    # Reset index and rename columns
    pivot_df = pivot_df.reset_index()
    pivot_df.columns.name = None

    # Save the output Excel file
    output_file = "output/"+str(start_date+datetime.timedelta(date_delta))+"sample.xlsx"
    pivot_df.to_excel(output_file, index=False)

print("Output generated successfully using pandas!")
