# Name: Amanda Rodgers
# Date: April 15th, 2024
# Project: NYC_Women_Resource

# Import pandas and numpy libraries
import pandas as pd
import numpy as np

# Load data
initial_data = pd.read_csv('NYC_Women_Resources.csv')

initial_data.head(10)

# Inspepct data structure
initial_data.describe()
initial_data.info()

# Make df for the boroughs
boroughs = initial_data[["Brooklyn", "Bronx", "Manhattan", "Queens", "Staten Island"]]
boroughs.dropna(inplace=True)
boroughs

# Count of 'Y' or organizations in Brooklyn
brooklyn_y = boroughs['Brooklyn'].eq('Y').sum()
print(brooklyn_y)

# Count number of 'Y' or number of organizations in each borough
borough_org_count = boroughs.eq('Y').sum()
print(borough_org_count)
