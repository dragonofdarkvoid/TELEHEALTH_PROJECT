import time
from datetime import datetime
from pandas import read_csv
import Filtering_PPG
import feature_extraction
import gathering_all_params
import get_serial
import integrasimongodb
import normalization_real
import predict_blood_pressure
import split_raw_data
import feature_extraction
rawdatas = []
patientname = input("Patient's name : ")
filename = patientname + ".csv"
database = input ("Is this time the first time?")
if database == 'y':
    config_file = True
else:
    config_file = True
f_extns = filename.split(".")
print("The Extension of the file is : " + repr(f_extns[-1]))
port = input("Insert Computer Port : ")
if (port == '0'):
    com = "/dev/ttyACM0"
elif (port =='1'):
    com = "/dev/ttyACM1"
elif (port =='2'):
    com = "/dev/ttyACM2"
current = datetime.now()
current_time = current.strftime("%D||%H:%M:%S")
print("Current Time = ", current_time)
start_state = input ("Start the Measurement? y|n = ")
if (start_state == 'y') :
    print("HEALTH PARAMETERS MEASUREMENT ......")
    get_serial.read_serial(filename, com, rawdatas)
    print("SAVING INITIAL DATA ......")
    get_serial.save_to_csv(filename,rawdatas)
    print("PREPROCESSING THE INITIAL DATA ......")
    split_raw_data.split_data_to_csv(filename)
    normalization_real.normalize_data(filename)
    Filtering_PPG.dataset_filtering(filename)
    preprocessed_data = read_csv("filtered_data/filtered_"+filename, index_col =0)
    print("Filtered_Data :")
    print(preprocessed_data)
    feature_extraction.extract_feature(filename)
    predict_blood_pressure.predict_systole(filename)
    predict_blood_pressure.predict_diastole(filename)
    gathering_all_params.gather_all_data(filename, patientname, config_file)
    integrasimongodb.import_content(filename)