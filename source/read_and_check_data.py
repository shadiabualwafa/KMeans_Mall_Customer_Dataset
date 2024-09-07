# read_and_check_data.py

import pandas as pd

def customer_dataset():
    # Load the dataset and return it
    dataset = pd.read_csv("D:/Courses/Data Science/Data/mall_customer_dataset.csv")
    return dataset
