# first neural network with keras tutorial
import keras.losses
from pandas import read_csv
from keras.models import model_from_json
import tensorflow as tf
import pandas as pd
# load the dataset
def predict_systole(filename):
    dataset = read_csv("features/features_"+filename, delimiter=',', skiprows=0,index_col =False)
    # split into input (X) and output (y) variables
    X = dataset.iloc[:, 1:8]
    sample = tf.linspace(1.0, 700.0, num=700)
    print(X)

    json_file = open('model_sys.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model_sys.h5")
    print("Loaded model from disk")
    loaded_model.compile(loss=keras.losses.MeanAbsoluteError(), optimizer='adam')
    predictions = loaded_model.predict(X).astype(int)
    for i in range (100):
        print('(Systole Predictions) => %d ' % (predictions[i]))

    systole = pd.DataFrame(predictions)

    print(systole)
    systole.to_csv('predicted/SystoleResult'+filename, sep=',', index=False)
    return systole
def predict_diastole(filename):
    dataset = read_csv("features/features_"+filename, delimiter=',', skiprows=0,index_col =False)
    # split into input (X) and output (y) variables
    X = dataset.iloc[:, 1:8]
    sample = tf.linspace(1.0, 700.0, num=700)
    print(X)

    json_file = open('model_dia.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model_dia.h5")
    print("Loaded model from disk")
    loaded_model.compile(loss=keras.losses.MeanAbsoluteError(), optimizer='adam')
    predictions = loaded_model.predict(X).astype(int)
    for i in range (100):
        print('(Diastole Predictions) => %d ' % (predictions[i]))

    diastole = pd.DataFrame(predictions)

    print(diastole)
    diastole.to_csv('predicted/DiastoleResult'+filename,sep=',', index=False)
    return diastole