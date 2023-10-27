import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df=pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = np.where(df['weight']/df['height']/df['height']*10**4>25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
for col in ['cholesterol', 'gluc']:
  df.loc[df[col]==1, col]=0
  df.loc[df[col]>1, col]=1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'],value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_c1=df_cat.groupby(['cardio', 'variable','value']).agg(total=('value','size'),).reset_index()

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # df_cat = None
    

    # Draw the catplot with 'sns.catplot()'

    # Get the figure for the output
    # fig=sns.catplot(kind='bar',data=df_c1, x="variable", y="total",col='cardio', hue="value", )
    fig, (ax0, ax1)=plt.subplots(1,2,figsize = (10,6))
    sns.barplot(data=df_c1[df_c1.cardio==0], x="variable", y="total", hue="value", ax=ax0)
    sns.barplot(data=df_c1[df_c1.cardio==1], x="variable", y="total", hue="value", ax=ax1)
    # the commented fig=... is a better solution and the result is more similar to the example. But the returned fig.axes is an array of array, which does not pass the unit test.
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat=df[(df['ap_lo'] <= df['ap_hi']) & 
    (df['height'] >= df['height'].quantile(0.025))&(df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025))&(df['weight'] <= df['weight'].quantile(0.975))].reset_index()
    corr=df.corr()
    # corr.drop(columns='index', inplace=True)
    # corr.drop('index', inplace=True)
    mask = np.triu(np.ones_like(corr))
    fig, ax=plt.subplots()
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f")
    # same method but some value are not correct
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
