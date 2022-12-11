from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
import json
from math import log

def positive_negative(rev_lst):
    pos_dict = defaultdict(int) 
    neg_dict = defaultdict(int)
    bigram_lst = []
    n_pos = 0
    n_neg = 0
    
    for review in rev_lst:
        #Negative reviews
        if review["score"]==1:
            n_neg+=1
            for bigram in set(review["bigrams"]):
                neg_dict[bigram]+=1
                bigram_lst.append(bigram)
        #Positive reviews
        elif review["score"]==5:
            n_pos+=1
            for bigram in set(review["bigrams"]):
                pos_dict[bigram]+=1
                bigram_lst.append(bigram)
        else:
            continue 
    return (pos_dict,neg_dict,list(set(bigram_lst)),n_pos,n_neg)
         

def task7():
    with open('task6.json') as json_file:
        reviews = json.load(json_file)
    (pos_dict,neg_dict,bigram_lst,n_pos,n_neg) = positive_negative(reviews)

    #Calulate probabilities
    pos_prob = {bigram:pos_dict[bigram]/n_pos for bigram in bigram_lst}
    neg_prob = {bigram:neg_dict[bigram]/n_neg for bigram in bigram_lst}
    
    #Calculate the odds ratios
    odds_pos = {bigram:pos_prob[bigram]/(1-pos_prob[bigram]) for bigram in bigram_lst if pos_prob[bigram] not in [0,1] and neg_prob[bigram] not in [0,1]}
    odds_neg = {bigram:neg_prob[bigram]/(1-neg_prob[bigram]) for bigram in bigram_lst if pos_prob[bigram] not in [0,1] and neg_prob[bigram] not in [0,1]}
    
    #Calculate the log odds ratio for each bigram
    log_odds_ratio_rows = []
    for bigram in odds_pos.keys():
        log_odds_ratio_rows.append({"bigram": bigram, "log_odds_ratio": round(log(odds_pos[bigram]/odds_neg[bigram],10),4)})
    log_odds_df = pd.DataFrame(log_odds_ratio_rows)
    log_odds_df = log_odds_df.sort_values(by="log_odds_ratio",ascending=True)
    log_odds_df.to_csv('task7a.csv',index=False)
    
    #Task7b: Create a histogram for the log_odds_ratios
    plt.style.use('seaborn-darkgrid') 
    fig,ax = plt.subplots()
    ax.hist(log_odds_df['log_odds_ratio'],rwidth=0.95,color='coral',bins=14)
    ax.set_title("Distribution of the log odds ratios")
    ax.set_xlabel("log10(or(b))")
    ax.set_ylabel("Frequency")
    plt.tight_layout()
    plt.savefig('task7b.png')
    plt.close()

    #Task7c: Create a bar chart
    top10 = log_odds_df.tail(10)
    bottom10 = log_odds_df.head(10)
    top10 = top10.set_index('bigram')
    bottom10 = bottom10.set_index('bigram')
    extreme_odds = pd.concat([top10,bottom10])
    
    fig2,ax2 = plt.subplots()
    plt.style.use('fivethirtyeight') 

    ####################################################################################################################################
    ####The code below was adapted from the highest upvoted solution in this stack overflow thread:
    #### https://stackoverflow.com/questions/22311139/bar-chart-how-to-choose-color-if-value-is-positive-vs-value-is-negative
    extreme_odds['positive'] = extreme_odds['log_odds_ratio']>0
    extreme_odds['log_odds_ratio'].plot(kind='barh',color=extreme_odds.positive.map({True:'g',False:'firebrick'}),figsize=(18,10))
    ####################################################################################################################################

    ax2.set_ylabel("Bigrams",fontsize=16)
    ax2.set_xlabel("lor(b)",fontsize=16)
    ax2.set_title("The highest and lowest odds ratios in the vocabulary",fontsize=20)
    fig2.savefig('task7c.png')
    return

