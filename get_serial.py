import csv
import re
import serial
import time
import pandas as pd

from datetime import datetime

def read_serial(filename, port, data):
    ser = serial.Serial(port, 9600, timeout=1)
    ser.setDTR(False)
    time.sleep(1)
    ser.setDTR(True)
    time.sleep(0.1)

    for i in range (2000):
        line = ser.readline().strip()
        if line:
            rawdata = line.decode(encoding="unicode_escape")
            print(rawdata)
            newrawdata = re.findall(r'^\w+|\d+\.\d+|\d+', rawdata)
            data.append(newrawdata)
    ser.close()
    return (filename,port,data)

def save_to_csv(filename,rawdatas):
    rawdata = pd.DataFrame(rawdatas)
    print(rawdata)
    rawdata.to_csv("rawdata/" +filename, index =False, header= ["Category","Value1","Value2", "Value3", "Value4"])
    return filename, rawdata
