
# coding: utf-8
def retrieve_data(*args, debug=False):
    import os,sys
    import pandas as pd
    
    # input parsing
    counties = args
    if len(counties) > 1:
        need_combine = True
        output = []
    else:
        need_combine = False
    
    # constants/defaults
    lookup_file = 'CA_lookup.csv'
    detail_directory = 'data_by_county'
    
    
    # load lookup table
    nearby_files = os.listdir()
    if lookup_file not in nearby_files:
        lookup_file = input('Please enter file path to lookup table\n')
    lookup = pd.read_csv(lookup_file)  
    
    for county in counties:
        # confirm county is in lookup
        if debug: print('looking up %s' % county)
        if lookup['County'].isin([county]).any():
            if debug: print('found %s in %s' % (county,lookup_file))
            detail_file = lookup.loc[lookup['County'] == county,'File Name'].values[0]
                # assumes detail_file command above will pull a singular list. [0] strips list to string.
            if detail_directory not in nearby_files:
                detail_path = input('Please enter the directory to detail files\n')
            detail_path = os.path.join(detail_directory,detail_file)

            # load detail data
            data = pd.read_csv(detail_path)
            if debug: print('%s loaded successfully' % detail_path)
            if need_combine and len(output) > 0:
                output = pd.concat([output,data],axis=0,ignore_index=True)
            else:
                output = data
        else:
            print('%s not in %s' % (county,lookup_file))
    if len(output) > 0:
        return output
    else:
        print('Could not find any county(s) entered.')

def str2unix(s):
    import datetime, time
    return time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d").timetuple())

def convert_timescale(x):
    return x/(60*60*24*365)

def extract_year(x):
    import datetime, time
    return datetime.datetime.strptime(x, "%Y-%m-%d").timetuple().tm_year

def express_as_year(x):
    return convert_timescale(str2unix(x))%1+extract_year(x)

def plot_housing_data(df, x_metric = 'Date',y_metric = 'MedianSoldPricePerSqft_AllHomes'):
    import matplotlib.pyplot as plt
    import pandas as pd
    
    if x_metric == 'Date':
        x_data = df[x_metric].apply(express_as_year)
    else:
        x_data = df[x_metric]
    
    y_data = df[y_metric]
    
    plt.plot(x_data,y_data,'.')
    plt.grid(True)
    plt.show()



