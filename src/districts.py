##################################################
###### Import Libraries
##################################################
# Libraries
import numpy as np
import pandas as pd

##################################################
###### Import Data: Read the file from AWS S3
##################################################

path_file = 'TFM/crime_philadelphia_20062019.csv'

# To Read files from AWS S3
import boto3
import io
s3 = boto3.client('s3')

obj = s3.get_object(Bucket='data-eml', Key=path_file)

data = pd.read_csv(io.BytesIO(obj['Body'].read()))

print('Data Imported from AWS S3')

##################################################
###### From DataFrame to Districts
##################################################
# Select Columns
data = data[['dispatch_date','dispatch_time','dc_dist','psa','location_block','ucr_general','text_general_code','point_x','point_y']]
# Parse Dates
data['dispatch_date'] = pd.to_datetime(data['dispatch_date'])
# Select Index
data.set_index('dispatch_date',drop=True,inplace=True)

# List of Philadelphia Distrcists
districts = data['dc_dist'].unique().tolist()
# Creating new DF
df = pd.DataFrame()
# City Column
df['city'] = data.groupby(pd.Grouper(freq="M"))['dc_dist'].count()
# District Columns
for dist in districts:
    dis_str = str(dist)
    df['dist_'+ dis_str] = data[data['dc_dist'] == dist].groupby(pd.Grouper(freq="M"))['dc_dist'].count()
# Remove the last month
df = df.iloc[:(len(df)-1)]

# Removing some columns with na values
cols_to_drop = ['dist_4','dist_23','dist_92']
df.drop(columns=cols_to_drop,inplace=True)

df.to_csv('../data/CSV/city_districts.csv')

print('Data Saved')