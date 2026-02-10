import streamlit as st
import numpy as np
import joblib
model =joblib.load('student_performance_model.pkl')
st.title("Student Performance Prediction")
attendance = st.number_input("Enter attendance percentage: ", min_value=0, max_value=100)
study_hours = st.number_input("Enter study hours per week: ", min_value=0,max_value=15)
previous_scores = st.number_input("Enter previous scores: ", min_value=0, max_value=100)
if st.button("Predict"):
    new_data = np.array([[attendance, study_hours, previous_scores]])
    prediction = model.predict(new_data)
    if prediction[0] == 1:
        st.success("The student is likely to pass.")
    else:
        st.error("The student is likely to fail.")
        