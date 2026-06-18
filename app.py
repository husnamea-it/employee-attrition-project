import streamlit as st
import pandas as pd
from joblib import load

# Load model
model = load("attrition_model1.joblib")

st.title("Employee Attrition Prediction System")

# Numeric Inputs
id = st.number_input("ID", value=1)
Age = st.number_input("Age", 18, 65, 30)
DailyRate = st.number_input("Daily Rate", value=500)
DistanceFromHome = st.number_input("Distance From Home", value=5)
Education = st.number_input("Education", 1, 5, 3)
EmployeeCount = st.number_input("Employee Count", value=1)
EnvironmentSatisfaction = st.number_input("Environment Satisfaction", 1, 4, 3)
HourlyRate = st.number_input("Hourly Rate", value=50)
JobInvolvement = st.number_input("Job Involvement", 1, 4, 3)
JobLevel = st.number_input("Job Level", 1, 5, 2)
JobSatisfaction = st.number_input("Job Satisfaction", 1, 4, 3)
MonthlyIncome = st.number_input("Monthly Income", value=5000)
MonthlyRate = st.number_input("Monthly Rate", value=10000)
NumCompaniesWorked = st.number_input("Number of Companies Worked", value=1)
PercentSalaryHike = st.number_input("Percent Salary Hike", value=15)
PerformanceRating = st.number_input("Performance Rating", 1, 4, 3)
RelationshipSatisfaction = st.number_input("Relationship Satisfaction", 1, 4, 3)
StandardHours = st.number_input("Standard Hours", value=80)
StockOptionLevel = st.number_input("Stock Option Level", 0, 3, 1)
TotalWorkingYears = st.number_input("Total Working Years", value=5)
TrainingTimesLastYear = st.number_input("Training Times Last Year", value=2)
WorkLifeBalance = st.number_input("Work Life Balance", 1, 4, 3)
YearsAtCompany = st.number_input("Years At Company", value=5)
YearsInCurrentRole = st.number_input("Years In Current Role", value=3)
YearsSinceLastPromotion = st.number_input("Years Since Last Promotion", value=1)
YearsWithCurrManager = st.number_input("Years With Current Manager", value=3)

# Categorical Inputs
BusinessTravel = st.selectbox(
    "Business Travel",
    ["Travel_Rarely", "Travel_Frequently", "Non-Travel"]
)

Department = st.selectbox(
    "Department",
    ["Sales", "Research & Development", "Human Resources"]
)

EducationField = st.selectbox(
    "Education Field",
    ["Life Sciences", "Medical", "Marketing",
     "Technical Degree", "Human Resources", "Other"]
)

Gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

JobRole = st.selectbox(
    "Job Role",
    ["Sales Executive", "Research Scientist",
     "Laboratory Technician", "Manufacturing Director",
     "Healthcare Representative", "Manager",
     "Sales Representative", "Research Director",
     "Human Resources"]
)

MaritalStatus = st.selectbox(
    "Marital Status",
    ["Single", "Married", "Divorced"]
)

Over18 = st.selectbox(
    "Over 18",
    ["Y"]
)

OverTime = st.selectbox(
    "Over Time",
    ["Yes", "No"]
)

if st.button("Predict Attrition"):

    data = pd.DataFrame({
        'id':[id],
        'Age':[Age],
        'BusinessTravel':[BusinessTravel],
        'DailyRate':[DailyRate],
        'Department':[Department],
        'DistanceFromHome':[DistanceFromHome],
        'Education':[Education],
        'EducationField':[EducationField],
        'EmployeeCount':[EmployeeCount],
        'EnvironmentSatisfaction':[EnvironmentSatisfaction],
        'Gender':[Gender],
        'HourlyRate':[HourlyRate],
        'JobInvolvement':[JobInvolvement],
        'JobLevel':[JobLevel],
        'JobRole':[JobRole],
        'JobSatisfaction':[JobSatisfaction],
        'MaritalStatus':[MaritalStatus],
        'MonthlyIncome':[MonthlyIncome],
        'MonthlyRate':[MonthlyRate],
        'NumCompaniesWorked':[NumCompaniesWorked],
        'Over18':[Over18],
        'OverTime':[OverTime],
        'PercentSalaryHike':[PercentSalaryHike],
        'PerformanceRating':[PerformanceRating],
        'RelationshipSatisfaction':[RelationshipSatisfaction],
        'StandardHours':[StandardHours],
        'StockOptionLevel':[StockOptionLevel],
        'TotalWorkingYears':[TotalWorkingYears],
        'TrainingTimesLastYear':[TrainingTimesLastYear],
        'WorkLifeBalance':[WorkLifeBalance],
        'YearsAtCompany':[YearsAtCompany],
        'YearsInCurrentRole':[YearsInCurrentRole],
        'YearsSinceLastPromotion':[YearsSinceLastPromotion],
        'YearsWithCurrManager':[YearsWithCurrManager]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Employee Likely To Leave Company")
    else:
        st.success("Employee Likely To Stay In Company")