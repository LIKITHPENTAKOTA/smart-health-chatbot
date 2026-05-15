from flask import Flask, render_template, request, jsonify
from chatbot.prediction import predict_disease

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_response():
    user_input = request.json.get("message")

    # Convert input into list of symptoms
    symptoms_list = [s.strip().lower() for s in user_input.split(",")]

    # Pad to 17 symptoms
    while len(symptoms_list) < 17:
        symptoms_list.append("no_symptom")

    disease, description, precautions = predict_disease(symptoms_list[:17])

    # Construct bot reply
    bot_reply = f"🩺 Predicted Disease: {disease}\n\n📖 {description}\n\n🛡️ Precautions:\n" + "\n".join([f"• {p}" for p in precautions])

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
