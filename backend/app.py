from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, mutual_info_classif
import joblib

app = Flask(__name__)
CORS(app)

# Load data
df = pd.read_csv("SaYoPillow.csv")

# Rename columns for better readability
df.columns = [
    "snoring range",
    "respiration rate",
    "body temperature",
    "limb movement rate",
    "blood oxygen levels",
    "eye movement",
    "number of hours of sleep",
    "heart rate",
    "Stress Levels",
]

# Split data into features (x) and target (y)
x = df.drop(columns=["Stress Levels"])
y = df["Stress Levels"]

# Perform feature selection using SelectKBest
kbest = SelectKBest(mutual_info_classif, k=4)
x_selected = kbest.fit_transform(x, y)

# Train the Random Forest model with selected features
model = RandomForestClassifier()
model.fit(x_selected, y)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    snoring_range = float(data["field1"])
    heart_rate = float(data["field2"])
    blood_oxygen_levels = float(data["field3"])
    respiration_rate = float(data["field4"])

    # Make prediction
    input_data = [[snoring_range, heart_rate, blood_oxygen_levels, respiration_rate]]
    prediction = model.predict(input_data)[0]

    # Convert numpy.int64 to native int
    prediction = int(prediction)

    return jsonify({"predictedStressLevel": prediction})


def recommend_management(stress_level, age, chronic_diseases):
    # Define management techniques based on age groups and stress levels
    management_techniques = {
        "0-30": {
            0: {"Physical Activity": ["Regular exercise", "Walking", "Swimming"],
                "Diet and Sleep": ["Healthy diet", "Adequate sleep", "Hydration"],
                "Mental Well-being": ["Mindfulness meditation", "Deep breathing exercises", "Progressive muscle relaxation"]},
            1: {"Physical Activity": ["Yoga", "Tai chi", "Pilates"],
                "Stress Reduction": ["Journaling", "Art therapy", "Music therapy"],
                "Social Support": ["Spending time with loved ones", "Joining social groups", "Supportive therapy groups"]},
            2: {"Therapeutic Support": ["Professional counseling", "Cognitive-behavioral therapy", "Stress management workshops"],
                "Hobbies and Leisure": ["Engaging in hobbies", "Reading", "Gardening"],
                "Time Management": ["Time management techniques", "Setting boundaries", "Prioritizing tasks"]},
            3: {"Medication and Therapy": ["Medication under doctor's supervision", "Psychotherapy", "Group therapy"],
                "Self-care Practices": ["Relaxation techniques", "Healthy lifestyle habits", "Self-compassion practices"],
                "Support System": ["Seeking social support", "Joining support groups", "Peer counseling"]},
            4: {"Specialized Treatment": ["Consulting a mental health professional", "Hospitalization if necessary", "Intensive therapy programs"],
                "Community Support": ["Support groups", "Community mental health resources", "Online forums"],
                "Integrated Care": ["Medication and therapy", "Integration of mental health with chronic disease management", "Holistic treatment approaches"]}
        },
        "30-60": {
            0: {"Physical Activity": ["Gentle exercises", "Walking", "Swimming"],
                "Diet and Sleep": ["Healthy diet", "Adequate sleep", "Hydration"],
                "Mental Well-being": ["Mindfulness meditation", "Deep breathing exercises", "Progressive muscle relaxation"]},
            1: {"Physical Activity": ["Yoga", "Tai chi", "Pilates"],
                "Stress Reduction": ["Journaling", "Art therapy", "Music therapy"],
                "Social Support": ["Spending time with loved ones", "Joining social groups", "Supportive therapy groups"]},
            2: {"Therapeutic Support": ["Professional counseling", "Cognitive-behavioral therapy", "Stress management workshops"],
                "Hobbies and Leisure": ["Engaging in hobbies", "Reading", "Gardening"],
                "Time Management": ["Time management techniques", "Setting boundaries", "Prioritizing tasks"]},
            3: {"Medication and Therapy": ["Medication under doctor's supervision", "Psychotherapy", "Group therapy"],
                "Self-care Practices": ["Relaxation techniques", "Healthy lifestyle habits", "Self-compassion practices"],
                "Support System": ["Seeking social support", "Joining support groups", "Peer counseling"]},
            4: {"Specialized Treatment": ["Consulting a mental health professional", "Hospitalization if necessary", "Intensive therapy programs"],
                "Community Support": ["Support groups", "Community mental health resources", "Online forums"],
                "Integrated Care": ["Medication and therapy", "Integration of mental health with chronic disease management", "Holistic treatment approaches"]}
        },
        "60 above": {
            0: {"Physical Activity": ["Gentle exercises", "Walking", "Water aerobics"],
                "Diet and Sleep": ["Healthy diet", "Adequate sleep", "Hydration"],
                "Mental Well-being": ["Mindfulness meditation", "Deep breathing exercises", "Light stretching"]},
            1: {"Physical Activity": ["Gentle yoga", "Tai chi", "Pilates"],
                "Stress Reduction": ["Journaling", "Art therapy", "Music therapy"],
                "Social Support": ["Spending time with loved ones", "Joining social groups", "Supportive therapy groups"]},
            2: {"Therapeutic Support": ["Professional counseling", "Cognitive-behavioral therapy", "Stress management workshops"],
                "Hobbies and Leisure": ["Engaging in hobbies", "Reading", "Gardening"],
                "Time Management": ["Time management techniques", "Setting boundaries", "Prioritizing tasks"]},
            3: {"Medication and Therapy": ["Medication under doctor's supervision", "Psychotherapy", "Group therapy"],
                "Self-care Practices": ["Relaxation techniques", "Healthy lifestyle habits", "Self-compassion practices"],
                "Support System": ["Seeking social support", "Joining support groups", "Peer counseling"]},
            4: {"Specialized Treatment": ["Consulting a mental health professional", "Hospitalization if necessary", "Intensive therapy programs"],
                "Community Support": ["Support groups", "Community mental health resources", "Online forums"],
                "Integrated Care": ["Medication and therapy", "Integration of mental health with chronic disease management", "Holistic treatment approaches"],
                "Physical Activity": ["Yoga", "Tai chi", "Pilates"]}  # Ensure "Physical Activity" is initialized
        }
    }

    # Adjust management techniques based on chronic diseases if needed
    if age > 60:
        if "Regular exercise" in management_techniques["60 above"][0]["Physical Activity"]:
            management_techniques["60 above"][0]["Physical Activity"].remove("Regular exercise")
        management_techniques["60 above"][0]["Physical Activity"].append("Gentle exercises")
    if "arthritis" in chronic_diseases:
        if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
            if "Yoga" in management_techniques["60 above"][1]["Physical Activity"]:
                management_techniques["60 above"][1]["Physical Activity"].remove("Yoga")
            management_techniques["60 above"][1]["Physical Activity"].append("Water aerobics")
    if "diabetes" in chronic_diseases:
        if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
            management_techniques["60 above"][2]["Diet and Sleep"].append("Monitoring blood sugar levels")
        if "Physical Activity" in management_techniques["60 above"][2]:  # Check if "Physical Activity" exists
            management_techniques["60 above"][2]["Physical Activity"].append("Regular blood sugar monitoring")
    if "hypertension" in chronic_diseases:
        if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
            management_techniques["60 above"][3]["Medication and Therapy"].append("Blood pressure monitoring")
            management_techniques["60 above"][3]["Diet and Sleep"].append("Low sodium diet")
    if "asthma" in chronic_diseases:
        if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
            management_techniques["60 above"][4]["Specialized Treatment"].append("Inhaler usage guidance")
            management_techniques["60 above"][4]["Physical Activity"].append("Breathing exercises")
    if "chronic obstructive pulmonary disease (COPD)" in chronic_diseases:
        if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
            management_techniques["60 above"][4]["Specialized Treatment"].append("Bronchodilator therapy")
            management_techniques["60 above"][4]["Physical Activity"].append("Pulmonary rehabilitation exercises")

    age_group = ""
    if age <= 30:
        age_group = "0-30"
    elif 30 < age <= 60:
        age_group = "30-60"
    else:
        age_group = "60 above"

    recommendations = management_techniques[age_group][stress_level]

    return recommendations


@app.route("/management", methods=["POST"])
def management():
    data = request.json
    stress_level = int(data["stressLevel"])
    age = int(data["age"])
    chronic_diseases = data["chronicDiseases"]

    recommended_techniques = recommend_management(stress_level, age, chronic_diseases)
    return jsonify(recommended_techniques)


if __name__ == "__main__":
    app.run(debug=True)