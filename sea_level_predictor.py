import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig,ax=plt.subplots()
    ax.scatter(x=df['Year'],y=df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    slope, intercept, r_value, p_value, stderr = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years=np.arange(df['Year'].min(),2051)
    ax.plot(years,(years*slope+intercept),color='red',label="Best Line")

    # Create second line of best fit
    dff=df[(df['Year']>=2000)]
    slopes, intercepts, r_value, p_value, stderr = stats.linregress(dff['Year'], dff['CSIRO Adjusted Sea Level'])
    yy=pd.Series(range(2000,2051))
    ax.plot(yy,(yy*slopes)+intercepts,color='green',label="Best Line",zorder=2)

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    fig.savefig('sea_level_plot.png')
    return fig.gca()
