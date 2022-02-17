
import datetime
import pandas as pd
from pymongo import MongoClient
try:
    conn = MongoClient()
    print("Connected to MongoDB")
except:
    print("Could not connect to MongoDB")
def import_content(filename):
    client = MongoClient("mongodb+srv://kenny:sitiajaib@cluster0.nlxih.mongodb.net/telehealth?retryWrites=true&w=majority")
    db = client['apitelehealth']
    collection = db['patientdatas']
    data = pd.read_csv("patient_databases/"+filename)
    data.set_index("date",inplace=False)
    data_dict = data.to_dict("records")
    collection.insert_many(data_dict)
    print("Data Uploaded to MongoDB")


