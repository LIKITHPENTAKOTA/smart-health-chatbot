from chatbot.prediction import predict_disease

def start_chatbot():
    print("🤖 Welcome to Smart Health Chatbot!")
    print("👉 Enter your symptoms one by one. Type 'done' when finished.\n")

    symptoms = []
    while True:
        symptom = input("Enter symptom (or type 'done'): ").strip()
        if symptom.lower() == "done":
            break
        if symptom:
            symptoms.append(symptom)

    # Pad with no_symptom if user gave less than required
    while len(symptoms) < 17:
        symptoms.append("no_symptom")

    print("\n🔍 Analyzing your symptoms...")
    disease, description, precautions = predict_disease(symptoms[:17])

    print(f"\n🩺 Predicted Disease: {disease}")
    print(f"📖 Description: {description}")
    print("🛡️ Precautions:")
    for p in precautions:
        print(f" • {p}")
