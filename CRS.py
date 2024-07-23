# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 18:35:47 2024

@author: Dell
"""

import streamlit as st
import pandas as pd
import numpy as np
import os
import warnings
import joblib
from streamlit_option_menu import option_menu
import sklearn
import base64
import pickle
import pickle

import pickle
from sklearn.ensemble import RandomForestClassifier

# Set page configuration with Unicode emoji for the icon
st.set_page_config(
    page_title="CropWise",
    layout="wide",
    page_icon="🌱"  # Unicode representation of the plant emoji
)

# Custom CSS for background image
st.markdown(
    """
    <style>
    .stApp {
        
        background-color: #D0E7D2; /* Light pastel color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load model with exception handling
try:
    st.write("Loading model...")
    crop_model = joblib.load('C:/Users/Dell/Desktop/Crop_recommender_project/RandomForest.pkl')
    st.write("Model loaded successfully.")
except FileNotFoundError:
    st.error("Model file not found. Please check the file path.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()

def main():
    # Title
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Crop Recommendation  🌱 </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Instruction
    col1, col2 = st.columns([2, 2])

    with col1:
        with st.expander("Instruction", expanded=True):
            st.write("""
            Crop recommendation is a tool that helps farmers make informed decisions about the crops they should grow.
            It includes various factors like temperature, humidity, Ph level and rainfall to provide personalized recommendation to farmers.
            """)

    # How it works
    st.markdown("## How does it work ❓")
    st.markdown("Enter all the parameters and the machine learning model will predict the most suitable crops to grow in a particular farm based on various parameters.")

    # Input columns
    col1, col2, col3 = st.columns(3)

    with col1:
        N = st.number_input('Nitrogen (in ppm)', min_value=0.0, step=1.0)

    with col2:
        P = st.number_input('Phosphorous (in ppm)', min_value=0.0, step=1.0)

    with col3:
        K = st.number_input('Potassium (in ppm)', min_value=0.0, step=1.0)

    with col1:
        temp = st.number_input('Temperature (°C)', min_value=-10.0, max_value=60.0, step=1.0)

    with col2:
        humidity = st.number_input('Humidity (%)', min_value=0.0, max_value=100.0, step=1.0)

    with col3:
        ph = st.number_input('Ph (1-14)', min_value=0.0, max_value=14.0, step=0.1)

    with col1:
        rainfall = st.number_input('Rainfall (mm)', min_value=0.0, step=0.01)

    # Prediction and recommendation
    crop_recommendation = ''

    if st.button('Recommend Crop'):
        st.write("Button clicked, making prediction...")
        user_input = [N, P, K, temp, humidity, ph, rainfall]
        user_input = [float(x) for x in user_input]

        try:
            crop_prediction = crop_model.predict([user_input])
            crop_recommendation = f'The recommended crop is: {crop_prediction[0]}'
            st.write("Prediction successful.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
            st.write("Prediction failed.")

    st.success(crop_recommendation)

if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()

