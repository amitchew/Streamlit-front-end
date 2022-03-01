# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 11:30:39 2022

@author: ragna
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st
loaded_model = pickle.load(open(r'C:\Users\ragna\Desktop\ML projects\trained_model.sav', 'rb'))

# Creating a function 
def diabetes_prediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return'The person is diabetic'



def main():
    
    #Giving a title for the webpage
    st.title('Diabetes Prediction Web App')
    
    # Getting the input data from the user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose= st.text_input('Glucose Level')
    BloodPressure= st.text_input('BP')
    SkinThickness= st.text_input('Skin Thickness')
    Insulin= st.text_input('Insulin Level')
    BMI= st.text_input('Get BMI')
    DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function Value')
    Age= st.text_input('Age')
    
    
    #code for Prediction
    diagnosis = ''
    #Creaing a button for prediction
    if st.button("Diabetes Test Result"):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
        BMI, DiabetesPedigreeFunction, Age])
    st.success(diagnosis)
    

    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
