CropWise: Crop Recommender System 🌱
CropWise is a machine learning-powered web application that helps farmers make informed crop selection decisions based on soil and climate parameters. It uses a trained Random Forest model to recommend the most suitable crops for specified environmental conditions.

Features
User-friendly web interface built with Streamlit.
Inputs include soil nutrients (Nitrogen, Phosphorus, Potassium), temperature, humidity, pH level, and rainfall.
Predicts optimal crop recommendation using a trained Random Forest classifier.
Robust error handling for model loading and prediction.
Interactive input forms with intuitive layouts.

Project Files
CRS.py=Streamlit app for crop recommendation UI and prediction logic.

Crop_Recommendation_Model.ipynb=Jupyter Notebook for dataset exploration, model training, evaluation, and saving.

Crop_model.pkl=Serialized Random Forest model loaded by the Streamlit app.

requirements.txt=Python dependencies required to run the project.
