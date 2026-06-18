from joblib import load

model = load("attrition_model1.joblib")

print("Model loaded successfully!")
print(type(model))