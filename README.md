# Airbnb Price Prediction in Austin, Texas Using Machine Learning Models

This repository contains the code and data for predicting Airbnb prices in Austin, Texas. The project aims to provide insights into the pricing patterns and help users analyze availability and predict future prices for Airbnb listings in Austin.

## Objective:
The primary objectives of this project are:

*  Forecast Airbnb listing prices in Austin, Texas using various predictive models tailored to the local market, such as linear regression, random forest, and XGBoost. These models capture price trends and fluctuations, providing valuable insights to hosts and potential guests.
*  Identify key factors impacting Airbnb listing prices in Austin, Texas, including property features, geographical positioning, seasonal trends, reviews, and local attractions. Enable hosts to optimize pricing strategies and empower guests to make informed choices aligned with their preferences and budget

## Motivation:

*  Address the challenge of fluctuating Airbnb prices in Austin, Texas by enabling hosts to optimize pricing strategies based on property features, location, seasonal trends, reviews, and local attractions. Guests can make informed choices based on factors that impact prices, aligning their accommodation with preferences and budget.

## About The Data

The data used for this project is from the [Inside Airbnb](http://insideairbnb.com/get-the-data) website, which provides detailed information on Airbnb rentals in various cities, [Kaggle](https://www.kaggle.com/datasets/clnguyen/austinairbnbs20191112) and [GitHub.](https://github.com/PreetJhanglani/AirBnB-Austin) Our focus is on the Austin, Tx datasets. More specifically the "listings", "calendar" and, "reviews" datasets. 

*  Listings: This dataset contains detailed information on each Airbnb listing, including the host's id, room type, and pricing.
*  Reviews: This dataset contains information on the reviews for each listing, including the listing id, date of review and the review comment.
*   Calendar: This dataset contains information on the availability and pricing of each listing.



## Project Structure
The repository is organized into the following folders:

*  **Calendar Folder:** Contains calendar data for Airbnb prices, including information about listing availability, prices, and booking duration.
*  **Listings Folder:** Contains data related to Airbnb listings in Austin, Texas.
*  **Reviews Folder:** Contains guest reviews from Airbnb listings in Austin, Texas.
*  **Model Folder:** Contains the code and models for price prediction.

### Listings Folder
The listings folder contains data related to Airbnb listings in Austin, Texas. This includes information about the properties, hosts, and various attributes of the listings. Further details about the specific data files and their usage can be found within the folder.

The Listings dataset has an initial total of 74 features which can be categorized into following types:   <br>
Location related <br>
Property related <br>
Booking availability <br>
Reviews related <br>
Host related <br>
Amenities <br>

*  **unprocessed_listings.csv:** This CSV contains the raw listings information from Austin, Tx.

*  **processed_listings.csv:** This CSV file contains the processed data for the airbnb listings. 

*  The notebook **listings_preprocessing.ipynb** provides the code and steps for preprocessing the listing data. It applies various techniques to clean and format the data.

### Calendar Folder

The calendar folder contains the calendar data for Airbnb prices. It includes the unprocessed and processed calendar data files, which cover the period from June 8, 2022, to March 29, 2024.

*  **unprocessed_calendar.csv:** The unprocessed calendar data from June 8, 2022, to March 29, 2024. This file serves as the raw data for Airbnb prices and is required for data preprocessing and model training. Note that the unprocessed_calendar.csv file is not included in the project repository due to its large size, but you can obtain it from the provided dataset [link.](https://drive.google.com/file/d/1PAUs5dKBzr9YGiPUZ9wX-mh7j1xU7XA3/view?usp=drive_link)

*  **processed_calendar.csv:** The processed calendar data with no missing time period.The processed data file can be accessed from the provided [link.](https://drive.google.com/file/d/1m4rKk1EuiXX1gBwAHv835HLzcTidprRX/view?usp=drive_link)
  
*  The notebook **calendar_preprocessing.ipynb** provides the code and steps for preprocessing the calendar data. It applies various techniques to clean and format the data, generates new data for the missing time period, and visualizes the data using plots and charts. To address the missing time period from April 22, 2021, to June 7, 2022, new data has been generated to fill the gap in the processed_calendar.csv file. The notebook provides details on the preprocessing steps applied to the data.

### Reviews Folder

The reviews folder contains guest reviews from Airbnb listings in Austin, Texas. It provides valuable insights into the experiences, feedback, and satisfaction levels of guests who have stayed at various Airbnb accommodations in the city. The reviews data can be used for sentiment analysis and understanding guest preferences.

*  **unprocessed_reviews.csv:** This CSV file contains the unprocessed reviews from March 17, 2009, to March 16, 2023. The reviews are valuable data points that provide important feedback on the guest's experience with a listing. Sentiment analysis will be implemented on this dataset using the Valence Aware Dictionary for Sentiment Reasoning (VADER). The unprocessed review dataset can be accessed from the provided dataset [link.](https://drive.google.com/file/d/1fZoeCFgwXsmnkGZ6Y-35U3pV-TiGOaxf/view?usp=drive_link)
  
*  **bert_reviews.csv:** This CSV file is slightly processed and ready for sentiment analysis implementation. The dataset can be accessed from the provided dataset [link.](https://drive.google.com/file/d/1Oj8-dwb_X5dHOI-_b0ZuMM3c1ewhuRba/view?usp=drive_link)
  
*  **processed_reviews.csv:** This CSV file contains the processed Airbnb reviews. Sentiment analysis has been implemented on this dataset using VADER. The processed review dataset can be accessed from the provided dataset [link.](https://drive.google.com/file/d/1wPvDpL23QYRgMDcG057o8jWMZsKwfWFE/view?usp=drive_link)

*  The notebook **sentimen_analysis.ipynb** implements sentiment analysis using VADER and the pre-trained ROBERTa model. The ROBERTa model is fine-tuned on the Yelp reviews dataset to predict sentiment. The notebook applies the ROBERTa model and VADER on the reviews dataset to analyze sentiments.
  
*  The notebook **reviews_preprocessing.ipynb** provides the steps for preprocessing the reviews dataset for data exploration. It applies various techniques to clean and format the data and visualizes the data using plots and word clouds.

### Sentiment Analysis Packages

The following packages are used for sentiment analysis:

*  NLTK: The Natural Language Toolkit is a library in Python that provides tools for natural language processing, including sentiment analysis. It is used in this project for Valence Aware Dictionary for Sentiment Reasoning (VADER) sentiment analysis.
*  emoji: This package provides a range of utilities for working with emojis in Python.


### Model Folder
The model folder contains the code and models used for price prediction. This includes various predictive models such as linear regression, random forest, and XGBoost. The models are designed to capture the trends and fluctuations in Airbnb listing prices in Austin.

*  The **merge_datasets.ipynb** notebook contains the code and steps for merging the reviews dataset with the processed calendar dataset and processed listings dataset.
*  Then the folder contains the feature selection methods as well as all of our current models (Lasso/Ridge Regressions, Random Forest, XGBoost).

## Package Versions
The notebooks in this project were developed using specific package versions, including pandas, numpy, matplotlib, seaborn, and statsmodels. Please ensure you have the appropriate package versions installed to reproduce the results.

The notebooks in this project were developed using the following package versions: <br>
pandas: 1.5.3 <br>
numpy: 1.22.4 <br>
matplotlib: 3.7.1 <br>
scipy: 1.10.1 <br>
Seaborn: 0.12.2 <br>
statsmodels: 0.13.5 <br>

## Getting Started

To get started with the project, follow these steps:

1.  Download the required datasets from the provided links.
2.  Install the necessary package versions mentioned above using pip.
3.  Run the project code using your preferred Python environment.

Please ensure that you have the correct file paths or access to the datasets to run the notebooks successfully.

Feel free to explore the project code, datasets, and notebooks to analyze Airbnb prices and guest reviews in Austin, Texas.





