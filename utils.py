import joblib 
import numpy as np

def preprocess(Open, High, Low, Volume):
    test_data = [[Open, High, Low, Volume]]
    trained_model = joblib.load('model.pkl')
    prediction = trained_model.predict(test_data)
    return prediction