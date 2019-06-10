# Libraries
import requests
import csv
import boto3

# Request the Dataset
data = requests.get('https://phl.carto.com:443/api/v2/sql?format=CSV&q=select * from phl.incidents_part1_part2')
print('Data Request Done')

# Converting Data 
with open('../../data/CSV/crime_philadelphia_20062019_v2.csv', 'w') as f:
    writer = csv.writer(f)
    reader = csv.reader(data.text.splitlines())

    for row in reader:
        writer.writerow(row)
print('Convert Data Done')
# Create a file in AWS S3

bucketName = "data-eml"
Key = "../../data/CSV/crime_philadelphia_20062019_v2.csv"
outPutname = "TFM/crime_philadelphia_20062019_v2.csv"

s3 = boto3.client('s3')
s3.upload_file(Key,bucketName,outPutname)
print('Upload File Done')