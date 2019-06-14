<p align="center"> 
<img src="https://github.com/emunozlorenzo/MasterDataScience/blob/master/img/image2.png">
</p>

# DataCop: A Crime Forecasting Tool


Master's Thesis Project

![alt text](https://github.com/emunozlorenzo/MasterDataScience/blob/master/img/icon2.png "Logo Title Text 1") [Eduardo Muñoz](https://www.linkedin.com/in/eduardo-mu%C3%B1oz-lorenzo-14144a144/)

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)

## Introduction


Through public open data generated and collected by many of the largest international cities, we can develope tech products in order to analise and forecast sociodemographic parameters such as crimes, emergencies, incomes, etc.
This allows us to manage and optimise public services and infrastructures.

The main goals of this project are:

- Crime analysis by districts
- 12 months Crime Forecast by districts using diffent time series models

## Repository Structure


- __data__ Inputs and outputs files are storaged in this folder
- __notebooks__ Jupyter Notebooks: Data preprocessing and time series models
- __src__ Source code related to data adquisition and data preprocessing
- __dashboard__ Tableau file where the results are shown
- __img__ Images

## Methodology

#### Data Adquisition

#### Data Preprocsessing

#### Analysis

#### Time Series Forecasting


## Requeriments and Data Adquisition

#### Install Requirements

```
pip3 install -r requirements.txt
```

#### Data Adquisition

Before you can begin using Boto 3, you should set up authentication credentials. Credentials for your AWS account can be found in the IAM Console

create the credential file yourself. By default, its location is at ```~/.aws/credentials```:

```sh
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```
You may also want to set a default region. This can be done in the configuration file. By default, its location is at ```~/.aws/config```:

```sh
[default]
region = eu-west-1
```

After this, one of these files must be run:

```sh
./src/data/dataAdquisitionAWS.py
```

or 

```sh
./data/01_Data_Adquisition_AWS_S3.ipynb
```

## Dashboard
The Dashboard has been developed using Tableau
Link: [Tableau Public Dashboard](https://public.tableau.com/views/DataCop_TFM_EML/Dashboard1?:embed=y&:display_count=yes&publish=yes&:origin=viz_share_link)

```
Forecast
```

<p align="center"> 
<img src="https://github.com/emunozlorenzo/DataCopCrimePrediction/blob/master/img/dataCopGreen.JPG">
</p>

```
Analysis
```

<p align="center"> 
<img src="https://github.com/emunozlorenzo/DataCopCrimePrediction/blob/master/img/dataCopBlue.JPG">
</p>


```
User Interface
```
![Playgrounds](https://github.com/emunozlorenzo/DataCopCrimePrediction/blob/master/img/dataCop.gif)
