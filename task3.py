import pandas as pd
import re

def average_cost(raw_cost):
    avg_price = 0          #If the cost is not valid default to 0
    raw_cost = re.sub(r',', '', raw_cost)
    cost_str = re.findall(r'(?<=\$)\d*\.*\d*',raw_cost)
    if cost_str:
        avg_price = sum([float(x) for x in cost_str])/len(cost_str) 
    return format(avg_price,'.2f')

def task3():
    df = pd.read_csv('../course/data/dataset.csv')
    
    prod_row = []
    for i,row in df.iterrows():
        prod_id = row['ID']
        category = row['category']
        avg_cost = average_cost(row['cost'])
        prod_row.append({"ID": prod_id, "category": category, "average_cost": avg_cost})

    products = pd.DataFrame(prod_row)
    products = products.sort_values(by='ID')
    products.to_csv('task3.csv',index=False)
    
    return

