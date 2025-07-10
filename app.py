import pandas as pd 
import pickle as pkl
import streamlit as st 
import numpy as np 


model =pkl.load(open('C:\Python310\House price prediction\House_prediction_model (2).pkl','rb')) 


st.header('Bangalore House Price Prediction')
data =pd.read_csv('C:\Python310\House price prediction\cleaned_data.csv')

loc = st.selectbox('choose the location', data['location'].unique())
sqft = st.number_input('Enter the total sqft')
beds = st.number_input('Enter the number of Bedrooms')
bath = st.number_input('Enter the number of Bathrooms')
balc = st.number_input('Enter the number of Balconies')


input_data = pd.DataFrame([[loc,sqft,bath,balc,beds]], columns=['location', 'total_sqft', 'bath', 'balcony', 'bedroom'])

if st.button('Predict Price'):
    output = model.predict(input)
    out_str ='Price of the house is Rs.' + str(output[0]* 100000)