"""
code for model initialization services (preprocessing, encoding, etc)
"""

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from .config import config_by_name

def encode_labels(target_column):

    le = LabelEncoder()
    le.fit(y_train)
    y_train = le.transform(y_train)
    
    if ML_DATA_TESTING_CONFIG:
        y_test  = le.transform(y_test) 
    else: 
        pass    
    return y_train
