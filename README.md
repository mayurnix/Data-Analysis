# Data Analysis Projects

This repository contains several Python-based data analysis projects focusing on statistical analysis, data visualization, and predictive modeling. Each project file includes a specific data analysis task and uses popular libraries such as NumPy, Pandas, Matplotlib, and Seaborn to derive insights from various datasets.

## Project Files Overview

### 1. **mean_var_std.py**
   - **Description**: Defines a function `calculate()` that uses NumPy to compute statistical measures (mean, variance, standard deviation, max, min, and sum) for a 3x3 matrix.
   - **Input**: A list of 9 digits, which is reshaped into a 3x3 NumPy array.
   - **Output**: A dictionary containing the computed statistics across rows, columns, and for the flattened matrix.

### 2. **demographic_data_analyzer.py**
   - **Description**: Analyzes demographic data extracted from the 1994 Census using Pandas.
   - **Objective**: Extract insights on various demographic variables to observe trends and distributions.

### 3. **medical_data_visualizer.py**
   - **Description**: Explores medical data that includes patient information such as body measurements, blood test results, and lifestyle choices.
   - **Objective**: Investigate correlations between cardiac disease, body measurements, blood markers, and lifestyle factors.

### 4. **time_series_visualizer.py**
   - **Description**: Visualizes time series data using line charts, bar charts, and box plots.
   - **Dataset**: Daily page views on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03.
   - **Objective**: Understand visit patterns and identify yearly and monthly growth trends.

### 5. **sea_level_predictor.py**
   - **Description**: Analyzes and predicts global average sea level changes.
   - **Dataset**: Global sea level data from 1880 onwards.
   - **Objective**: Use historical data to predict sea level changes through the year 2050.

## Libraries Used
- **NumPy**: For numerical operations, matrix manipulation, and statistical calculations.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib** & **Seaborn**: For creating various data visualizations and exploring trends.

## How to Use
Each script is designed as a standalone module. To run a project:
1. Install required libraries: `pip install numpy pandas matplotlib seaborn`.
2. Run the specific Python script to view its output.
