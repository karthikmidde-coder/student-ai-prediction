import streamlit as st
import pandas as pd
import joblib # Or use your specific model loading library

# 1. Page Configuration
st.set_page_config(page_title="AI Student Predictor", layout="wide")

st.title("🎓 Student Performance Prediction System")
st.write("Enter the student details below to predict the final outcome.")

# 2. Input Features (Customize these to match your dataset)
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        attendance = st.slider("Attendance Percentage", 0, 100, 85)
        study_hours = st.number_input("Study Hours per Week", 0, 50, 10)
        
    with col2:
        prev_grade = st.number_input("Previous Grade (0-100)", 0, 100, 75)
        extracurricular = st.selectbox("Extracurricular Activities", ["Yes", "No"])

    submit = st.form_submit_button("Predict Performance")

# 3. Prediction Logic
if submit:
    # Convert 'Yes/No' to numeric if your model requires it
    activities = 1 if extracurricular == "Yes" else 0
    
    # Prepare the data for the model
    input_data = [[attendance, study_hours, prev_grade, activities]]
    
    try:
        # Load your pre-trained model (Replace 'model.pkl' with your file)
        # model = joblib.load('student_model.pkl')
        # prediction = model.predict(input_data)
        
        # FOR DEMO ONLY: Mock logic if you don't have the .pkl file ready yet
        prediction = (attendance * 0.3) + (study_hours * 0.4) + (prev_grade * 0.3)
        
        st.divider()
        st.subheader(f"Predicted Score: {round(prediction, 2)}%")
        
        if prediction >= 50:
            st.success("Result: Likely to Pass ✅")
        else:
            st.error("Result: At Risk of Failure ⚠️")
            
    except Exception as e:
        st.warning("Model file not found. Showing mock prediction for DTI demo.")