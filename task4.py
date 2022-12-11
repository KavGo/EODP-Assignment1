import pandas as pd
import matplotlib.pyplot as plt


def task4():
    df1 = pd.read_csv('task2.csv')
    df2 = pd.read_csv('task3.csv')
    
    avgsc_df = df1.loc[df1['category']=='Pet Supplies']
    avgprice_df = df2.loc[df2['category']=='Pet Supplies']

    #Merge the two dataframes
    combine = pd.merge(avgsc_df, avgprice_df, on="ID", how="inner")
    
    #Create a scatter plot with axes avgcost and avgscore
    plt.style.use('bmh') 
    fig, ax1 = plt.subplots()
    ax1.scatter(x=combine['average_cost'],y=combine['average_score'])
    ax1.set_title("Pet Supplies")
    ax1.set_xlabel("Average price ($)")
    ax1.set_ylabel("Average review score")
    plt.tight_layout()
    plt.savefig('task4.png')
    plt.close()

    return
