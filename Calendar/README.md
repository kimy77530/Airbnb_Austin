# Airbnb Calendar Data for Prices
This repository contains calendar data for Airbnb prices, which includes information about listing availability, prices, and booking duration. The data covers the period from June 8, 2022, to March 29, 2024. The dataset is available in two formats: "unprocessed_calendar.csv" and "processed_calendar.csv".

## Calendar Data Features and Description
The calendar dataset consists of the following features:
<br>
| Feature | Type | Description |
|:----------:|:----------:|:----------:|
|listing_id|Integer|Unique id given to every listing |
|date|Date|Calendar date for reservations|
|available|Boolean|Boolean value for availability of booking. False: "unavailable", True: "available"|
|price|Numeric | Price per night of booking or reservation|
|adjusted_price|Numeric |Adjusted price per night of booking or reservation|
|minimum_nights | Integer | Minimum number of nights for booking
|maximum_nights |Integer | Maximum number of nights for booking

### Data Files

*  **unprocessed_calendar.csv:** This file contains the unprocessed calendar data from June 8, 2022, to March 29, 2024. There is a gap in the data from April 22, 2021, to June 7, 2022. Before running the notebook, make sure to provide the path to the unprocessed_calendar.csv file. This file serves as the raw data for the Airbnb prices and is required for data preprocessing and model training. Ensure that the unprocessed_calendar.csv file is located in the correct directory or specify the correct file path in the code. Please note that the unprocessed_calendar.csv file is not included in the project repository due to its large size. However, you can obtain the dataset [here.](https://drive.google.com/file/d/1PAUs5dKBzr9YGiPUZ9wX-mh7j1xU7XA3/view?usp=drive_link) Once you have obtained the unprocessed_calendar.csv file, place it in the designated directory and update the file path accordingly in the code.
  
*  **processed_calendar.csv:** This file contains the processed calendar data from calendar_preprocessing.ipynb with no missing time period. [Processed data link](https://drive.google.com/file/d/1m4rKk1EuiXX1gBwAHv835HLzcTidprRX/view?usp=drive_link) 

*  The notebook **calendar_preprocessing.ipynb** provides the code and steps for preprocessing the calendar data. It applies various techniques to clean and format the data, generates new data for the missing time period, and visualizes the data using plots and charts.
To address the missing time period from April 22, 2021, to June 7, 2022, new data has been generated to fill the gap in the processed_calendar.csv file. The calendar_preprocessing.ipynb notebook provides the details of the preprocessing steps applied to the data.

### Usage
The calendar data can be used for various purposes, such as analyzing pricing patterns, identifying popular booking dates, or predicting future prices. Users can leverage this dataset for research, data analysis, or machine learning projects related to Airbnb prices and availability.

### Package Versions
The **calendar_preprocessing.ipynb** notebook was developed using the following package versions: <br>
pandas version: 1.5.3 <br>
numpy version: 1.22.4 <br>
matplotlib version: 3.7.1 <br>
scipy version: 1.10.1 <br>
Seaborn version: 0.12.2 <br>
statsmodels version: 0.13.5 <br>

### Package Description:
*  pandas: pandas is a powerful data manipulation and analysis library in Python. It provides easy-to-use data structures and data analysis tools, making it efficient for working with structured data.

*  numpy: numpy is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.

*  matplotlib: matplotlib is a popular plotting library in Python. It provides a wide range of visualization options for creating static, animated, and interactive plots. It is widely used for creating charts, histograms, scatter plots, and more.

*  seaborn: seaborn is a data visualization library built on top of matplotlib. It provides a high-level interface for creating attractive and informative statistical graphics. Seaborn simplifies the process of creating complex visualizations and supports various types of plots, including heatmaps, box plots, and violin plots.

*  statsmodels: statsmodels is a Python module that provides a comprehensive set of statistical models and tools for statistical data analysis. It includes a wide range of statistical techniques, such as regression analysis, time series analysis, and hypothesis testing.
