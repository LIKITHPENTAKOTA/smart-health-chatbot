from flask import Flask, render_template, request
from chatbot.prediction import predict_disease

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    symptoms = request.form.get("symptoms")
    symptoms_list = [s.strip() for s in symptoms.split(",")]

    # Pad to 17 symptoms
    while len(symptoms_list) < 17:
        symptoms_list.append("no_symptom")

    disease, description, precautions = predict_disease(symptoms_list[:17])

    return render_template("result.html",
                           disease=disease,
                           description=description,
                           precautions=precautions)

if __name__ == "__main__":
    app.run(debug=True)
