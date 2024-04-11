# Learn pandas, numpy, matplotlib, and ploty
# scikicklearn for machine learning

#Load csv
my_data = pd.read_csv('file_name.csv')

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
# dropping deletes stuff forever, axis=1 so it knows it is a column
df.drop('Salary', axis=1, inplace=True)
print(df)

# to change a persons age
df['Age'][0] = 56

#Reading a csv file
# Means store csv and make it into a pandas dataframe
df = pd.read_csv('data.csv')

#writing to or creating csv file, index = False means to not have first column be nums or index
df.to_csv('new_data.csv', index=False)

# Statistical functions

# gives overview of dataframe numbers
print(df.describe())

# spotify
import pandas as pd

# Load the dataset
df = pd.read_csv('Most_Streamed_Spotify_Songs_2023.csv')

# Show the first 5 rows
print(df.head())

# Export to just CSV with deliminate with comman

#Load spotify csv
import pandas as pd

# Load the dataset
df = pd.read_csv('Most_Streamed_Spotify_Songs_2023.csv')

# Show the first 5 rows
print(df.head())

# get overview of data
df.describe()

or

df.info()

# Filter the songs, you get an error because it can't parse the line 574
# drop or delete a row
df = df.drop(574)

# Convert string to integer
df['streams_float'] = df['streams'].astype(float)

filtered_songs = df[df['streams_float'] > 1_000_000_000]

# Show the filtered songs
print(filtered_songs)

# list top most five with danceability
# Sort and filter the top 5 most danceable songs
top_danceable_songs = df.sort_values('danceability_%', ascending=False).head(5)

# Show the top 5 most danceable songs
print(top_danceable_songs)

# Calculate the average BPM by artist ( group by artist and subset or
# summarize by beats per minute)
# Example of summarization or aggregation
avg_bpm_by_artist = df.groupby('artist(s)_name')['bpm'].mean()

# Show the result
print(avg_bpm_by_artist)

#can remove rows that have NaN values in a DataFrame using the dropna() method in pandas.
import pandas as pd

# Assuming df is your DataFrame

# Drop rows with NaN values
df_clean = df.dropna()

# Alternatively, you can specify the axis parameter to remove columns with NaN values
# df_clean = df.dropna(axis=1)

# Print the cleaned DataFrame
print(df_clean)

# when you call a group_by it doesn't return a dataframe
my_data_new = my_data[[column1, column2]]

# to create a dataframe after using group_by
#grouped.reset_index()
x = y.reset_index()
x

# drop or delete rows that have missing values, globally
my_data.dropna(inplace=True)

# pick two columns to work with
# Select columns of interest
# subsetting, give list of column names you want to subset
selected_data = my_data[['location', 'med_salary']]
selected_data.dropna(inplace=True)
selected_data

#
