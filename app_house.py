import streamlit as st
import pandas as pd
import joblib

model = joblib.load('ph_house_prices.pkl')
model_columns=joblib.load('model_columns.pkl')
st.title("Philippine Real State Price Predictor")
st.write("Estimate the market value of properties across the Philippines.")

col1,col2=st.columns(2)

with col1:
    location=st.selectbox(
        "Select location",
        ['Makati','Quezon City','Cebu City','Davao City','Calamba']
    )
    area=st.number_input(
        "Floor area(sqm)",
        20,
        500,
        100
    )
with col2:
    rooms=st.number_input(
        "Number of Bedrooms",
        1,
        10,
        2
    )
if st.button("Calculate estimated price"):
    input_df=pd.DataFrame(
        0,
        [0],
        columns=model_columns
    )
    input_df['Bedrooms']=rooms
    input_df['Area_sqm']=area

    loc_column='Location_'+location
    if loc_column in model_columns:
        input_df[loc_column]=1

    prediction=model.predict(input_df)[0]

    st.divider()
    st.subheader(f"Estimated Price: ₱{prediction:,.2f}")

    price_per_sqm=prediction/area
    st.info(f"Average Price per sqm in this area: ₱{price_per_sqm:,.2f}")