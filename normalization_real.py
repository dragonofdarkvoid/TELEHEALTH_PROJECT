# Normalize time ppg data
from pandas import read_csv
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def normalize_data(filename):
    ppg=read_csv('rawdata/'+filename, header=0, index_col=False)
    #prepare data
    normalized = pd.DataFrame(ppg)
    normalized = normalized[normalized['Value1'] >= 800]
    normalized = normalized[normalized['Value2'] >= 800]
    normalized = normalized[normalized['Value3'] >= 1]
    normalized = normalized[normalized['Value4'] >=90]
    print("NORMALIZED DATA")
    print(normalized)
    x= normalized.iloc[:, 1:3]
    #train the normalization
    normalized.iloc[:, 1:3] = (x - x.min()) / (x.max() - x.min())
    normalized = normalized[normalized['Value1'] > 0]
    normalized = normalized[normalized['Value2'] > 0]
    normalized = normalized[normalized['Value3'] >= 1]
    normalized = normalized[normalized['Value4'] >= 90]
    print("ARTEFACT REMOVAL RESULTS")
    print(normalized)
    normalized.to_csv("normalized_data/normalized_"+filename, index=False)
    return filename, normalized