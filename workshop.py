# EDA (Exploratory Data Analysis and Visualiztion with Python)
# import, preprocess, filter, descriptive statistics, visualization

import pandas as pd

#Load data
my_data = pd.read_csv('csv_file.csv')
# or pd.read_excel('data.xlsx')
my_data.head()
my_data.describe()
my_data.info()

# float for remote allowed will be boolean yes or no (1 is true 0 is false?)
# recode to true or false

my_data['formatted_experience_level']
my_data['skills_desc'][10000:20000]

# Compute measures of central tendency: mean, median etc


# To explore:
# what are the top 10 job title listings
# titles with top and lowest salaries
# jobs with most applicates
# remote data
# different types of posting_domain

my_data['posting_domain'].unique

import pandas as pd

# Assuming you have a DataFrame df with a column named 'title'

# Group by 'title' and count occurrences
title_counts = df['title'].value_counts()

# Sort the counts in descending order
title_counts_sorted = title_counts.sort_values(ascending=False)

# Get the most common observations (top n)
n = 10  # Change this value as needed
top_titles = title_counts_sorted.head(n)

print("Top", n, "most common titles:")
print(top_titles)

# to see the top 100 rows
df.loc[0:100]

#group by

# to drop rows??? with NA data
df.dropna(inplace=True)

# pick two columns to work with
# Select columns of interest
# subsetting, give list of column names you want to subset
#select the columns
selected_data = my_data[['location', 'med_salary']]
# remove rows with NaN values ( dropna works on the df from memory so you
# might need to go to top cell and hit run again)
selected_data.dropna(inplace=True)
# return a dataframe
selected_data

# sorted top five med_salary
selected_data.sort_values('med_salary', ascending=False).head(5)

# lowest five salaries
selected_data.sort_values('med_salary', ascending=False).head(5)
