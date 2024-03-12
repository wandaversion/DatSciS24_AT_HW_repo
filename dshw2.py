import pandas as pd
import numpy as np

print(".........................")
url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
df = pd.read_csv(url)

print(".....Task 1...................")
newdf = df.iloc[::20][['Manufacturer', 'Model', 'Type']]
# Draw every 20th row
print("'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0)")
print("Length of DataFrame:", len(newdf))
print(newdf)

print(".....Task 2...................")
# Get mean
print("Rows with missing 'Min.Price' or 'Max.Price' values:")
missing_before = df[pd.isnull(df['Min.Price']) | pd.isnull(df['Max.Price'])]
print(missing_before[['Manufacturer', 'Model', 'Min.Price', 'Max.Price']].head())

# Calculate means for 'Min.Price' and 'Max.Price'
min_mean = df['Min.Price'].mean()
max_mean = df['Max.Price'].mean()
# Fill missing values without using inplace=True
df_filled = df.fillna({'Min.Price': min_mean, 'Max.Price': max_mean})
# Now, showing the change for the same rows after filling missing values
print("Post Computation:")
print(df_filled.loc[missing_before.index][['Manufacturer', 'Model', 'Min.Price', 'Max.Price']].head())

print(".....Task 3...................")
dfn = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
row_tot = dfn.sum(axis=1)
test = row_tot > 100
sorted_row = dfn[test]
print(sorted_row)

print(".....Task 4...................")
# 4x4 numpy array, filled w random ints 1-100
new_array = np.random.randint(1, 100, (4, 4))
print("Array", new_array)

row = lambda x: np.sum(x, axis=1)
column = lambda x: np.sum(x.T, axis=1)

sum_r = row(new_array)
sum_c = column(new_array)
print("Sum Rows", sum_r)
print("Sum Columns", sum_c)