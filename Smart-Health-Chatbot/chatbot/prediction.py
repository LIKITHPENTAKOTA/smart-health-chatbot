import pandas as pd
import joblib
import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Load model
model_path = os.path.join(MODEL_DIR, "best_model.pkl")
model = joblib.load(model_path)

# Load CSVs
desc_df = pd.read_csv(os.path.join(DATASET_DIR, "symptom_Description.csv"))
desc_df['Disease'] = desc_df['Disease'].str.strip().str.lower()

precaution_df = pd.read_csv(os.path.join(DATASET_DIR, "symptom_precaution.csv"))
precaution_df['Disease'] = precaution_df['Disease'].str.strip().str.lower()

severity_df = pd.read_csv(os.path.join(DATASET_DIR, "symptom_severity.csv"))
severity_df['Symptom'] = severity_df['Symptom'].str.strip().str.lower()

# Create severity dictionary
symptom_severity_dict = dict(zip(severity_df['Symptom'], severity_df['weight']))

# Disease prediction function
def predict_disease(symptom_list):
    cleaned = [s.strip().lower() for s in symptom_list]
    vector = [symptom_severity_dict.get(s, 0) for s in cleaned]

    prediction = model.predict([vector])[0].strip().lower()

    # Description
    description = desc_df[desc_df['Disease'] == prediction]['Description'].values
    description = description[0] if len(description) > 0 else "Description not available."

    # Precautions
    precautions = precaution_df[precaution_df['Disease'] == prediction].iloc[:, 1:].values
    precautions = precautions[0].tolist() if len(precautions) > 0 else ["No precautions available."]

    return prediction.title(), description, precautions
