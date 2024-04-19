# Airbnb Reviews Dataset - Austin, TX
The Airbnb Reviews dataset contains a comprehensive collection of guest reviews from Airbnb listings in Austin, Texas. This dataset provides valuable insights into the experiences, feedback, and satisfaction levels of guests who have stayed at various Airbnb accommodations in Austin.

## Features and Description
The reviews dataset includes the following key features:

| Feature | Type | Description |
|:----------:|:----------:|:----------:|
|listing_id|Numeric|Unique id given to every listing |
|id|Numeric|Unique id given to every review|
| date   |Date|Date on which review was given|
|reviewer_id|Numeric|Unique id given to every reviewer|
|reviewer_name|Character|Name of the reviewer|
|comments|Character|Review given by the guest/reviewer|

The dataset covers a wide range of listings in Austin, Texas, offering insights into guest experiences, sentiments, and overall satisfaction levels. Analyzing this dataset can help identify popular listings, assess the quality of accommodations, and gain a deeper understanding of guests' preferences and feedback.

### Data Files
*  **pre_process_reviews.py** This scripts includes all the pre-processing functions for the reviews data.

*  **unprocessed_reviews.csv:** This CSV file contains the unprocessed reviews from March 17, 2009 to March 16, 2023. The reviews are valuable data points that provide important feedback on the guest's experience with a listing. It allows for additional insight beyond the standard ratings, offering detailed sentiments and comments. Sentiment Analysis will be implemented on this dataset using Valence Aware Dictionary for Sentiment Reasoning (VADER) and the pre-trained ROBERTa model. The unprocessed review dataset can be accessed from our project's [Google drive.](https://drive.google.com/file/d/1fZoeCFgwXsmnkGZ6Y-35U3pV-TiGOaxf/view?usp=drive_link)

*  **bert_reviews.csv:** This CSV file is slighty processed and ready for sentiment analysis implementation. The dataset can be accessed from our project's [Google drive.](https://drive.google.com/file/d/1Oj8-dwb_X5dHOI-_b0ZuMM3c1ewhuRba/view?usp=drive_link)

*  **processed_reviews.csv:** This CSV file contains the processed Airbnb reviews. Sentiment Analysis has been implemented on this dataset using Valence Aware Dictionary for Sentiment Reasoning (VADER). The processed review dataset can be accessed from our project's [Google drive.](https://drive.google.com/file/d/1wPvDpL23QYRgMDcG057o8jWMZsKwfWFE/view?usp=drive_link)

*  **sentiment_analysis.ipynb** This notebook implements sentiment analysis using VADER and the pre-trained ROBERTa model. The ROBERTa model is fine-tuned on the [yelp reviews dataset.](https://huggingface.co/datasets/yelp_polarity) to predict sentiment. The notebook applies the ROBERTa model and VADER on the reviews dataset to analyze sentiments. For this project, VADER was the only tool used. Roberta requires sufficient RAM to work on large datasets. 

*  **reviews_preprocessing.ipynb** This notebook provides the steps for preprocessing the reviews dataset for data exploration. It applies various techniques to clean and format the data, and visualizes the data using plots and word clouds.
  
The VADER (Valence Aware Dictionary for Sentiment Reasoning) module is an NLTK module that provides sentiment scores based on the words used. It is a rule-based sentiment analyzer in which the terms are generally labeled as positive or negative based on their semantic orientation. VADER is intelligent enough to understand basic context and modifiers, allowing it to interpret phrases like "did not love" as a negative statement. It also takes into account capitalization and punctuation for emphasis, such as "ENJOY".
  
ROBERTa is a large pre-trained language model developed by Facebook AI and released in 2019. It shares the same architecture as the BERT model but with minor adjustments to key hyperparameters and embeddings. ROBERTa is used for various downstream tasks, including sentiment analysis. The model parameters are fine-tuned on specific datasets to make accurate predictions.

### Source of the Dataset:
The Airbnb Reviews dataset for Austin, Texas can be obtained from the official Inside Airbnb website. You can access and download the dataset from the following source: [Inside Airbnb.](http://insideairbnb.com/get-the-data/)

To use the Airbnb Reviews notebook, please ensure that you have the appropriate file path or access to the dataset.

### Package Versions and Imports

To successfully run the notebook and reproduce the results, ensure that you have the following package versions installed: <br>
Seaborn version: 0.12.2 <br>
pandas version: 1.5.3 <br>
numpy version: 1.22.4 <br>
matplotlib version: 3.7.1 <br>
emoji version: 2.6.0 <br>
re version: 2.2.1 <br>
nltk version: 3.8.1 <br>

*  seaborn: seaborn is a data visualization library built on top of matplotlib. It provides a high-level interface for creating attractive and informative statistical graphics. Seaborn simplifies the process of creating complex visualizations and supports various types of plots, including heatmaps, box plots, and violin plots.

*  pandas: pandas is a powerful data manipulation and analysis library in Python. It provides easy-to-use data structures and data analysis tools, making it efficient for working with structured data.

*  matplotlib: matplotlib is a popular plotting library in Python. It provides a wide range of visualization options for creating static, animated, and interactive plots. It is widely used for creating charts, histograms, scatter plots, and more.

*  numpy: numpy is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.

*  emoji: emoji is a Python package that provides a range of utilities for working with emojis. It allows you to easily access and manipulate emojis in your text data. This package can be helpful when dealing with sentiment analysis, text processing, or any task involving emojis.

*  re: re is the built-in regular expression module in Python. It provides a set of functions and patterns for working with regular expressions, which are powerful tools for pattern matching and text manipulation. The re module is commonly used for tasks such as text extraction, text cleaning, and pattern-based data processing.

*  nltk: nltk (Natural Language Toolkit) is a library in Python that provides tools and resources for working with human language data. It offers a wide range of functionalities for tasks such as text processing, tokenization, stemming, lemmatization, part-of-speech tagging, and sentiment analysis. nltk is a popular choice for natural language processing (NLP) tasks and research.



You can install the required packages using `pip`:  <br>
`!pip install -q contractions` <br>
`!pip install emoji==2.6.0` <br>
`!pip install NLTK==3.8.1` <br>

### Getting Started

To get started with the project, follow these steps:

1. Download the Austin, Tx Airbnb reviews dataset from [Inside Airbnb](http://insideairbnb.com/get-the-data/) or [Google drive.](https://drive.google.com/file/d/1fZoeCFgwXsmnkGZ6Y-35U3pV-TiGOaxf/view?usp=drive_link)
2. Install the required dependencies as mentioned above.
3. Run the project code using your preferred Python environment.



