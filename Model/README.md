# Airbnb Model: Feature Selection, Linear Regression, and Random Forest

### Data Files
 *  **merge_datasets.ipynb** This notebook contains the code and steps for merging the reviews dataset with the processed calendar dataset and then with the processed listings dataset. The three datasets used are "processed_reviews.csv," "processed_calendar.csv," and "processed_listings.csv." Following the merge of the three datasets, the shape of the data frame is (18105646, 91).
  
*  **dataload_process.py** This script provides functions for encoding categorical columns and splitting data into features and target variables, which are commonly used preprocessing steps before applying machine learning algorithms.

*  **forward_selection.py** Includes two functions that work together to perform feature selection through feed forward selection. The forward_selection function uses the evaluate_features function to assess the performance of different feature combinations and selects the best-performing features based on the improvement in model accuracy (measured by MSE) on the test data.

*  **model_implementation.ipynb** This notebook initializes Lasso, Ridge, Elastic Net, Random Forest and XGBoost Regressor on original data with no feature selection.

*  **forward_selection_implementation.ipynb** This notebook implements feed forward selection and saves the filtered dataset. 

*  **all_models_feature_selected.ipynb** This notebook initializes Lasso, Ridge, Elastic Net, Random Forest and XGBoost Regressor with feed forward selection on the filtered dataset.

*  **crossvalidation_tune.ipynb** This notebook conducts randomized cross-validation on the feed-forward filtered dataset. It also incorporates SHAP on the model with best performance.



### Source of the Dataset:

The datasets utilzied within the "merge_datasets.ipynb" are sourced from the data processing steps found in "Calendar," "Listings," and "Reviews" folders. For ease with the feature selection notebooks, the merged dataset can be downloaded from the group's [Google drive.](https://drive.google.com/file/d/1vrxc_sT68YGYBgI9K15YlKWO7jQX8zu8/view?usp=drive_link)
The feed-forward dataset can be dowloaded [here.](https://drive.google.com/file/d/1-07MOYij0cpKF1Ca3IjGKRBdaDCx9FjY/view?usp=drive_link)
### Package Versions and Imports

To successfully run the notebook and reproduce the results, ensure that you have the following package versions installed: <br>
pandas version: 1.5.3 <br>
numpy version: 1.22.4 <br>
matplotlib version: 3.7.1 <br>
mrmr version: 0.2.8 <br>

*  pandas: pandas is a powerful data manipulation and analysis library in Python. It provides easy-to-use data structures and data analysis tools, making it efficient for working with structured data.

*  matplotlib: matplotlib is a popular plotting library in Python. It provides a wide range of visualization options for creating static, animated, and interactive plots. It is widely used for creating charts, histograms, scatter plots, and more.

*  numpy: numpy is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.

* mrmr: MRMR, or Maximum Relevance - Minimum Redundancy, is classified as a minimal-optimal feature selection package algorithm. Its use is due to its prowness compared to SelectKBest for the feature selection before the results are implemented into the Linear Regression and Random Forest models.

You can install the required packages using `pip`:  <br>
`!pip install -q contractions` <br>


### Getting Started

To get started with the project, follow these steps:

1. Download the datasets from the respective folders. 
2. Install the required dependencies as mentioned above.
3. Run the project code using your preferred Python environment.
