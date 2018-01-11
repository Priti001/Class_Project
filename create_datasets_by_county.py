
# coding: utf-8

# Objective: 
# - Merge Zillow City_time_series.csv and city_crosswalk.csv and filter to only include CA.
# - Save high level summary spreadsheet for county lookup and detail spreadsheet for each county.

# Required file structure:
# - this script
# - directory: 'datasets'
#     - directory: 'zecon'
#         - 'City_time_series.csv'
#         - 'cities_crosswalk.csv'


# Dependencies
import sys
import os
import pandas as pd


# Initialize directory structure relative to notebook location
nb_loc = os.getcwd()
zecon_dataset_loc = os.path.join(nb_loc,'datasets','zecon')
datasets = os.listdir(zecon_dataset_loc)

# hard-coded filenames to use
files_used = ['City_time_series.csv',
             'cities_crosswalk.csv']

# Import fileData
crosswalk = pd.read_csv(os.path.join(zecon_dataset_loc,files_used[1]))
city_time_series = pd.read_csv(os.path.join(zecon_dataset_loc,files_used[0]))

# Merge datasets
combine = city_time_series.merge(crosswalk,right_on = 'Unique_City_ID', left_on = 'RegionName')


# Filter to only CA
ca_data = combine.loc[combine['State']=='CA'].dropna(axis='columns',how='all')
ca_data.to_csv('CA_Zillow_data.csv')
county_data_dir = 'data_by_county'

# Save detail data by county
try:
    os.stat(county_data_dir)
except:
    os.mkdir(county_data_dir)
counties = ca_data['County'].unique()
for county in counties:
    this_data = ca_data.loc[ca_data['County'] == county]
    county_filename = county.replace(' ','')
    this_data.to_csv(os.path.join(county_data_dir,county_filename+'.csv'))

