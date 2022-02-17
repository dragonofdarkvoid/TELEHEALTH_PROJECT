import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
from pandas import read_csv

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a
def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y
order = 5
fs = 100
cutoff = 40
b, a = butter_lowpass(cutoff, fs, order)
w, h = freqz(b, a, worN=8000)

def dataset_filtering(filename):
    #importdata
    ppgdataset = read_csv('normalized_data/normalized_'+filename, header=0, index_col=False)
    print(ppgdataset)
    ppg_rows = len(ppgdataset.index)

    irled= ppgdataset.iloc[:, 1:2]
    irled_val = irled.values

    redled = ppgdataset.iloc[:, 2:3]
    redled_val = redled.values

    # Demonstrate the use of the filter.
    # First make some data to be filtered.
    T = ppg_rows/44         # seconds
    n = ppg_rows # total number of samples
    t = np.linspace(0, T, n, endpoint=False)
    # "Noisy" data.  We want to recover the 1.2 Hz signal from this.


    # Filter the data, and plot both the original and filtered signals.
    filtered_redled = butter_lowpass_filter(redled_val, cutoff, fs, order)
    filtered_irled = butter_lowpass_filter(irled_val, cutoff, fs, order)
    ppgdataset.iloc[:,1:2] = filtered_irled
    ppgdataset.iloc[:,2:3] = filtered_redled

    ppgdataset.to_csv("filtered_data/filtered_"+filename, index = False)

    return ppgdataset
