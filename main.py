# ------------------------------- Imports ------------------------------- #
import pandas as pd   # Pandas for data manipulation and analysis
import os             # OS module to interact with the file system


# ------------------------------- Load and Combine CSV Files ------------------------------- #
folder = "./data"         # Folder containing all CSV files
all_dfs = list()          # A list to hold DataFrames from each file

# Loop through every file in the folder and read it into a DataFrame
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)        # Get the complete path to the file
    all_dfs.append(pd.read_csv(file_path))            # Read CSV and append to the list

# Combine all DataFrames into one large DataFrame
combined_df = pd.concat(all_dfs)


# ------------------------------- Filter Pink Morsels ------------------------------- #
# Select only rows where the product is 'pink morsel' and copy it to create a new Dataframe not view to avoid warning message
pink_morsels = combined_df[combined_df['product'] == 'pink morsel'].copy()


# ------------------------------- Clean Price Column ------------------------------- #
# Remove the "$" sign from prices and convert them to float
pink_morsels["price"] = pink_morsels["price"].str.replace("$", "", regex=False).astype(float)


# ------------------------------- Calculate Sales ------------------------------- #
# Create a new 'sales' column as price * quantity
pink_morsels['sales'] = pink_morsels['price'] * pink_morsels['quantity']


# ------------------------------- Format Columns ------------------------------- #
# Capitalize column names for consistency
pink_morsels.columns = pink_morsels.columns.str.title()

# Define a new order for columns
new_order = ['Sales', 'Date', 'Region']

# Reorder DataFrame columns based on new_order
final_df = pink_morsels.reindex(columns=new_order)  
# Alternative way: final_df = pink_morsels[new_order]


# ------------------------------- Save Final Data ------------------------------- #
# Export the cleaned and processed DataFrame to a new CSV file
final_df.to_csv("pink_morsel_sales_data.csv", index=False)