import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

def forward_selection(train_df, train_y, test_df, test_y):
    """
    Perform forward selection for feature selection.

    This function iteratively selects the best feature to add to the set of selected features
    based on the improvement in mean squared error (MSE) on the test set.

    Parameters:
    train_df (DataFrame): The training data features.
    train_y (array-like): The training data target values.
    test_df (DataFrame): The test data features.
    test_y (array-like): The test data target values.

    Returns:
    list: The list of selected feature indices.
    """
    num_features = train_df.shape[1]
    selected_features = []
    best_features = None
    global_best_error = float('inf')

    for _ in range(num_features):
        remaining_features = [feature for feature in range(num_features) if feature not in selected_features]
        current_error = evaluate_features(train_df, train_y, test_df, test_y, selected_features, remaining_features)
        
        best_feature_index = np.argmin(current_error)
        recent_best_error = current_error[best_feature_index]
        best_feature = remaining_features[best_feature_index]

        selected_features.append(best_feature)

        if recent_best_error < global_best_error:
            global_best_error = recent_best_error
            best_features = selected_features.copy()

    return best_features

def evaluate_features(train_df, train_y, test_df, test_y, selected_features, remaining_features):
    """
    Evaluate the performance of different feature combinations.

    This function trains Linear Regression models with different feature combinations
    and calculates the mean squared error (MSE) on the test set for each combination.

    Parameters:
    train_df (DataFrame): The training data features.
    train_y (array-like): The training data target values.
    test_df (DataFrame): The test data features.
    test_y (array-like): The test data target values.
    selected_features (list): The list of selected feature indices.
    remaining_features (list): The list of remaining feature indices to evaluate.

    Returns:
    list: List of mean squared errors for each evaluated feature combination.
    """
    current_error = []
    for feature in remaining_features:
        temp_features = selected_features + [feature]

        model = LinearRegression()
        model.fit(train_df.iloc[:, temp_features], train_y)

        y_pred = model.predict(test_df.iloc[:, temp_features])
        mse = mean_squared_error(test_y, y_pred)
        current_error.append(mse)

    return current_error
