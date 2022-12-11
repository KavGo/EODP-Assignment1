import pandas as pd
import matplotlib.pyplot as plt

def task5():
    df = pd.read_csv('task2.csv')
    avgsc_cat = df.groupby('category')['average_score'].mean().sort_values()
    
    #Create a bar chart
    plt.style.use('fivethirtyeight') 
    ax = avgsc_cat.plot.barh(figsize=(10,14))
    ax.set_title('Mean rating for each catagory')
    ax.set_ylabel('Catagory')
    ax.set_xlabel('Mean rating')
    fig = ax.get_figure()
    plt.tight_layout()
    fig.savefig('task5.png')
    return
