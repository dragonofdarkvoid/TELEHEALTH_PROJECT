import pandas as pd
import os
from pandas import read_csv
from datetime import datetime
def gather_all_data (filename, patientname, config_file):
    current = datetime.now()

    current_date = current.strftime("%Y-%m-%d")
    current_time = current.strftime("%H:%M:%S")
    date = pd.DataFrame([current_date])
    time = pd.DataFrame([current_time])
    patient = pd.DataFrame([patientname])
    ppg_based_data = read_csv("filtered_data/filtered_" + filename, index_col=False, skiprows=1)
    estimated_systole = read_csv("predicted/SystoleResult" + filename, index_col=False, skiprows=1)
    estimated_diastole = read_csv("predicted/DiastoleResult" + filename, index_col=False, skiprows=1)
    temp_data = read_csv("temp/temp_" + filename, index_col=False, skiprows=1)
    ppg_data = ppg_based_data.iloc[:, 3:5]

    systole_result = estimated_systole
    diastole_result = estimated_diastole
    temperature = temp_data.iloc[:, 2:3]

    timing = pd.concat([patient,date, time])
    data_format = [ppg_data, systole_result, diastole_result, temperature]
    dataset = pd.concat(data_format, axis=1)
    averaged_data = dataset.mean(skipna=True, numeric_only=True).astype(int)
    averaged_dataset = pd.DataFrame(averaged_data)
    usia = input("Usia Pasien: ")
    jenis_kelamin = input("Jenis Kelamin Pasien: ")
    tinggi=input("Tinggi Badan Pasien: ")
    berat = input("Berat Badan Pasien: ")
    riwayat = input("Medical Records Pasien: ")
    kamar = input("Ruangan Kamar Pasien: ")
    usiadf = pd.DataFrame([usia])
    jkdf = pd.DataFrame([jenis_kelamin])
    tinggidf = pd.DataFrame([tinggi])
    beratdf = pd.DataFrame([berat])
    riwayatdf = pd.DataFrame([riwayat])
    kamardf = pd.DataFrame([kamar])
    datasetwithtime = pd.concat([averaged_dataset, timing, usiadf, jkdf, tinggidf, beratdf, riwayatdf, kamardf])
    print(datasetwithtime)
    datasetwithtime = datasetwithtime.transpose()
    print(datasetwithtime)


# if file does not exist write header
    if config_file == True:
        datasetwithtime.to_csv('patient_databases/'+filename, sep=",", index=False,
                                header=['heartrate', 'oxygen', 'systole', 'diastole',
                                        'body_temp', 'name', 'date','time', 'usia', 'jenis_kelamin','tinggi_badan','berat_badan','riwayat_penyakit', 'kamar'])

    else: # else it exists so append without writing the header
        datasetwithtime.to_csv('patient_databases/'+filename, mode='a', header=False, index=False)


