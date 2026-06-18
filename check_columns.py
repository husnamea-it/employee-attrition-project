from joblib import load

model = load("attrition_model1.joblib")

print(model.feature_names_in_)