#BMI CALCULATOR
import streamlit as st
import time 

st.set_page_config(
    page_title="BMI Calculator ",
    page_icon="😊",
    layout="centered"
)

st.title("Project 1 - BMI Calculator 😊")

st.markdown("""
This is a simple BMI calculator for **weight and height** Enter kare.
""")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Enter your weight (kg):", min_value=0.0, max_value=200.0, step=0.1, value=70.0)

with col2:
    height = st.number_input("Enter your height (cm):", min_value=0.0, max_value=200.0, step=0.1, value=170.0)

if st.button("Calculate"):
    bmi = weight / ((height / 100) ** 2)
    st.subheader("Your Weight Status")
    st.write(f"{bmi:.2}",unsafe_allow_html=True)

    if bmi < 18.5:
        st.write("Underweight")
    elif 18.5 <= bmi < 24.9:
        st.write("Normal weight")
    elif 24.9 <= bmi < 29.9:
        st.write("Overweight")
    else:
        st.write("Obsity 🚨") 
    st.write("Please enter valid weights and heights")

