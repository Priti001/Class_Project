

```python
import pandas as pd
from housing_utilities import retrieve_data
import matplotlib.pyplot as plt
```


```python
school_data = pd.read_csv('School_Scores_Data_Summary.csv')
```


```python
lookup = pd.read_csv('CA_lookup.csv')

counties = lookup['County']

upper = lambda x: x.upper()
school_params = {'min_grade':9,
                'max_grade': 12,
                'subject': ['Mathematics','English Language Arts/Literacy']}

min_threshold = 5

for county in counties:
    this_county_housing = retrieve_data(county)
    # clean city name to join with school data
    this_county_housing['City'] = this_county_housing['City'].apply(upper)
    this_sample_house = this_county_housing.groupby(['City'])['MedianSoldPricePerSqft_AllHomes'].mean()
    for subject in school_params['subject']:
        this_school_sample = school_data.where(
            school_data['Test Name']==subject).where(
            school_data['Grade'] >= school_params['min_grade']).where(
            school_data['County Name']==county).dropna().groupby(['City']).mean()
        data_to_plot = pd.concat([this_sample_house,this_school_sample],axis=1).dropna(how='any')
        if len(data_to_plot) >= min_threshold:
            plt.plot(data_to_plot['2015-2017 Avg Percentage Standard Met and Above'],
                     data_to_plot['MedianSoldPricePerSqft_AllHomes'],'.')
            plt.title('%s Performance vs. Price/Sq. Ft. in %s County' % (subject.split(' ')[0],county))
            plt.grid(True)
            plt.xlabel('% Meeting or Above Subject Standard')
            plt.ylabel('Median $/Sq Ft')
            plt.xlim([0,100])
            plt.show()
        else:
            print('%s County has less than %s datapoints to plot for %s performance' % (county,min_threshold,subject))
```


![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_0.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_1.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_2.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_3.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_4.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_5.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_6.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_7.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_8.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_9.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_10.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_11.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_12.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_13.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_14.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_15.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_16.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_17.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_18.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_19.png)


    Napa County has less than 5 datapoints to plot for Mathematics performance
    Napa County has less than 5 datapoints to plot for English Language Arts/Literacy performance



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_21.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_22.png)


    Calaveras County has less than 5 datapoints to plot for Mathematics performance
    Calaveras County has less than 5 datapoints to plot for English Language Arts/Literacy performance



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_24.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_25.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_26.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_27.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_28.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_29.png)


    Kings County has less than 5 datapoints to plot for Mathematics performance
    Kings County has less than 5 datapoints to plot for English Language Arts/Literacy performance



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_31.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_32.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_33.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_34.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_35.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_36.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_37.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_38.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_39.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_40.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_41.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_42.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_43.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_44.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_45.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_46.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_47.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_48.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_49.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_50.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_51.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_52.png)


    Inyo County has less than 5 datapoints to plot for Mathematics performance
    Inyo County has less than 5 datapoints to plot for English Language Arts/Literacy performance
    Imperial County has less than 5 datapoints to plot for Mathematics performance
    Imperial County has less than 5 datapoints to plot for English Language Arts/Literacy performance
    Yuba County has less than 5 datapoints to plot for Mathematics performance
    Yuba County has less than 5 datapoints to plot for English Language Arts/Literacy performance



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_54.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_55.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_56.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_57.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_58.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_59.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_60.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_61.png)


    Colusa County has less than 5 datapoints to plot for Mathematics performance
    Colusa County has less than 5 datapoints to plot for English Language Arts/Literacy performance
    Tehama County has less than 5 datapoints to plot for Mathematics performance
    Tehama County has less than 5 datapoints to plot for English Language Arts/Literacy performance



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_63.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_64.png)


    Yolo County has less than 5 datapoints to plot for Mathematics performance
    Yolo County has less than 5 datapoints to plot for English Language Arts/Literacy performance
    Siskiyou County has less than 5 datapoints to plot for Mathematics performance
    Siskiyou County has less than 5 datapoints to plot for English Language Arts/Literacy performance
    Humboldt County has less than 5 datapoints to plot for Mathematics performance
    Humboldt County has less than 5 datapoints to plot for English Language Arts/Literacy performance
    Mendocino County has less than 5 datapoints to plot for Mathematics performance
    Mendocino County has less than 5 datapoints to plot for English Language Arts/Literacy performance
    Nevada County has less than 5 datapoints to plot for Mathematics performance
    Nevada County has less than 5 datapoints to plot for English Language Arts/Literacy performance



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_66.png)



![png](Exploratory%20Comparison_files/Exploratory%20Comparison_2_67.png)


    San Benito County has less than 5 datapoints to plot for Mathematics performance
    San Benito County has less than 5 datapoints to plot for English Language Arts/Literacy performance
    Amador County has less than 5 datapoints to plot for Mathematics performance

