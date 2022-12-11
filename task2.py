import pandas as pd
import json
import re

def task2():
    df = pd.read_csv('../course/data/dataset.csv')
    rows_prod_avgscore = []

    for i, row in df.iterrows():
        prod_id = row['ID']
        prod_cat = row['category']
        revlst_str = row['REVIEWLIST']
        avg_score = 0  #If all entries are invalid star ratings default to 0
        score_lst = []
        rev_lst = json.loads(revlst_str)
  
        for review in rev_lst:
            raw_star = review["review_star"]
            star = re.search(r'(?<=a-star-)\d',raw_star) #Positive lookbehind

            if star:
                score_lst.append(int(star.group()))
        if len(score_lst): 
            avg_score = sum(score_lst)/len(score_lst)
        rows_prod_avgscore.append({"ID":prod_id, "category":prod_cat, "average_score": avg_score})
    
    prod_avgscore = pd.DataFrame(rows_prod_avgscore)
    prod_avgscore = prod_avgscore.sort_values(by='ID')
    prod_avgscore.to_csv('task2.csv',index=False)
    
    return
    
