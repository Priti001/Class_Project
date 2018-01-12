
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

# Output(s)
# - 'CA_lookup.csv'
# - directory: 'data_by_county'
#     - county_1.csv
#     - ...
#     - county_n.csv

# In[1]:


# Dependencies
import sys
import os
import pandas as pd
import datetime


# In[2]:


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


# In[3]:


def extract_year(x, dateformat = "%Y-%m-%d"):
    return datetime.datetime.strptime(x, dateformat).timetuple().tm_year


# In[4]:


# Filter to only: CA
ca_data = combine.loc[combine['State']=='CA'].dropna(axis='columns',how='all')
ca_data.to_csv('CA_Zillow_data.csv')
county_data_dir = 'data_by_county'

# Create Index of files
template = pd.DataFrame({
    'County' : [],
    'State' : 'CA',
    'File Name' : [],
    'Min Date': [],
    'Max Date': [],
    'Min Price Per Sq Ft': [],
    'Max Price Per Sq Ft': []
})

county_profile = template

# Save detail data by county
try:
    os.stat(county_data_dir)
except:
    os.mkdir(county_data_dir)

counties = ca_data['County'].unique()

for county in counties:
    this_data = ca_data.loc[ca_data['County'] == county]
    county_filename = county.replace(' ','')+'.csv'
    this_data.to_csv(os.path.join(county_data_dir,county_filename))
    this_index_entry = pd.DataFrame({
            'County' : county,
            'State' : 'CA',
            'File Name' : county_filename,
            'Min Year': this_data['Date'].apply(extract_year).min(),
            'Max Year': this_data['Date'].apply(extract_year).max(),
            'Min Price Per Sq Ft': this_data['MedianSoldPricePerSqft_AllHomes'].min(),
            'Max Price Per Sq Ft': this_data['MedianSoldPricePerSqft_AllHomes'].max()
        }, index=[0])
    county_profile = pd.concat([county_profile,this_index_entry],axis=0,ignore_index=True)
    
county_profile.to_csv('CA_lookup.csv')
    

