import streamlit as st
import pickle
import pandas as pd

data = pickle.load(open('housing_data.pkl', 'rb'))
model = pickle.load(open('model_housing.pkl', 'rb'))

st.title("🏠 House Price Predictor")

location = st.selectbox(
    "Select the Location",
    (data['location'].unique())
)

bhk = st.selectbox(
    "Size of house (BHK)",
    (sorted(data['bhk'].unique()))
)

bathrooms = st.select_slider(
    "Select number of Bathrooms",
    options=sorted(data['bath'].unique())
)

sqft = st.number_input(
    "Enter the area of house (sqft)",
    min_value=0.0,
    format="%.2f",
    placeholder="Type a number..."
)


if st.button("Predict Price"):
    if sqft > 0:
        input_df = pd.DataFrame([{
            'location': location,
            'total_sqft': sqft,
            'bath': bathrooms,
            'bhk': bhk
        }])
        prediction = model.predict(input_df)[0]
        st.success(f"Estimated Price: ₹{prediction:,.2f} Lakhs")
    else:
        st.warning("Please enter a valid area before predicting.")
