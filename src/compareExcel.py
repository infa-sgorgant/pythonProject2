import pandas as pd

file1_path = "C:\\HAWK-QE\\shared\\AIML\\output\\compareFolder\\SynonymQueries.xlsx"
file2_path = "C:\\HAWK-QE\\shared\\AIML\\output\\compareFolder\\SynonymQueries_25082023.xlsx"
output_path = "C:\\HAWK-QE\\shared\\AIML\\output\\compareFolder\\differences.xlsx"


# Read the first Excel file and create the first dictionary
df1 = pd.read_excel(file1_path)
dict1 = {row['NLTestQueries']: row['BaselineDSL'] for _, row in df1.iterrows()}

# Read the second Excel file and create the second dictionary
df2 = pd.read_excel(file2_path)
dict2 = {row['NLTestQueries']: row['BaselineDSL'] for _, row in df2.iterrows()}

# Create a list to store differences
differences = []

# Compare the dictionaries
for key, value1 in dict1.items():
    value2 = dict2.get(key)
    if value2 is None or value1 != value2:
        differences.append({'NLTestQueries': key, 'BaselineDSL1': value1, 'BaselineDS2': value2})

# Create a DataFrame from the differences list
df_differences = pd.DataFrame(differences)

# Write the differences to a new Excel file
df_differences.to_excel(output_path, index=False)


