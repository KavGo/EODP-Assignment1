import json
import pandas as pd

def task1():
    df = pd.read_csv('../course/data/dataset.csv')
    X = df['ID'].nunique()
    Y = df.category.unique().size
    info = {"Number of Products:": X, "Number of Categories:": Y}
    json.dump(info,open("task1.json", "w"))

    return None
