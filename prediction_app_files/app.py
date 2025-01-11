import streamlit as st
import pickle 
import numpy as np

with open (r"E:\Diamond Price Prediction\xgboost_best_model.pkl","rb") as file:
    model = pickle.load(file)

# Title of the app
st.title("Diamond Price Prediction App")
st.write("Enter the details of the diamond to predict its price.")

# Input fields for features
st.subheader("Enter Diamond Features")

# Carat size
carat = st.slider("Carat Size (in carats):", min_value=0.1, max_value=5.5, step=0.1)

# Cut quality
cut_options = ["Ideal", "Premium","Good", "Very Good", "Fair"]
cut = st.selectbox("Cut Quality:", cut_options)

# Encode the 'cut' feature (update based on your encoding in the dataset)
cut_encoding = {
    "Ideal": 1,
    "Premium": 2,
    "Good": 3,
    "Very Good": 4,
    "Fair": 5
}
cut_encoded = cut_encoding[cut]

# Dimensions (size)
size = st.number_input("Size = (length x width x depth):", min_value=0.0, step=0.1)

# Predict button
if st.button("Predict Price"):
    # Prepare the input features as a NumPy array
    input_features = np.array([[carat, cut_encoded, size]])

    # Make a prediction using the loaded XGBoost model
    predicted_price = model.predict(input_features)[0]

    # Display the prediction
    st.success(f"Predicted Diamond Price: ${predicted_price:,.2f}")


    