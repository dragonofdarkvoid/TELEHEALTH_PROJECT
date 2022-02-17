# Normalize time ppg data
from pandas import read_csv
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def extract_feature(filename):
    ppg=read_csv('filtered_data/filtered_'+filename, header=None, index_col=False, skiprows=1)
    #prepare data
    normalized = pd.DataFrame(ppg)
    main = normalized.iloc[:, 1:3]
    feature1 = main.diff(axis=1, periods=1)
    feature1 = feature1.dropna(axis=1)
    feature1 = feature1.abs()

    feature2 = main.diff(axis=0, periods =1)
    feature2 = feature2.abs()
    feature2 = feature2.dropna(axis=0)

    features=pd.concat([normalized, feature1, feature2], axis=1)


    features =features.dropna()



    features.to_csv("features/features_"+filename, index=False, header=['Category', 'IRLED', 'REDLED', 'HEARTRATE',
                                        'OXYGEN', 'FEATURE1', 'FEATURE2', 'FEATURE3'])
    return filename, normalized
