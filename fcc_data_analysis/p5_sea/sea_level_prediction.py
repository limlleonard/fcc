import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df=pd.read_csv('epa-sea-level.csv')

    pred1=linregress(df.Year, df['CSIRO Adjusted Sea Level'])
    linex1=[i for i in range(df.Year.min(), 2051)]
    liney1=[x*pred1.slope+pred1.intercept for x in linex1]
    pred2=linregress(df[df.Year>1999].Year, df[df.Year>1999]['CSIRO Adjusted Sea Level'])
    linex2=[i for i in range(2000, 2050)]
    liney2=[x*pred2.slope+pred2.intercept for x in linex2]

    fig, ax = plt.subplots()
    ax.scatter(df.Year, df['CSIRO Adjusted Sea Level'])
    ax.plot(linex1, liney1, color='k', linewidth=2)
    ax.plot(linex2, liney2, color='r', linewidth=2)
    ax.set_ylabel('Sea Level (inches)')
    ax.set_xlabel('Year')
    ax.set_title('Rise in Sea Level')    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()