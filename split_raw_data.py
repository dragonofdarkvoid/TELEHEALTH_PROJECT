import csv
import pandas as pd



def split_data_to_csv (filename):
    recap = pd.read_csv("rawdata/"+filename, delimiter=',')
    df = pd.DataFrame(recap)
    print(df)
    temp = df.loc[df['Category']=='temp']
    print("This is Temp Data")
    print(temp)
    temp.to_csv("temp/temp_" +filename, index =False)
    ppg = df.loc[df['Category']=='ppg']
    print("This is PPG Based Data")
    print(ppg)
    ppg.to_csv("ppg/ppg_" +filename, index = False)
    return (filename,df)


