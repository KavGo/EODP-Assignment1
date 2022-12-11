import pandas as pd
import re
import json
import nltk
from nltk.corpus import stopwords

def task6():
    df = pd.read_csv('../course/data/dataset.csv')
    reviews = []
    
    for i, row in df.iterrows():
        reviewlst_str = row['REVIEWLIST']
        rev_lst = json.loads(reviewlst_str)

        for review in rev_lst:
            raw_star = review["review_star"]
            star = re.search(r'(?<=a-star-)\d',raw_star) #Positive lookbehind
            
            #Invalid score, skip the entry
            if star is None:
                continue
            star = int(star.group())

            #Text pre-processing
            raw_review = review["review_body"] 
            lowercased = raw_review.lower()
            alpha_char = re.sub(r'\\u|\\n|\\t|[^a-zA-Z\s]', ' ', lowercased)
            cleaned_text = re.sub(r'\s+', ' ', alpha_char)
            
            #Tokenise and remove stop words
            tokens = nltk.word_tokenize(cleaned_text)
            stop_words = set(stopwords.words("english"))
            non_stopwords = [word for word in tokens if word not in stop_words]
            clean_words = [word for word in non_stopwords if len(word)>2]

            #Form bigrams
            seq_pairs = [' '.join([clean_words[i],clean_words[i+1]]) for i in range(len(clean_words)-1)]
            #Invalid review
            if len(seq_pairs)==0:
                continue
            reviews.append({"score": star, "bigrams":seq_pairs})
        
    json.dump(reviews,open("task6.json", "w"))

    return
