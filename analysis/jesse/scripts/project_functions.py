import pandas as pd
import numpy as np
def load_and_process(url):
    # Method Chain 1 (Load and remove unneccasary columns and rows with too many missing values)
    df1 = (
        pd.read_csv(url, error_bad_lines=False)
        .drop(columns = ['country', 'province', 'city', 'infection_case', 'symptom_onset_date'])
        .dropna(thresh=5)
        .reset_index()
        .drop(columns = 'index')
       .rename(columns = {"age":"approximate_age"})
    )
    # Method Chain 2 (Remove the s from the age column)
    df1['approximate_age'] = (
        df1['approximate_age']
        .str
        .replace(r's$', '')
    )
    
    return df1