# Learn pandas, numpy, matplotlib, and ploty
# scikicklearn for machine learning

# Pandas (panel data)
handles series ( an array) adn dataframes ( 2 dimenstional, x and y, rows and columns)

#Install pandas
pip install pandas

#Import pandas ( or load the pandas library):
import pandas as pd
# import pandas as means as alias pd, we call panda pd

# pd.function_in_pandas

# Series in pandas ( they are like arrays)
s = pd.Series([1, 2, 3, 4, 5, ])
print(s)
print(s[2])
 # to get value in index 2

# Create a Series with custom indices
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# Create series from dictionary, it knows it's a dictionary from {}
s = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(s['a'])

# Create a DataFrame from a dictionary
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Chris'],
    'Age': [25, 30, 35],
    'Occupation': ['Engineer', 'Doctor', 'Artist']
})
df or
#print(df) it flattens it, just to see it
# to see name column
print(df['Name'])

#access rows by label or index
# What is the the difference between label and index?
print(df.loc[0])  # Access by label
print(df.iloc[0])  # Access by index

# Get rows where Age is greater than 28, you are subsetting with []
filtered_data = df[df['Age'] > 28]
print(filtered_data)

#Adding a column
df['Salary'] = [70000, 80000, 90000]
print(df)

#Deleting a column, inplace means keep the column in same order
# dropping deletes stuff forever
df.drop('Salary', axis=1, inplace=True)
print(df)

# to change a persons age
df['Age'][0] = 56

#Reading a csv file
df = pd.read_csv('data.csv')

#writing to or creating csv file, index = False means to not have first column be nums or index
df.to_csv('new_data.csv', index=False)


