"""
code for loading datasets
"""
import pandas as pd



def load_data():
    """loads data on import of package"""
    if ML_DATA_TESTING_CONFIG:
        f = 'rspct_10k.csv'
        data = pd.read_csv()
    return data
