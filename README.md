
# Advanced Programming Final Project

## Introduction

Welcome to the final project for the Advanced Programming course. This project aims to conduct an in-depth analysis of a given dataset and create visualizations to provide comprehensive insights. The project involves data retrieval, preprocessing, descriptive data analysis, and visualization.

## Project Structure

- `project.py`: Contains the main code for data analysis and visualization.

## Setup and Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Install the required libraries:
    ```sh
    pip install pandas matplotlib seaborn scikit-learn
    ```

3. Ensure that the dataset `mushroom_cleaned.csv` is in the same directory as the `project.py` script.

## Usage

Run the `project.py` script to execute the data analysis and generate visualizations:
```sh
python project.py
```

## Project Overview

### Data Description

- **Dataset**: The dataset used is `mushroom_cleaned.csv`.
- **Columns**:
  - The dataset contains various features of mushrooms such as cap-shape, cap-surface, cap-color, and more.
  - The target variable is `class`, which indicates if the mushroom is edible or poisonous.

### Steps and Methods

1. **Data Loading and Initial Exploration**:
    - Load the dataset.
    - Display the first few rows and statistical summary.

2. **Data Preprocessing**:
    - Remove duplicates.
    - Remove rows with zero values in the 'stem-width' column.
    - Remove outliers using the IQR method.
    - Normalize data using MinMaxScaler.

3. **Visualization**:
    - Plot histograms to show the distribution of features.
    - Plot box plots to show the relation between features and the class.
    - Generate a correlation matrix heatmap.
    - Create scatter plots for highly correlated variables.

## Visualizations

1. **Feature Distribution**:
    - Histograms for each feature to visualize their distributions.
2. **Class Relationship**:
    - Box plots to visualize the relationship between each feature and the class.
3. **Correlation Matrix**:
    - Heatmap to display correlations between features.
4. **Scatter Plots**:
    - Scatter plots for pairs of highly correlated features.

## Conclusion

This project showcases the process of data cleaning, preprocessing, and visualization using Python libraries. The visualizations provide insights into the distribution of features and their relationships with the target variable.

## License

This project is licensed under the MIT License.
