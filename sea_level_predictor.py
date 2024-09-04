"""    freecodecamp data analysis project5    """

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv")
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']


    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x,y)

    # Create first line of best fit
    r = linregress(x,y)
    print(r)
    x_pred = pd.Series([i for i in range(1880,2051)])
    y_pred = r.slope*x_pred + r.intercept
    plt.plot(x_pred, y_pred, 'r')


    # Create second line of best fit
    new_df = df.loc[df['Year']>=2000]
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']
    x_pred1 = pd.Series([i for i in range(2000,2051)])
    r1 = linregress(new_x,new_y)
    y_pred1 = r1.slope*x_pred1 + r1.intercept
    plt.plot(x_pred1, y_pred1, 'g')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title("Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()