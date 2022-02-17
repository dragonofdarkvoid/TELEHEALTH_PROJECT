# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine
import pandas as pd
# DEFINE THE DATABASE CREDENTIALS
user = 'kenny'
password = 'sitiajaib'
host = 'localhost'
port = 3306
database = 'biosignal_db'



# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
connection= create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database))
mydict = {
            'heartrate':[78, 79, 71, 78],
            'oxygen':[95,98,95,95],
            'systole':[120,132,122,120],
            'diastole':[86, 76,85, 86],
            'body_temp':[37.5,37.2,36.3,37.5],
            'date':["2022-01-24","2022-01-24","2022-01-24","2022-01-24"],
            'time':["10:15:00","10:16:00","10:18:00","10:20:00"],
            'name':["Bpk. James","Bpk.Dodit", "Bpk. Adi","Bpk. Imanuel"],
            'id':["0","0","0","0"]
}

df = pd.DataFrame(mydict)
print(df)
df.to_sql(name='patient_databases',con=connection, if_exists='append', index=False)
#if __name__ == '__main__':

 #   try:

        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
  #      engine = get_connection()
   #     print(
      #      f"Connection to the {host} for user {user} created successfully.")
    #except Exception as ex:
     #   print("Connection could not be made due to the following error: \n", ex)
