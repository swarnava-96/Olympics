# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 16:24:45 2021

@author: SWARNAVA
"""

# Lets import pandas to read the datasets
import pandas as pd

# Lets define a function for basic data preprocessing
def preprocess(df, df1):
    
    # Lets filter the data for summer olympics
    df = df[df["Season"] == "Summer"]
    # Merging the two datasets
    df = df.merge(df1, on = "NOC", how = "left")
    # Dropping duplicates
    df.drop_duplicates(inplace = True)
    # One Hot Encoding on Medal
    df = pd.concat([df, pd.get_dummies(df["Medal"])], axis = 1)
    return df